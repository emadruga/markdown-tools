# PROJECT_REQUIREMENTS_BEAUTIFY_DOCX

Especificação visual para conversão Markdown → DOCX dos laboratórios de Segurança Defensiva 2026-1.
Documento de referência: `docs/Cap1 e Cap 2/Lab1_e_Lab2.docx`.

---

## 1. Configuração de Página

| Propriedade | Valor |
|-------------|-------|
| Tamanho | A4 |
| Margem superior | 2,0 cm |
| Margem inferior | 2,0 cm |
| Margem esquerda | 2,5 cm |
| Margem direita | 2,5 cm |

---

## 2. Fontes

| Uso | Fonte | Tamanho | Observações |
|-----|-------|---------|-------------|
| Corpo de texto (Normal) | Arial | 11 pt | Espaçamento padrão do documento |
| Blocos de código / comandos | Courier New | 9 pt | Fundo `#F4F4F4`, sem bordas laterais |
| Inline code (backtick) | Courier New | 10 pt | Mesmo tamanho do corpo circundante, sem fundo |

---

## 3. Hierarquia de Headings

| Nível Markdown | Estilo Word | Tamanho | Cor | Bold | Espaçamento |
|----------------|-------------|---------|-----|------|-------------|
| `#` (título do documento) | Personalizado (não Heading1) | 20 pt | `#1F4E79` | Sim | Centralizado, `space_after=400` |
| `##` (capítulo / lab) | Heading1 | 18 pt | `#1F4E79` | Sim | `space_before=320, space_after=160` |
| `###` (seções: Passo a Passo, Troubleshooting, etc.) | Heading2 | 13 pt | `#1F4E79` | Sim | `space_before=240, space_after=120` |
| `####` (etapas: ETAPA 1, ETAPA 2...) | Heading3 | 12 pt | `#1F4D78` | Não | — |
| Heading4 (sub-etapas, se houver) | Heading4 | 11 pt | `#2E74B5` | Não | Itálico |

---

## 4. Paleta de Cores

### 4.1 Cores de texto

| ID | Hex | Uso |
|----|-----|-----|
| `text-primary` | `#1F4E79` | Títulos de capítulo, headings H1/H2 |
| `text-heading3` | `#1F4D78` | Heading3 (etapas) |
| `text-accent` | `#2E74B5` | Heading4/H5, subtítulos, bordas de separador |
| `text-body` | `#000000` | Corpo de texto normal |
| `text-note` | `#444444` | Texto de instruções em itálico, notas |
| `text-muted` | `#888888` | Placeholders de imagem |
| `text-placeholder` | `#BBBBBB` | Labels "Resposta (até 4 linhas):" |
| `text-subtitle` | `#595959` | Subtítulo na página de rosto |
| `text-white` | `#FFFFFF` | Texto sobre fundos escuros (badges, headers) |

### 4.2 Cores de fundo (shading/fill)

| ID | Hex | Uso |
|----|-----|-----|
| `bg-header-dark` | `#1F4E79` | Cabeçalho de tabela escuro (capítulos) |
| `bg-header-medium` | `#2E74B5` | Cabeçalho de seção |
| `bg-header-light` | `#DAEAF7` | Cabeçalho de tabela claro (sumário, metadados) |
| `bg-code` | `#F4F4F4` | Fundo de blocos de código |
| `bg-table-alt` | `#F9F9F9` | Linha alternada em tabelas longas |
| `bg-info` | `#E3F2FD` | Caixa de informação / nota |
| `bg-tip` | `#E0F2F1` | Caixa de dica (com borda esquerda teal) |
| `bg-warning` | `#FFF2CC` | Caixa de atenção (> **Atenção:**) |
| `bg-danger` | `#FCE4E4` | Caixa de alerta/erro |
| `bg-answer` | `#FAFAFA` | Área de resposta das perguntas de fixação |
| `bg-placeholder` | `#F0F0F0` | Placeholders de screenshot |
| `bg-checkid` | `#1F3864` | Célula de check_id (texto branco) |
| `bg-checkdesc` | `#EBF3FB` | Célula de descrição do check_id |

### 4.3 Badges de nível de dificuldade

