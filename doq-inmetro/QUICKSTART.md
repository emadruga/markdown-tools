# doq-inmetro — Quick Start

Conversor de Markdown para `.docx` no padrão institucional Inmetro, cobrindo os dois
formatos de documento normativo:

- **DOQ** (Documento Orientativo da Qualidade) — modelo [MOD-Gabin-39](normas/MOD-Gabin-39_02.docx)
- **NIT** (Norma Inmetro Técnica) — modelo [MOD-Gabin-40](normas/MOD-Gabin-40_02.doc)

As diferenças entre os dois modelos estão detalhadas em
[docs/MOD39_MOD40_DIFERENCAS.md](docs/MOD39_MOD40_DIFERENCAS.md). Em resumo: o corpo do documento
(fonte, margens, cabeçalho/rodapé de página, tabelas, listas) é idêntico — a única
diferença real é que o **DOQ tem página de capa** antes do sumário e a **NIT não tem**
(o sumário já é a primeira página).

## Pré-requisitos

```bash
cd /Users/emadruga/proj/markdown-tools
source venv/bin/activate   # ou: conda activate MARKDOWN_TOOLS
pip install -r requirements.txt
```

O script usa `inmetro-logo.png` (já presente nesta pasta) para o logo do cabeçalho.

## Comando básico

```bash
python markdown2inmetro_docx.py <input.md> [-o output.docx] [--format {doq,nit}]
```

| Opção | Obrigatório | Default | Descrição |
|---|---|---|---|
| `input` | sim | — | Arquivo markdown de entrada |
| `-o`, `--output` | não | `<input>.docx` (mesmo nome, extensão trocada) | Caminho do `.docx` de saída |
| `--format` | não | **`doq`** | `doq` (com capa) ou `nit` (sem capa) |

> Se `--format` não for informado, o script assume **`doq`** — o comportamento
> histórico do script, preservado para não quebrar scripts/pipelines existentes.

## Gerar um DOQ

```bash
python markdown2inmetro_docx.py testes/doq/DOQ-DIMCI-020_jun2026-Final.md \
  -o testes/doq/DOQ-DIMCI-020_jun2026-Final.docx \
  --format doq
```

Equivalente (formato é o default, pode ser omitido):

```bash
python markdown2inmetro_docx.py testes/doq/DOQ-DIMCI-020_jun2026-Final.md
```

### Markdown mínimo para um DOQ

O script exige, nesta ordem, no início do arquivo:

1. Um heading `# <Título do documento>` (H1) — vira a capa.
2. Linhas de metadados da capa logo abaixo do H1 (autoria, "Documento de caráter
   orientativo", código do documento, revisão) — são apenas texto normal, pois
   `build_cover_page()` já desenha o layout fixo da capa; essas linhas são
   **consumidas e descartadas** pelo parser (servem só de referência legível no
   `.md`, não são renderizadas literalmente).
3. Um separador `---` fechando o bloco de capa.
4. Um heading `## SUMÁRIO` — seu conteúdo (bullets/links) também é descartado; é
   substituído por um sumário navegável com campo `TOC` nativo do Word.
5. Um separador `---` fechando o bloco de sumário.
6. O corpo do documento, com headings `##`, `###` etc. numerados manualmente no
   próprio texto (ex.: `## 1 OBJETIVO`), parágrafos, tabelas (`|...|`) e listas
   (`- item`, `• item`, `● item`).

Exemplo mínimo:

```markdown
# ORIENTAÇÃO PARA AVALIAÇÃO DE MATURIDADE DE INDÚSTRIAS 4.0

**Diretoria de Metrologia Científica e Industrial**

Documento de caráter orientativo

**DOQ-DIMCI-020**
Revisão 01 – Junho/2026

---

## SUMÁRIO

- [1 OBJETIVO](#1-objetivo)
- [2 CAMPO DE APLICAÇÃO](#2-campo-de-aplicação)

---

## 1 OBJETIVO

Texto do objetivo.

## 2 CAMPO DE APLICAÇÃO

Texto do campo de aplicação.
```

## Gerar uma NIT

```bash
python markdown2inmetro_docx.py testes/nit/NIT-LAINF-009_jun2026.md \
  -o testes/nit/NIT-LAINF-009_jun2026.docx \
  --format nit
```

`--format nit` é **obrigatório** para gerar uma NIT — sem ele, o script monta a capa
estilo DOQ mesmo que o markdown não tenha um H1 real no início.

### Markdown mínimo para uma NIT

Não há página de capa, então o H1 inicial é opcional:

- **Sem H1**: o arquivo pode começar direto em `## SUMÁRIO`. É o jeito recomendado,
  já que a NIT não tem capa — menos conteúdo para manter sincronizado.
- **Com H1**: se o markdown trouxer um H1 antes do sumário (por reaproveitar a
  mesma transcrição de origem de um DOQ, por exemplo), ele é apenas **descartado**
  junto com as linhas de metadados até o próximo `---` — não aparece no `.docx`
  gerado, pois a identificação do documento já está na coluna CODIFICAÇÃO do
  cabeçalho de página.

Depois do (opcional) H1/capa, a estrutura é igual à do DOQ:

1. Heading `## SUMÁRIO` (conteúdo descartado, substituído pelo `TOC` nativo).
2. Separador `---`.
3. Corpo do documento (headings numerados, parágrafos, tabelas, listas).

Exemplo mínimo (sem H1):

```markdown
## SUMÁRIO

- [1 OBJETIVO](#1-objetivo)
- [2 CAMPO DE APLICAÇÃO](#2-campo-de-aplicação)

---

## 1 OBJETIVO

Texto do objetivo.

## 2 CAMPO DE APLICAÇÃO

Texto do campo de aplicação.
```

## Controlando o nível de log

```bash
LOGLEVEL=DEBUG python markdown2inmetro_docx.py input.md --format nit
LOGLEVEL=WARNING python markdown2inmetro_docx.py input.md --format doq
```

Variável de ambiente `LOGLEVEL` (default `INFO`), igual aos demais scripts do
repositório — ver [../QUICKSTART.md](../QUICKSTART.md#4-controlling-log-verbosity).
