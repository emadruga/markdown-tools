#!/usr/bin/env python3
"""
Markdown -> DOCX para documentos normativos DOQ-Inmetro.

Converte o markdown do DOQ-DIMCI-020 (e documentos irmãos com a mesma
estrutura) para um .docx que replica o padrão visual institucional do
PDF de referência: documento monocromático, fonte sans-serif, cabeçalho
em tabela (logo INMETRO | código do documento | revisão | página) em
todas as páginas exceto a capa, capa simples, sumário com hyperlinks
internos e campo TOC nativo do Word, tabelas com bordas simples e
cabeçalho em negrito.

Uso:
    python markdown2doq_docx.py <input.md> [-o output.docx]
"""

import argparse
import logging
import os
import re
import sys
import unicodedata
from pathlib import Path

_level = getattr(logging, os.environ.get('LOGLEVEL', 'INFO').upper(), logging.INFO)
logging.basicConfig(format='%(levelname)s: %(message)s', level=_level)
log = logging.getLogger(__name__)

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SCRIPT_DIR = Path(__file__).resolve().parent
LOGO_PATH = SCRIPT_DIR / "inmetro-logo.png"

DOC_CODE = "DOQ-DIMCI-020"
DOC_REV = "REV. 01"

# Rodapé institucional (modelo MOD-Gabin-039). Referências ainda a confirmar
# (decisão §5.2 do PLANO_TEMPLATE_CONFORMIDADE) — deixadas fora por ora.
FOOTER_TEXT = (
    "DOQ-DIMCI-020 - Rev. 01 – Publicado Jun/2026 – Responsabilidade: Dmtic"
)


# ---------------------------------------------------------------------------
# Low level XML helpers
# ---------------------------------------------------------------------------