| Nível | Emoji MD | Fundo | Texto |
|-------|----------|-------|-------|
| Iniciante | `🟢` | `#1E7A1E` | `#FFFFFF` (branco) |
| Intermediário | `🟡` | `#C45911` | `#FFFFFF` |
| Avançado | `🔴` | `#C00000` | `#FFFFFF` |

Implementação: célula inline (tabela 1×1 compacta) ou run com shading, bold, 9 pt.

### 4.4 Bordas e separadores

| Elemento | Tipo | Espessura (`w:sz`) | Cor | Posição |
|----------|------|---------------------|-----|---------|
| Separador de capítulo | `single` | `6` | `#1F3864` | `bottom` |
| Separador de seção | `single` | `6` | `#2E74B5` | `bottom` |
| Borda de caixa tip/dica | `single` | `6` | `#00695C` | `left` |
| Bordas de tabela (padrão) | `single` | `4` | `auto` | Todas (top, bottom, left, right, insideH, insideV) |

---

## 5. Componentes Visuais

### 5.1 Página de Título

Estrutura (de cima para baixo):
1. Parágrafo vazio (`space_after=400`)
2. Título principal — centralizado, bold, 20 pt, `#1F4E79`
3. Referência ao livro — centralizado, itálico, 14 pt, `#595959`
4. Autor / edição — centralizado, 12 pt, `#595959`
5. Lista dos labs — centralizado, bold, 12 pt, `#1F4E79`
6. Instituição — centralizado, `#595959`
7. Separador horizontal — `border-bottom: single 6 #1F3864`
8. Quebra de página

### 5.2 Sumário com Hyperlinks

- Fundo do bloco de sumário: `#DAEAF7`
- Cada item é um hyperlink interno (`w:hyperlink w:anchor="..."`)
- Bookmarks nos destinos: `cap3`, `lab31`, `lab32`, ..., `apendice_a`
- IDs de bookmark: iniciar em 100 para não colidir com o Word
- Formato dos itens: inclui emoji de nível + título do lab
- Separação visual entre capítulos

### 5.3 Tabela de Metadados do Lab

Tabela 6 linhas × 2 colunas (Objetivo, Capítulo, Nível, Duração, Pré-req., Recursos):

| Coluna | Largura | Fundo | Fonte |
|--------|---------|-------|-------|
| Labels (col 1) | 5 cm | `#D6E4F7` (`bg-header-light`) | Bold, 10 pt |
| Valores (col 2) | 11 cm | `#FFFFFF` | Normal, 10 pt |

A célula de **Nível** na coluna de valor deve conter o badge colorido correspondente.

### 5.4 Blocos de Código (```bash...```)

| Propriedade | Valor |
|-------------|-------|
| Fonte | Courier New |
| Tamanho | 9 pt |
| Fundo | `#F4F4F4` (`bg-code`) |
| Bordas | Nenhuma (apenas shading) |
| Espaçamento | `space_before=6pt, space_after=6pt` |
| Recuo | `left_indent=1cm` |

Cada linha do bloco é um parágrafo separado com o mesmo estilo. Linhas começando com `#` (comentários bash) podem ter cor `#888888` para diferenciação visual.

### 5.5 Caixas de Callout (blockquotes `>`)

Mapeamento do Markdown para o tipo de caixa:

| Padrão no texto | Tipo | Fundo | Borda esquerda |
|-----------------|------|-------|----------------|
| `> **Atenção:**` | Warning | `#FFF2CC` | — |
| `> **Importante:**` | Warning | `#FFF2CC` | — |
| `> **Nota:**` ou `> **Nota sobre`... | Info | `#E3F2FD` | — |
| `> **Regra prática:**` | Tip | `#E0F2F1` | `#00695C` (left, sz=6) |
| `> **Dica:**` | Tip | `#E0F2F1` | `#00695C` (left, sz=6) |
| Outros blockquotes genéricos | Info | `#E3F2FD` | — |

Implementação: parágrafo com shading no fundo e opcionalmente borda esquerda. Texto em 10 pt, cor `#444444`.

### 5.6 Tabelas de Conteúdo (genéricas)

