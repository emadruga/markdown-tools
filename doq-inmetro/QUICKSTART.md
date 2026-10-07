# doq-inmetro — Quick Start

Conversor de Markdown para `.docx` no padrão institucional Inmetro, cobrindo os dois
formatos de documento normativo:

- **DOQ** (Documento Orientativo da Qualidade) — modelo [MOD-Gabin-39](normas/MOD-Gabin-39_02.docx)
- **NIT** (Norma Inmetro Técnica) — modelo [MOD-Gabin-40](normas/MOD-Gabin-40_02.doc)

As diferenças entre os dois modelos estão detalhadas em
[docs/MOD39_MOD40_DIFERENCAS.md](docs/MOD39_MOD40_DIFERENCAS.md). Em resumo: o corpo do
documento (fonte, margens, tabelas, listas) é idêntico — as diferenças reais são:

- O **DOQ tem página de capa** antes do sumário; a **NIT não tem** (o sumário já é a
  primeira página).
- A **1ª página da NIT** usa um cabeçalho próprio de 2 linhas × 4 colunas (título,
  norma/código, revisão, data de publicação, página) — diferente do cabeçalho padrão
  de 1 linha usado pelo DOQ (a partir da 2ª página) e pela própria NIT a partir da sua
  2ª página.

## Pré-requisitos

```bash
cd /Users/emadruga/proj/markdown-tools
source venv/bin/activate   # ou: conda activate MARKDOWN_TOOLS
pip install -r requirements.txt
```

O script usa `inmetro-logo.png` (já presente nesta pasta) para o logo do cabeçalho.

## Comando básico

```bash
python markdown2inmetro_docx.py <input.md> [-o output.docx] [--format {doq,nit}] \
  [--doc-code CÓDIGO] [--doc-rev REVISÃO] [--doc-title TÍTULO] [--doc-date MÊS/ANO] \
  [--doc-toc-levels N]
```

| Opção | Obrigatório | Default | Descrição |
|---|---|---|---|
| `input` | sim | — | Arquivo markdown de entrada |
| `-o`, `--output` | não | `<input>.docx` (mesmo nome, extensão trocada) | Caminho do `.docx` de saída |
| `--format` | não | **`doq`** | `doq` (com capa) ou `nit` (sem capa) |
| `--doc-code` | não | `DOQ-DIMCI-020` | Código exibido no cabeçalho (coluna CODIFICAÇÃO no DOQ; NORMA Nº / CODIFICAÇÃO na 1ª página da NIT) e na capa, se `--format doq` |
| `--doc-rev` | não | `01` | **Só o número da revisão** (ex. `00`, `02`) — o rótulo "REV." já é fixo no layout, numa linha acima do valor |
| `--doc-title` | não | H1 do markdown, se houver; senão `TÍTULO` | **Só usado em `--format nit`** — título exibido no cabeçalho da 1ª página. No DOQ o título vem sempre do H1 da capa |
| `--doc-date` | não | `MÊS/ANO` | **Só usado em `--format nit`** — mês/ano de publicação exibido no cabeçalho da 1ª página (coluna PUBLICADO EM). Não aparece no cabeçalho do DOQ |
| `--doc-toc-levels` | não | `4` | Quantos níveis de heading (1 a 5) entram no sumário (campo `TOC \o "1-N"` do Word) — `1` inclui só headings de nível 1, `5` inclui até o nível mais profundo suportado |

> Se `--format` não for informado, o script assume **`doq`** — o comportamento
> histórico do script, preservado para não quebrar scripts/pipelines existentes.
>
> `--doc-code`/`--doc-rev` sempre devem ser definidos (via CLI ou front matter,
> ver abaixo) ao gerar um documento que não seja o DOQ-DIMCI-020 — o default
> reflete apenas o primeiro documento que o script converteu; sem eles, o
> cabeçalho de qualquer outro DOQ ou NIT sai com a identificação errada. Em
> `--format nit`, `--doc-date` também deve ser sempre informado (não tem como
> ser inferido do markdown); `--doc-title` pode ser omitido se o markdown já
> tiver um H1 com o título antes do `## SUMÁRIO`.

### Definindo os dados do documento via front matter (alternativa às flags)

Em vez de repetir `--doc-code`/`--doc-rev`/`--doc-date`/`--doc-title` toda vez que
converter o mesmo arquivo, esses valores podem morar no próprio markdown, num bloco de
front matter no topo do arquivo (antes de qualquer outra linha, inclusive comentários
HTML):

```markdown
---
doc-code: NIT-LAINF-009
doc-rev: "00"
doc-date: Jun/2026
doc-title: AVALIAÇÃO DE MATURIDADE DE INDÚSTRIAS 4.0
doc-toc-levels: "3"
---

## SUMÁRIO
...
```

Com isso, o comando de conversão fica só:

```bash
python markdown2inmetro_docx.py testes/nit/NIT-LAINF-009_jun2026.md --format nit
```

Regras:

- **Chaves aceitas**: `doc-code`, `doc-rev`, `doc-date`, `doc-title`, `doc-toc-levels` —
  qualquer outra linha `chave: valor` no bloco é ignorada (reservado para uso futuro).
  `doc-toc-levels` precisa ser um número inteiro entre `1` e `5` (como texto ou não —
  `"3"` e `3` são equivalentes); um valor fora desse intervalo ou não numérico interrompe
  a conversão com erro.