def set_cell_border(cell, **kwargs):
    """Aplica bordas simples (single, sz=4, auto) a uma célula de tabela."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = tcPr.find(qn('w:tcBorders'))
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)
    for edge in ('top', 'left', 'bottom', 'right'):
        tag = f'w:{edge}'
        el = tcBorders.find(qn(tag))
        if el is None:
            el = OxmlElement(tag)
            tcBorders.append(el)
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), '4')
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), 'auto')


def set_table_borders(table):
    for row in table.rows:
        for cell in row.cells:
            set_cell_border(cell)


def set_cell_bg(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)


def set_cell_vcenter(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    vAlign = OxmlElement('w:vAlign')
    vAlign.set(qn('w:val'), 'center')
    tcPr.append(vAlign)


def add_bookmark(paragraph, name, bookmark_id):
    start = OxmlElement('w:bookmarkStart')
    start.set(qn('w:id'), str(bookmark_id))
    start.set(qn('w:name'), name)
    end = OxmlElement('w:bookmarkEnd')
    end.set(qn('w:id'), str(bookmark_id))
    paragraph._p.insert(0, start)
    paragraph._p.append(end)


def add_internal_hyperlink(paragraph, anchor, text, size=10):
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('w:anchor'), anchor)
    run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    rStyle = OxmlElement('w:rStyle')
    rStyle.set(qn('w:val'), 'Hyperlink')
    rPr.append(rStyle)
    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), str(size * 2))
    rPr.append(sz)
    run.append(rPr)
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = text
    run.append(t)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)


def add_field(paragraph, field_code):
    """Insere um campo de Word (ex.: PAGE, NUMPAGES, TOC)."""
    run = paragraph.add_run()
    fldChar_begin = OxmlElement('w:fldChar')
    fldChar_begin.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = field_code
    fldChar_sep = OxmlElement('w:fldChar')
    fldChar_sep.set(qn('w:fldCharType'), 'separate')
    fldChar_end = OxmlElement('w:fldChar')
    fldChar_end.set(qn('w:fldCharType'), 'end')
    r = run._r
    r.append(fldChar_begin)
    r.append(instrText)
    r.append(fldChar_sep)
    r.append(fldChar_end)
    return run


def add_page_break(doc):
    doc.add_page_break()


def slugify_anchor(text):
    """Gera um slug ASCII a partir do heading, respeitando o limite de nome
    de bookmark do Word (letras/dígitos/underscore, até 40 caracteres)."""
    s = text.strip().lower()
    s = re.sub(r'[`*_]', '', s)
    # normaliza acentos para ASCII simples (bookmarks do Word toleram
    # unicode, mas manter ASCII evita problemas em versões antigas do Word)
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^a-z0-9\s\-]', '', s)
    s = re.sub(r'\s+', '-', s).strip('-')
    if not s or not s[0].isalpha():
        s = f'a{s}'
    return s[:40].rstrip('-') or 'anchor'


# ---------------------------------------------------------------------------
# Estilos do documento
# ---------------------------------------------------------------------------

def setup_styles(doc):
    styles = doc.styles

    normal = styles['Normal']
    normal.font.name = 'Arial'
    normal.font.size = Pt(11)
    normal.font.color.rgb = RGBColor(0, 0, 0)
    normal.paragraph_format.space_after = Pt(8)
    normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    rpr = normal.element.get_or_add_rPr()
    rFonts = rpr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rpr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), 'Arial')

    heading_specs = {
        'Heading 1': (16, True),
        'Heading 2': (14, True),
        'Heading 3': (12, True),
        'Heading 4': (11, True),
        'Heading 5': (11, False),
    }
    for name, (size, bold) in heading_specs.items():
        try:
            st = styles[name]
        except KeyError:
            continue
        st.font.name = 'Arial'
        st.font.size = Pt(size)
        st.font.bold = bold
        st.font.color.rgb = RGBColor(0, 0, 0)
        st.font.italic = False
        st.paragraph_format.space_before = Pt(14)
        st.paragraph_format.space_after = Pt(6)
        st.paragraph_format.keep_with_next = True
        st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    try:
        hl = styles['Hyperlink']
        hl.font.color.rgb = RGBColor(0x05, 0x63, 0xC1)
        hl.font.underline = True
    except KeyError:
        pass

    # Estilo visualmente idêntico ao Heading4, porém sem outlineLvl — usado
    # para subtítulos que se repetem em toda Capacidade ('Bloco/Pilar',
    # 'Resumo Descritivo', 'Questões') e que não devem poluir o campo TOC,
    # que seleciona entradas pelo outline level (\o "1-4").
    if 'Heading4NoTOC' not in styles:
        no_toc = styles.add_style('Heading4NoTOC', WD_STYLE_TYPE.PARAGRAPH)
        no_toc.base_style = styles['Heading 4']
        no_toc.font.name = 'Arial'
        no_toc.font.size = Pt(11)
        no_toc.font.bold = True
        no_toc.font.italic = False
        no_toc.font.color.rgb = RGBColor(0, 0, 0)
        no_toc.paragraph_format.space_before = Pt(14)
        no_toc.paragraph_format.space_after = Pt(6)
        no_toc.paragraph_format.keep_with_next = True
        no_toc.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        # 'basedOn=Heading4' herda outlineLvl=3 do estilo-base; um outlineLvl
        # ausente no filho NÃO sobrescreve o herdado, então é preciso
        # explicitamente definir um valor fora do range do TOC (\o "1-4").
        # w:val="9" equivale a "Corpo de texto" (sem nível de estrutura).
        pPr = no_toc.element.get_or_add_pPr()
        outlineLvl = pPr.find(qn('w:outlineLvl'))
        if outlineLvl is None:
            outlineLvl = OxmlElement('w:outlineLvl')
            pPr.append(outlineLvl)
        outlineLvl.set(qn('w:val'), '9')


# ---------------------------------------------------------------------------
# Cabeçalho / rodapé
# ---------------------------------------------------------------------------

def build_header(section, total_pages_placeholder="465"):
    header = section.header
    header.is_linked_to_previous = False
    for p in list(header.paragraphs):
        p.text = ''

    table = header.add_table(rows=1, cols=4, width=Cm(17))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [Cm(3.2), Cm(8.3), Cm(2.8), Cm(2.7)]
    for col, w in zip(table.columns, widths):
        col.width = w
    row = table.rows[0]
    for cell, w in zip(row.cells, widths):
        cell.width = w
        set_cell_vcenter(cell)

    logo_cell, code_cell, rev_cell, page_cell = row.cells

    add_logo_run(logo_cell.paragraphs[0])

    code_p = code_cell.paragraphs[0]
    code_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = code_p.add_run(DOC_CODE)
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Arial'

    rev_p = rev_cell.paragraphs[0]
    rev_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = rev_p.add_run(DOC_REV)
    run.bold = True
    run.font.size = Pt(10)
    run.font.name = 'Arial'

    page_p = page_cell.paragraphs[0]
    page_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = page_p.add_run('PÁGINA\n')
    run.bold = True
    run.font.size = Pt(10)
    run.font.name = 'Arial'
    page_p2 = page_cell.add_paragraph()
    page_p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_field(page_p2, 'PAGE')
    r = page_p2.add_run('/')
    r.font.size = Pt(10)
    add_field(page_p2, 'NUMPAGES')
    for pp in (page_p, page_p2):
        for r in pp.runs:
            r.font.size = Pt(10)
            r.font.name = 'Arial'

    set_table_borders(table)
    add_header_spacer(header)
    return table


def add_header_spacer(header):
    """Parágrafo em branco após a tabela do cabeçalho, dando 0,5cm de
    respiro entre o cabeçalho e o início do conteúdo da página."""
    spacer = header.add_paragraph()
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.space_after = Cm(0.5)


def set_paragraph_top_border(paragraph, color='000000', sz='4'):
    """Linha fina acima do parágrafo (usada como separador do rodapé)."""
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = pPr.find(qn('w:pBdr'))
    if pBdr is None:
        pBdr = OxmlElement('w:pBdr')
        pPr.append(pBdr)
    top = OxmlElement('w:top')
    top.set(qn('w:val'), 'single')
    top.set(qn('w:sz'), sz)
    top.set(qn('w:space'), '4')
    top.set(qn('w:color'), color)
    pBdr.append(top)


def build_footer(section):
    """Rodapé institucional (modelo MOD-Gabin-039): linha fina + texto de
    codificação em Arial 8 pt, negrito, replicado em todas as páginas
    (F-2 do PLANO). Aplicado tanto na seção da capa quanto na do corpo."""
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.text = ''
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    set_paragraph_top_border(p)
    run = p.add_run(FOOTER_TEXT)
    run.bold = True
    run.font.size = Pt(8)
    run.font.name = 'Arial'


def add_logo_run(paragraph, size_cm=2.6):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if LOGO_PATH.exists():
        run = paragraph.add_run()
        run.add_picture(str(LOGO_PATH), width=Cm(size_cm))
    else:
        run = paragraph.add_run('INMETRO')
        run.bold = True
        run.font.size = Pt(11)


def build_cover_header(section):
    """Cabeçalho da capa: logo + nome da diretoria, sem código/revisão/página
    (diferente do cabeçalho usado nas demais páginas, sumário incluso)."""
    header = section.header
    header.is_linked_to_previous = False
    for p in list(header.paragraphs):
        p.text = ''

    table = header.add_table(rows=1, cols=2, width=Cm(17))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [Cm(3.2), Cm(13.8)]
    for col, w in zip(table.columns, widths):
        col.width = w
    row = table.rows[0]
    for cell, w in zip(row.cells, widths):
        cell.width = w
        set_cell_vcenter(cell)

    logo_cell, text_cell = row.cells
    add_logo_run(logo_cell.paragraphs[0])

    text_p = text_cell.paragraphs[0]
    text_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = text_p.add_run('Instituto Nacional de Metrologia, Qualidade e Tecnologia')
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Arial'

    set_table_borders(table)
    add_header_spacer(header)
    return table


# ---------------------------------------------------------------------------
# Parsing do Markdown
# ---------------------------------------------------------------------------

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$')
TABLE_ROW_RE = re.compile(r'^\|(.+)\|\s*$')
TABLE_SEP_RE = re.compile(r'^\|[\s:|-]+\|\s*$')
BULLET_RE = re.compile(r'^( *)-\s+(.*)$')
DOT_BULLET_RE = re.compile(r'^( *)•\s+(.*)$')
HTML_COMMENT_RE = re.compile(r'<!--.*?-->', re.DOTALL)
ITALIC_LABEL_RE = re.compile(r'^\*(Tabela|Figura|Quadro)\s')

# Headings que devem sempre iniciar em nova página: ANEXO, APÊNDICE, cada
# Dimensão (tanto '### I.N Dimensão: ...' no ANEXO I quanto '#### Dimensão N:
# ...' no APÊNDICE A) e cada Capacidade ('#### I.N.M Capacidade: ...').
PAGE_BREAK_BEFORE_RE = re.compile(
    r'^(ANEXO\b|APÊNDICE\b|(\S+\s+)?Dimensão[\s:]|(\S+\s+)?Capacidade:)',
    re.IGNORECASE,
)

# Primeira Capacidade de cada Dimensão no ANEXO I ('I.N.1 Capacidade: ...') —
# esta NÃO deve forçar quebra de página própria: continua na mesma página em
# que a Dimensão (I.N) abriu.
FIRST_CAPACIDADE_RE = re.compile(r'^I\.\d+\.1\s+Capacidade:', re.IGNORECASE)

# Subtítulos de nível 4 que se repetem em toda Capacidade e não devem
# aparecer no sumário (usam o estilo 'Heading4NoTOC', sem outlineLvl).
NO_TOC_HEADING_TEXTS = {'bloco/pilar', 'resumo descritivo', 'questões', 'glossário'}

# Subtítulos de nível 5 cujas listas (bullets) recebem recuo extra para se
# alinhar mais à direita, conforme padrão do PDF de referência.
INDENTED_BULLET_BLOCK_TEXTS = {
    'artefatos e onde buscar', 'métricas/kpis', 'sinais por nível', 'amostragem',
}
INDENTED_BULLET_EXTRA_CM = 1.0

# ANEXO II: 'Critérios de Entrada:' / 'Critérios de Saída:' são parágrafos
# comuns (não headings) que também abrem um bloco de bullets a recuar.
INDENTED_BULLET_PARAGRAPH_TEXTS = {'critérios de entrada:', 'critérios de saída:'}


def strip_html_comments(text):
    return HTML_COMMENT_RE.sub('', text)


def split_inline_runs(text):
    """Divide uma linha em runs (text, bold, italic) respeitando **bold** e *italic*."""
    runs = []
    pos = 0
    pattern = re.compile(r'(\*\*.+?\*\*|\*[^*\n]+?\*)')
    for m in pattern.finditer(text):
        if m.start() > pos:
            runs.append((text[pos:m.start()], False, False))
        token = m.group(0)
        if token.startswith('**'):
            runs.append((token[2:-2], True, False))
        else:
            runs.append((token[1:-1], False, True))
        pos = m.end()
    if pos < len(text):
        runs.append((text[pos:], False, False))
    if not runs:
        runs = [(text, False, False)]
    return runs


def add_runs(paragraph, text, base_size=11, base_color=None):
    for chunk, bold, italic in split_inline_runs(text):
        if chunk == '':
            continue
        run = paragraph.add_run(chunk)
        run.bold = bold
        run.italic = italic
        run.font.size = Pt(base_size)
        run.font.name = 'Arial'
        if base_color:
            run.font.color.rgb = base_color


def parse_table_row(line):
    inner = line.strip()
    inner = inner[1:-1] if inner.startswith('|') and inner.endswith('|') else inner
    cells = inner.split('|')
    return [c.strip() for c in cells]


class MarkdownDocxBuilder:
    def __init__(self, doc):
        self.doc = doc
        self.bookmark_id = 100
        self.toc_entries = []  # (level, text, anchor)
        self._anchor_counts = {}
        self._current_subsection = None

    def next_bookmark_id(self):
        self.bookmark_id += 1
        return self.bookmark_id

    def unique_anchor(self, text):
        """Bookmarks do Word precisam de nome único no documento inteiro;
        como títulos como 'Bloco/Pilar' ou 'Amostragem' se repetem centenas
        de vezes (uma vez por capacidade/questão), desambigua com sufixo."""
        base = slugify_anchor(text)
        count = self._anchor_counts.get(base, 0)
        self._anchor_counts[base] = count + 1
        return base if count == 0 else f'{base}-{count}'

    # -- heading -------------------------------------------------------
    def add_heading(self, level, text):
        stripped_text = text.strip()
        # Marca o início/fim dos blocos que recebem recuo extra nos bullets
        # ('Artefatos e onde buscar', 'Métricas/KPIs', 'Sinais por nível',
        # 'Amostragem'); qualquer outro heading de nível <= 5 encerra o bloco.
        if stripped_text.lower() in INDENTED_BULLET_BLOCK_TEXTS:
            self._current_subsection = stripped_text.lower()
        else:
            self._current_subsection = None
        is_first_capacidade = bool(FIRST_CAPACIDADE_RE.match(stripped_text))
        if PAGE_BREAK_BEFORE_RE.match(stripped_text) and not is_first_capacidade:
            self.doc.add_page_break()
        excluded_from_toc = stripped_text.lower() in NO_TOC_HEADING_TEXTS
        style_name = 'Heading4NoTOC' if excluded_from_toc else f'Heading {min(level, 5)}'
        p = self.doc.add_paragraph(style=style_name)
        anchor = self.unique_anchor(text)
        add_bookmark(p, anchor, self.next_bookmark_id())
        add_runs(p, text, base_size=11)
        # add_runs força tamanho 11 nos runs — corrige para o tamanho do heading.
        size_map = {1: 16, 2: 14, 3: 12, 4: 11, 5: 11}
        italic5 = (level == 5) and not excluded_from_toc
        for run in p.runs:
            run.font.size = Pt(size_map.get(level, 11))
            run.bold = (level != 5) or excluded_from_toc
            run.italic = italic5 or run.italic
        if not excluded_from_toc:
            self.toc_entries.append((level, text, anchor))
        return p

    # -- paragraph -------------------------------------------------------
    def add_paragraph_text(self, text):
        stripped_text = text.strip()
        was_in_criterios_block = self._current_subsection in INDENTED_BULLET_PARAGRAPH_TEXTS
        # 'Critérios de Entrada:' / 'Critérios de Saída:' (ANEXO II) também
        # abrem um bloco cujos bullets recebem recuo extra; qualquer outro
        # parágrafo comum encerra o bloco (seja de 'Sinais por nível' etc.,
        # seja de Critérios).
        is_criterios_label = stripped_text.lower() in INDENTED_BULLET_PARAGRAPH_TEXTS
        if is_criterios_label:
            self._current_subsection = stripped_text.lower()
        else:
            self._current_subsection = None
        p = self.doc.add_paragraph()
        if is_criterios_label:
            # O próprio rótulo ('Critérios de Entrada:'/'Critérios de
            # Saída:') também recebe o recuo extra, não só seus bullets.
            p.paragraph_format.left_indent = Cm(0.5 + INDENTED_BULLET_EXTRA_CM)
            # Sem espaço abaixo: o rótulo deve colar no primeiro bullet
            # logo em seguida (sem linha em branco entre eles).
            p.paragraph_format.space_after = Pt(0)
        elif was_in_criterios_block:
            # Saindo do bloco de bullets de Critérios de Entrada/Saída: dá
            # respiro antes do próximo texto comum (o parágrafo anterior era
            # um bullet com space_after=2pt, pequeno demais).
            p.paragraph_format.space_before = Pt(8)
        add_runs(p, text, base_size=11)
        return p

    def add_italic_caption(self, text):
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text)
        run.italic = True
        run.font.size = Pt(10)
        run.font.name = 'Arial'
        p.paragraph_format.space_after = Pt(4)
        return p

    def add_bullet(self, text, indent_level):
        # Em 'Sinais por nível', o rótulo 'Nível N:' (indent 0) mantém o
        # marcador de bullet padrão (•); todos os seus sub-itens (indent > 0,
        # a descrição de cada nível) usam hífen em vez do marcador.
        use_dash = self._current_subsection == 'sinais por nível' and indent_level > 0

        base = 0.5 + (INDENTED_BULLET_EXTRA_CM if self._current_subsection else 0)
        indent = Cm(base + 0.6 * indent_level)

        if use_dash:
            p = self.doc.add_paragraph()
            p.paragraph_format.left_indent = indent
            p.paragraph_format.space_after = Pt(2)
            dash_run = p.add_run('-  ')
            dash_run.font.size = Pt(11)
            dash_run.font.name = 'Arial'
            add_runs(p, text, base_size=11)
        else:
            p = self.doc.add_paragraph(style='List Bullet')
            p.paragraph_format.left_indent = indent
            p.paragraph_format.space_after = Pt(2)
            add_runs(p, text, base_size=11)
        return p

    def add_table(self, rows):
        if not rows:
            return None
        ncols = max(len(r) for r in rows)
        rows = [r + [''] * (ncols - len(r)) for r in rows]
        table = self.doc.add_table(rows=len(rows), cols=ncols)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER

        # Tabelas "Respostas" do ANEXO I (Nível | Item de resposta) têm a
        # coluna 'Nível' populada só com dígitos (0-6) — a largura de
        # autofit fica desproporcionalmente larga. Fixa a 1a coluna no
        # tamanho do próprio título e deixa a 2a coluna tomar o restante.
        narrow_first_col = (
            ncols == 2 and rows[0][0].strip().lower() == 'nível'
        )
        if narrow_first_col:
            table.autofit = False
            first_w, second_w = Cm(2.2), Cm(14.3)
            for col, w in zip(table.columns, (first_w, second_w)):
                col.width = w
        else:
            table.autofit = True

        for ridx, row_data in enumerate(rows):
            for cidx, cell_text in enumerate(row_data):
                cell = table.rows[ridx].cells[cidx]
                if narrow_first_col:
                    cell.width = first_w if cidx == 0 else second_w
                cell.paragraphs[0].text = ''
                p = cell.paragraphs[0]
                add_runs(p, cell_text, base_size=10)
                if ridx == 0:
                    for run in p.runs:
                        run.bold = True
                    set_cell_bg(cell, 'F2F2F2')
        set_table_borders(table)
        spacer = self.doc.add_paragraph()
        spacer.paragraph_format.space_after = Pt(6)
        return table


def parse_plain_text_table(lines):
    """Trata a última tabela do arquivo ('Controle de Versões'), que não usa
    sintaxe de pipes e sim colunas separadas por 2+ espaços."""
    rows = []
    for line in lines:
        if not line.strip():
            continue
        cols = re.split(r' {2,}', line.strip())
        rows.append(cols)
    return rows


def convert(md_path, docx_path):
    raw = Path(md_path).read_text(encoding='utf-8')
    raw = strip_html_comments(raw)
    lines = raw.split('\n')

    doc = Document()

    # ---- configuração de página -----------------------------------
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.0)
    section.header_distance = Cm(1.0)
    section.footer_distance = Cm(1.0)

    setup_styles(doc)
    build_cover_header(section)
    build_footer(section)

    builder = MarkdownDocxBuilder(doc)

    # ---- estado do parser -------------------------------------------
    i = 0
    n = len(lines)
    first_h1_done = False
    started_body_section = False
    table_buffer = []
    list_buffer_flush = None

    def flush_table():
        nonlocal table_buffer
        if table_buffer:
            builder.add_table(table_buffer)
            table_buffer = []

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # --- linhas em branco ---
        if stripped == '':
            flush_table()
            i += 1
            continue

        # --- separador horizontal ---
        if re.fullmatch(r'-{3,}', stripped):
            flush_table()
            i += 1
            continue

        # --- tabela markdown (pipes) ---
        if TABLE_ROW_RE.match(line):
            if TABLE_SEP_RE.match(line):
                i += 1
                continue
            table_buffer.append(parse_table_row(line))
            i += 1
            continue
        else:
            flush_table()

        # --- heading ---
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()

            if text.upper() == 'SUMÁRIO':
                # pula o índice manual em markdown: será substituído por um
                # sumário navegável com hyperlinks + campo TOC nativo, inserido
                # logo após a capa.
                i += 1
                # consome as linhas do índice (bullets/links) até o próximo
                # heading ou separador '---'
                while i < n:
                    l2 = lines[i]
                    if HEADING_RE.match(l2) or re.fullmatch(r'-{3,}', l2.strip()):
                        break
                    i += 1
                continue

            if level == 1 and not first_h1_done:
                build_cover_page(doc, text)
                first_h1_done = True
                # consome as linhas de metadados da capa (autoria, código,
                # revisão) já renderizadas por build_cover_page, até o
                # separador '---' que fecha a capa no markdown de origem.
                i += 1
                while i < n and not re.fullmatch(r'-{3,}', lines[i].strip()):
                    i += 1
                if i < n:
                    i += 1  # pula o '---'
                # a partir do sumário (inclusive) as páginas usam o cabeçalho
                # com logo/código/revisão/página — só a capa usa o cabeçalho
                # reduzido (logo + nome da diretoria).
                new_section = doc.add_section(WD_SECTION.NEW_PAGE)
                new_section.page_width = section.page_width
                new_section.page_height = section.page_height
                new_section.top_margin = section.top_margin
                new_section.bottom_margin = section.bottom_margin
                new_section.left_margin = section.left_margin
                new_section.right_margin = section.right_margin
                new_section.header_distance = section.header_distance
                new_section.footer_distance = section.footer_distance
                build_header(new_section)
                build_footer(new_section)
                started_body_section = True
                insert_toc_placeholder(doc, builder)
                add_page_break(doc)
                i += 1
                continue

            builder.add_heading(level, text)
            i += 1
            continue

        # --- legenda em itálico (Tabela N. / Figura N. / Quadro N.) ---
        if ITALIC_LABEL_RE.match(stripped) and stripped.endswith('*'):
            builder.add_italic_caption(stripped.strip('*'))
            i += 1
            continue

        # --- bullets com '-' ---
        m = BULLET_RE.match(line)
        if m:
            indent = len(m.group(1)) // 2
            builder.add_bullet(m.group(2), indent)
            i += 1
            continue

        # --- bullets com '•' ---
        m = DOT_BULLET_RE.match(line)
        if m:
            indent = len(m.group(1)) // 2
            builder.add_bullet(m.group(2), indent)
            i += 1
            continue

        # --- "Controle de Versões" tabela de texto plano (fim do arquivo) ---
        if re.match(r'^Vers[aã]o\s{2,}Data', stripped):
            plain_rows = [stripped]
            j = i + 1
            while j < n and lines[j].strip():
                plain_rows.append(lines[j].strip())
                j += 1
            rows = parse_plain_text_table(plain_rows)
            builder.add_table(rows)
            i = j
            continue

        # --- parágrafo comum ---
        # Em trechos transcritos via pdftotext -layout (ex.: ANEXO II), uma
        # mesma frase pode estar quebrada em várias linhas consecutivas sem
        # linha em branco entre elas. Junta essas linhas num único parágrafo
        # até encontrar uma linha em branco ou outro tipo de elemento
        # (heading, bullet, tabela, separador).
        para_lines = [stripped]
        i += 1
        while i < n:
            nxt = lines[i]
            nxt_stripped = nxt.strip()
            if nxt_stripped == '':
                break
            if HEADING_RE.match(nxt):
                break
            if TABLE_ROW_RE.match(nxt):
                break
            if re.fullmatch(r'-{3,}', nxt_stripped):
                break
            if BULLET_RE.match(nxt) or DOT_BULLET_RE.match(nxt):
                break
            if ITALIC_LABEL_RE.match(nxt_stripped) and nxt_stripped.endswith('*'):
                break
            if re.match(r'^Vers[aã]o\s{2,}Data', nxt_stripped):
                break
            para_lines.append(nxt_stripped)
            i += 1
        builder.add_paragraph_text(' '.join(para_lines))

    flush_table()

    doc.save(docx_path)
    return builder


def build_cover_page(doc, title_text):
    p0 = doc.add_paragraph()
    p0.paragraph_format.space_after = Pt(60)

    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p1.add_run(title_text)
    run.font.size = Pt(18)
    run.font.name = 'Arial'
    p1.paragraph_format.space_after = Pt(30)

    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p2.add_run('Diretoria de Metrologia Científica e Industrial')
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Arial'
    p2.paragraph_format.space_after = Pt(16)

    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p3.add_run('Documento de caráter orientativo')
    run.font.size = Pt(12)
    run.font.name = 'Arial'
    p3.paragraph_format.space_after = Pt(60)

    p4 = doc.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p4.add_run(DOC_CODE)
    run.bold = True
    run.font.size = Pt(20)
    run.font.name = 'Arial'
    p4.paragraph_format.space_after = Pt(6)

    p5 = doc.add_paragraph()
    p5.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p5.add_run('Revisão 01 – Junho/2026')
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Arial'


def insert_toc_placeholder(doc, builder):
    p = doc.add_paragraph(style='Heading 2')
    run = p.add_run('SUMÁRIO')
    run.font.size = Pt(14)
    run.bold = True
    run.font.name = 'Arial'
    p.paragraph_format.space_after = Pt(10)

    field_p = doc.add_paragraph()
    add_field(field_p, 'TOC \\o "1-4" \\h \\z \\u')
    note_p = doc.add_paragraph()
    note_run = note_p.add_run(
        '(Clique com o botão direito no sumário acima e escolha '
        '"Atualizar campo" para carregar os números de página após abrir o documento no Word.)'
    )
    note_run.italic = True
    note_run.font.size = Pt(9)
    note_run.font.color.rgb = RGBColor(0x60, 0x60, 0x60)


def main():
    parser = argparse.ArgumentParser(description='Converte markdown DOQ-Inmetro para DOCX.')
    parser.add_argument('input', help='Arquivo markdown de entrada')
    parser.add_argument('-o', '--output', help='Arquivo .docx de saída')
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        log.error('Arquivo não encontrado: %s', input_path)
        sys.exit(1)

    output_path = Path(args.output) if args.output else input_path.with_suffix('.docx')

    log.info('Convertendo %s -> %s', input_path, output_path)
    convert(str(input_path), str(output_path))
    log.info('Concluído: %s', output_path)


if __name__ == '__main__':
    main()