| Elemento | Estilo |
|----------|--------|
| Linha de cabeçalho | Fundo `#DAEAF7`, bold, 10 pt |
| Linhas de dados | Fundo branco, normal, 10 pt |
| Linhas alternadas (se >5 linhas) | Fundo `#F9F9F9` |
| Bordas | `single, sz=4, color=auto` em todas as direções |

### 5.7 Tabela de Troubleshooting

Tabela com 2 colunas: **Problema** | **Solução**.

| Elemento | Estilo |
|----------|--------|
| Header | Fundo `#FCE4E4` (`bg-danger`), bold, 10 pt |
| Coluna Problema | Largura ~6 cm, normal, 10 pt |
| Coluna Solução | Largura ~10 cm, normal, 10 pt |
| Linhas alternadas | Fundo `#F9F9F9` |

### 5.8 Tabela de Critérios de Avaliação

Tabela com 2 colunas: **Critério** | **Pontos**.

| Elemento | Estilo |
|----------|--------|
| Header | Fundo `#DAEAF7`, bold, 10 pt |
| Linha TOTAL | Bold, fundo `#DAEAF7` |
| Referências a `(check ...)` | Courier New, 9 pt, dentro do texto normal |

### 5.9 Checklist de Entrega

Lista com marcadores `- [ ]`:

| Propriedade | Valor |
|-------------|-------|
| Estilo Word | List Bullet |
| Prefixo | `[ ]  ` (checkbox manual) |
| Fonte | 10 pt |
| Espaçamento | `space_before=2pt, space_after=2pt` |
| Referências a `(check ...)` | Courier New, 9 pt |

### 5.10 Perguntas de Fixação

Cada pergunta:
1. **Enunciado**: bold, 10 pt, `space_before=8pt, space_after=2pt`
   - Formato: `N. Texto da pergunta`
   - Perguntas com `(Desafio)` podem ter o prefixo em cor `#C45911`
2. **Área de resposta**: tabela 1×1
   - Fundo: `#FAFAFA`
   - Primeira linha: `Resposta (até 4 linhas):` — itálico, 9 pt, `#BBBBBB`
   - 3 parágrafos vazios adicionais
   - Bordas: `single, sz=4, color=AAAAAA`

### 5.11 Tabela de Check_IDs (Seção C dos templates de relatório)

Tabela 1 linha × 2 colunas por check:

| Célula | Largura | Fundo | Texto |
|--------|---------|-------|-------|
| ID (esquerda) | 4 cm | `#1F3864` (`bg-checkid`) | `check_<id>` — branco, bold, 9 pt, centralizado |
| Descrição (direita) | 12 cm | `#EBF3FB` (`bg-checkdesc`) | `Comando:` bold 9pt + texto / `Esperado:` bold 9pt + texto |

### 5.12 Placeholders de Imagem

Tabela 1×1:

| Propriedade | Valor |
|-------------|-------|
| Fundo | `#F0F0F0` |
| Largura | 6 inches |
| Texto | `[ LABEL ]` — centralizado, itálico, 10 pt, `#888888` |
| Espaçamento interno | `space_before=18pt, space_after=18pt` |

---

## 6. Mapeamento Markdown → Componente DOCX

| Elemento Markdown | Componente DOCX |
|-------------------|-----------------|
| `# Título` | Página de título (Seção 5.1) |
| `## Capítulo N —` | Heading1 + bookmark `capN` + separador |
| `## 🟢 LAB N.M —` / `🟡` / `🔴` | Heading1 + badge de nível + bookmark `labNM` |
| `### Passo a Passo` | Heading2 |
| `### Troubleshooting` | Heading2 + tabela estilo 5.7 |
| `### Critérios de Avaliação` | Heading2 + tabela estilo 5.8 |
| `### ✔ Checklist de Entrega` | Heading2 + lista estilo 5.9 |
| `### Perguntas de Fixação` | Heading2 + pares pergunta/resposta estilo 5.10 |
| `#### ETAPA N —` | Heading3 |
| `` ```bash ... ``` `` | Bloco de código estilo 5.4 |
| `> **Atenção:**` | Caixa warning estilo 5.5 |
| `> **Nota:**` / `>` genérico | Caixa info estilo 5.5 |
| `> **Regra prática:**` | Caixa tip estilo 5.5 |
| Tabela com `\| ... \|` | Tabela genérica estilo 5.6 |
| `- [ ] item (check ...)` | Checklist estilo 5.9 |
| `**N. Pergunta?**` | Pergunta de fixação estilo 5.10 |
| `---` | Separador `border-bottom` (Seção 4.4) |
| `## Apêndice A` | Heading1 + bookmark `apendice_a` |