- **Prioridade**: se a mesma flag for passada via CLI *e* existir no front matter, a
  CLI vence. Isso permite, por exemplo, usar o front matter como valor padrão do
  arquivo e sobrescrever pontualmente (ex. uma revisão diferente) sem editar o `.md`.
  Log mostra qual front matter foi lido (`Front matter do markdown: {...}`) a cada
  conversão, para conferência.
- **Delimitação**: o bloco precisa começar na 1ª linha do arquivo com `---` sozinho
  numa linha, e terminar com outro `---` sozinho numa linha. Um `---` usado como
  separador de seção mais abaixo no arquivo (como o que fecha o SUMÁRIO) não é afetado
  — só a 1ª ocorrência, logo no início do arquivo, conta como front matter.
- **Sintaxe**: só pares simples `chave: valor` (sem aninhamento, listas ou blocos) —
  aspas simples ou duplas ao redor do valor são opcionais e removidas automaticamente.
- Funciona tanto em `--format doq` quanto em `--format nit` — no DOQ, `doc-title` e
  `doc-date` do front matter são ignorados (o título vem do H1 da capa; o DOQ não exibe
  data de publicação no cabeçalho), mas `doc-code`/`doc-rev` valem normalmente.

## Gerar um DOQ

```bash
python markdown2inmetro_docx.py testes/doq/DOQ-DIMCI-020_jun2026-Final.md \
  -o testes/doq/DOQ-DIMCI-020_jun2026-Final.docx \
  --format doq --doc-code DOQ-DIMCI-020 --doc-rev "01"
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

O fixture [testes/nit/NIT-LAINF-009_jun2026.md](testes/nit/NIT-LAINF-009_jun2026.md) já
traz `doc-code`/`doc-rev`/`doc-date`/`doc-title` no front matter (ver seção acima), então
o comando fica simples:

```bash
python markdown2inmetro_docx.py testes/nit/NIT-LAINF-009_jun2026.md \
  -o testes/nit/NIT-LAINF-009_jun2026.docx \
  --format nit
```

Equivalente, se o markdown **não** tivesse front matter — tudo via flags:

```bash
python markdown2inmetro_docx.py testes/nit/NIT-LAINF-009_jun2026.md \
  -o testes/nit/NIT-LAINF-009_jun2026.docx \
  --format nit --doc-code NIT-LAINF-009 --doc-rev "00" \
  --doc-date "Jun/2026" --doc-title "AVALIAÇÃO DE MATURIDADE DE INDÚSTRIAS 4.0"
```

`--format nit` é **obrigatório** para gerar uma NIT — sem ele, o script monta a capa
estilo DOQ mesmo que o markdown não tenha um H1 real no início. `doc-code`/`doc-rev`/
`doc-date` também são essenciais aqui (via CLI ou front matter): sem eles o cabeçalho
sai com os defaults (`DOQ-DIMCI-020` / `01` / `MÊS/ANO`), que não fazem sentido
numa NIT. `doc-title` pode ser omitido se o markdown tiver um H1 antes do
`## SUMÁRIO` — nesse caso o título do cabeçalho vem automaticamente desse H1.

A 1ª página do `.docx` gerado usa um cabeçalho de 2 linhas × 4 colunas (TÍTULO | NORMA
Nº/CODIFICAÇÃO + REV. Nº | PUBLICADO EM + PÁGINA) — diferente do cabeçalho padrão de 1
linha usado a partir da 2ª página (que é o mesmo do DOQ). Ver
[docs/MOD39_MOD40_DIFERENCAS.md#cabeçalho-de-página](docs/MOD39_MOD40_DIFERENCAS.md#cabeçalho-de-página)
para o detalhamento completo.

### Markdown mínimo para uma NIT

Não há página de capa, então o H1 inicial é opcional. Opcionalmente, o arquivo pode
começar com um bloco de front matter (ver seção acima) para já trazer `doc-code`/
`doc-rev`/`doc-date`/`doc-title` embutidos:

- **Sem H1**: o arquivo pode começar direto em `## SUMÁRIO` (ou em `## SUMÁRIO` logo
  após o front matter, se houver). Nesse caso defina `doc-title` via front matter ou
  `--doc-title` (senão fica o default `TÍTULO`).
- **Com H1**: se o markdown trouxer um H1 antes do sumário (por reaproveitar a
  mesma transcrição de origem de um DOQ, por exemplo), seu texto é usado como
  título do cabeçalho da 1ª página (a menos que `doc-title` já tenha vindo do
  front matter ou de `--doc-title`) e depois **descartado** do corpo junto com as
  linhas de metadados até o próximo `---` — não vira página de capa.

Depois do front matter (opcional) e do H1 (opcional), a estrutura é igual à do DOQ:

1. Heading `## SUMÁRIO` (conteúdo descartado, substituído pelo `TOC` nativo).
2. Separador `---`.
3. Corpo do documento (headings numerados, parágrafos, tabelas, listas).

Exemplo mínimo (sem H1, com front matter):

```markdown
---
doc-code: NIT-LAINF-009
doc-rev: "00"
doc-date: Jun/2026
doc-title: TÍTULO DA NORMA
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

Exemplo mínimo (sem H1, sem front matter — dados só via CLI):

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