---

## 7. Bookmarks e Hyperlinks

### 7.1 Convenção de nomes

| Elemento | Bookmark |
|----------|----------|
| Capítulo N | `capN` (ex: `cap3`, `cap4`) |
| LAB N.M | `labNM` (ex: `lab31`, `lab42`) |
| Apêndice A | `apendice_a` |

### 7.2 IDs de bookmark

Iniciar em `100` para evitar colisão com bookmarks internos do Word.

### 7.3 Sumário

Cada item do sumário é um `w:hyperlink` com `w:anchor="<bookmark>"`. O texto inclui o emoji de nível e o título do lab.

---

## 8. Rodapé

| Propriedade | Valor |
|-------------|-------|
| Conteúdo | `Segurança Defensiva 2026-1 — Laboratórios Capítulos N e M` (esquerda) + número da página (direita) |
| Fonte | Arial, 9 pt, `#888888` |
| Separador | Linha fina acima do rodapé |

Dois rodapés distintos: primeiro (página de título, sem número) e default (demais páginas).

---

## 9. Helpers Python-docx Reutilizáveis

Funções auxiliares necessárias (referência: `docs/Lab1.2/gerar_relatorio_lab12.py`):

```python
def set_cell_bg(cell, hex_color: str)
    # Aplica w:shd fill à célula

def add_border_to_table(table, color='AAAAAA', sz='4')
    # Aplica bordas em todas as direções

def para_bold(cell, text, size=11, color=None, align=LEFT)
    # Parágrafo bold no primeiro paragraph da célula

def para_normal(cell, text, size=10, italic=False, color=None)
    # Parágrafo normal no primeiro paragraph da célula

def add_section_heading(doc, number, title, color_hex='1F4E79')
    # Heading numerado com cor e espaçamento

def add_placeholder_img(doc, label)
    # Caixa cinza para screenshot

def add_code_block(doc, lines: list[str])
    # Bloco com fundo #F4F4F4, Courier New 9pt

def add_callout_box(doc, text, box_type='info')
    # Caixa colorida: info/tip/warning/danger

def add_badge(paragraph, level: str)
    # Run inline com fundo colorido e texto branco

def add_bookmark(paragraph, name: str, bookmark_id: int)
    # Insere w:bookmarkStart + w:bookmarkEnd

def add_hyperlink(paragraph, anchor: str, text: str)
    # Insere w:hyperlink com w:anchor interno
```

---

## 10. Documento de Referência Extraído

Arquivo original analisado: `docs/Cap1 e Cap 2/Lab1_e_Lab2.docx`

### Propriedades do documento original

| Propriedade | Valor |
|-------------|-------|
| Criador | python-docx + lxml |
| Fonte padrão (docDefaults) | Arial, 22 half-points (11 pt) |
| Tema | Aptos / Aptos Display (Office default) |
| Estilo de hyperlink | `#0563C1` (azul padrão Office) |

### Estilos nomeados usados

| styleId | Nome | Tamanho | Cor | Bold | Itálico |
|---------|------|---------|-----|------|---------|
| `Normal` | Normal | 11 pt | preto | — | — |
| `Heading1` | heading 1 | 18 pt | `#1F4E79` | Sim | — |
| `Heading2` | heading 2 | 13 pt | `#1F4E79` | Sim | — |
| `Heading3` | heading 3 | 12 pt | `#1F4D78` | — | — |
| `Heading4` | heading 4 | 11 pt | `#2E74B5` | — | Sim |
| `Heading5` | heading 5 | 11 pt | `#2E74B5` | — | — |
| `ListParagraph` | List Paragraph | 11 pt | — | — | — |
| `Hyperlink` | Hyperlink | — | `#0563C1` | — | — |
| `FootnoteText` | footnote text | 10 pt | — | — | — |
