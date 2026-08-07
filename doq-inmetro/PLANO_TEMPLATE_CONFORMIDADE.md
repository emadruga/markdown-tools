# Plano de Conformidade ao Template Oficial (MOD-Gabin-039)

Análise comparativa entre:

- **Template oficial:** `MOD-Gabin-39_02.docx` — modelo de DOQ do Inmetro
  (MOD-Gabin-039, Rev. 02, publicado Jan/22, responsabilidade Gabin,
  referência NIG-Gabin-040).
- **Versão de trabalho:** `DOQ-DIMCI-020_jun2026-Final.docx` — gerada a
  partir de `DOQ-DIMCI-020_jun2026-Final.md` pelo conversor
  `markdown2doq_docx.py`.

O objetivo deste plano é catalogar as divergências estruturais e visuais
da versão de trabalho em relação ao template institucional obrigatório e
definir as ações de correção, uma por vez, priorizadas por impacto de
conformidade.

> **Nota de escopo.** Este plano trata **exclusivamente da conformidade
> ao template oficial** (estrutura de seções, cabeçalho, rodapé, quadros
> obrigatórios). Não conformidades de **nomenclatura de conteúdo**
> (nomes de dimensão abreviados, uso ambíguo de "Empresa", dimensões sem
> capacidade) são tratadas em documento separado
> (`INCONSISTENCIAS_NOMENCLATURA.md`) e ficam fora deste escopo.

---

## 1. Estrutura de seções obrigatórias

### 1.1 Ordem canônica do template

O MOD-Gabin-039 fixa nove seções numeradas, nesta ordem:

| Nº | Seção (template) |
|----|------------------|
| 1 | Objetivo |
| 2 | Campo de aplicação |
| 3 | Responsabilidade |
| 4 | Documentos de referência |
| 5 | Documentos complementares |
| 6 | Siglas |
| 7 | Termos e definições |
| 8 | *(seção temática livre — "Xxxxx Xxxxx Xxxxx")* |
| 9 | Histórico da revisão e quadro de aprovação |

### 1.2 Ordem atual da versão de trabalho

| Nº | Seção (versão de trabalho) | Correspondência no template |
|----|----------------------------|------------------------------|
| 1 | Objetivo | 1 ✓ |
| 2 | Campo de aplicação | 2 ✓ |
| 3 | Responsabilidade | 3 ✓ |
| 4 | **Histórico da Revisão** | **9** (fora de ordem) |
| 5 | **Documentos Complementares** | **5** (fora de ordem) |
| 6 | **Documentos de Referência** | **4** (fora de ordem) |
| 7 | Siglas | 6 ✓ (só o número diverge) |
| 8 | **Definições** | 7 "Termos e definições" |
| 9 | Generalidades | 8 (temática) |
| 10 | Orientações de Conduta | 8 (temática) |
| 11 | Documentação Pessoal Necessária | 8 (temática) |
| 12 | Conhecimento dos Requisitos de Certificação | 8 (temática) |
| 13 | Avaliação de Maturidade | 8 (temática) |
| — | ANEXO I | (anexo) |
| — | ANEXO II | (anexo) |
| — | Bibliografia | (não numerada) |

### 1.3 Divergências de estrutura

> ✅ **Corrigidas** (E-1, E-2, E-3/E-5, E-4) — ver status e commits na §6.

| ID | Divergência | Situação atual | Situação-alvo (template) |
|----|-------------|----------------|---------------------------|
| E-1 | **Ordem das seções 4-6 trocada.** O template ordena `4 Documentos de referência`, `5 Documentos complementares`; a versão de trabalho traz `5 Documentos Complementares` e `6 Documentos de Referência`, além de intercalar `4 Histórico da Revisão`. | 4 Histórico / 5 Compl. / 6 Ref. | 4 Referência / 5 Complementares |
| E-2 | **Histórico da Revisão fora de posição.** No template é a **seção 9** (final); na versão de trabalho está como **seção 4**, no início. | Seção 4 | Seção 9 |
| E-3 | **Numeração de Siglas divergente.** Template: seção 6; versão de trabalho: seção 7. Consequência de E-1/E-2. | 7 Siglas | 6 Siglas |
| E-4 | **"Definições" vs "Termos e definições".** O template usa o título canônico `7 Termos e definições`; a versão de trabalho usa `8 Definições`. | 8 Definições | 7 Termos e definições |
| E-5 | **Seções temáticas (9-13) ocupam o lugar da seção 8.** O template reserva **uma** seção temática (nº 8) para o conteúdo específico do DOQ; a versão de trabalho tem cinco (9-13). Não é não conformidade em si — o template admite conteúdo temático — mas a **numeração** precisa realinhar após corrigir E-1..E-4. | 9-13 | 8, 8.x… |

### 1.4 Fontes e tamanhos do template

Fonte padrão do documento declarada no `docDefaults` do
`MOD-Gabin-39_02.docx`: **Times New Roman**. Os tamanhos aplicados por
elemento (extraídos das propriedades de run do próprio `.docx`):

| Elemento | Fonte | Tamanho | Estilo |
|----------|-------|---------|--------|
| Corpo de texto | Times New Roman | 12 pt | normal |
| Títulos de seção (`1 OBJETIVO`, `2 CAMPO…`) | Times New Roman | 12 pt | negrito |
| Título do DOQ (capa) | Times New Roman | 24 pt | negrito |
| Código do DOQ na capa (`DOQ-XXXXX-YYY`) | Times New Roman | 28 pt | normal |
| "Documento de caráter orientativo" / "Revisão YY" (capa) | Times New Roman | 12 pt | negrito |
| Cabeçalho — nome do Instituto (capa) | Times New Roman | 12 pt | negrito |
| Cabeçalho — "CODIFICAÇÃO" (páginas internas) | Times New Roman | 10 pt | negrito |
| Cabeçalho — REV. / XX / PÁGINA / nº | Times New Roman | 12 pt | negrito |
| Rodapé (linha `MOD-Gabin-039…`) | Arial | 8 pt | negrito |

Observações:

- O corpo é **uniforme em Times New Roman 12 pt**; títulos de seção
  usam o mesmo tamanho, distinguindo-se apenas pelo negrito.
- A **única exceção de fonte** é o rodapé, em **Arial 8 pt** (não Times
  New Roman).

### 1.5 Divergência de fonte

> ✅ **Corrigidas** (F-1, F-2) — ver status e commits na §6.

| ID | Divergência | Situação atual | Situação-alvo (template) |
|----|-------------|----------------|---------------------------|
| F-1 | **Fonte do corpo divergente.** A versão de trabalho usa **Arial 11 pt** (herança do PDF original, gerado pelo Google Docs) em corpo e títulos de seção; o template exige **Times New Roman 12 pt**. | Arial 11 pt | Times New Roman 12 pt |
| F-2 | **Fonte do rodapé.** Como o rodapé está ausente na versão de trabalho (ver R-1), a fonte correta do rodapé (Arial 8 pt, negrito) precisa ser aplicada ao criá-lo. | (rodapé ausente) | Arial 8 pt, negrito |

A correção de F-1 é abrangente: afeta o estilo `Normal` e os estilos de
heading definidos em `markdown2doq_docx.py` (hoje fixados em Arial).
**Decisão tomada (§5.4):** adotar o padrão do template — corpo e títulos
ambos em Times New Roman 12 pt, distinguidos só pelo negrito, sem
variação de tamanho entre níveis de heading.

---

## 2. Cabeçalho de página

> ✅ **C-1 corrigido** (§6). C-2/C-3 já eram conformes. C-4 (logo) na §2.1.

| ID | Elemento | Template (MOD-Gabin-039) | Versão de trabalho | Ação |
|----|----------|--------------------------|--------------------|------|
| C-1 | **Cabeçalho da capa (pág. 1).** | Logo + **"Instituto Nacional de Metrologia, Qualidade e Tecnologia"** (2 células). | Logo + **"Diretoria de Metrologia Científica e Industrial"**. | **Decisão tomada (§5.1):** adotar o texto do template — "Instituto Nacional de Metrologia, Qualidade e Tecnologia". |
| C-2 | **Rótulo da coluna de código.** | Placeholder `CODIFICAÇÃO`. | `DOQ-DIMCI-020` (código real). | ✓ Conforme — a versão de trabalho preenche o placeholder com o código correto. |
| C-3 | **Colunas REV. / PÁGINA.** | `REV. / XX` e `PÁGINA / n/N` em células distintas. | `REV. 01` e `PÁGINA / n/N`. | ✓ Conforme na forma; confirmar apenas o valor de revisão. |

### 2.1 Dimensão do logo do Inmetro

O template usa a imagem `image1.jpeg` (JPEG 236×256 px, 300 DPI) no
cabeçalho, em dois tamanhos ligeiramente diferentes:

| Cabeçalho | Largura | Altura | EMU (cx × cy) |
|-----------|---------|--------|----------------|
| Capa (pág. 1) | 1,79 cm | 1,87 cm | 643890 × 671830 |
| Páginas internas | 1,79 cm | 1,97 cm | 643890 × 708660 |

A **largura é a mesma** (1,79 cm) nos dois cabeçalhos; só a **altura**
varia (~1 mm). A versão de trabalho, por outro lado, renderiza o logo
(`inmetro-logo.png`) a **2,6 cm de largura** — bem maior que o template.

> ✅ **C-4 corrigido** (§6): logo reduzido para 1,79 cm de largura, com
> altura proporcional ao PNG atual (para não distorcê-lo).

| ID | Divergência | Situação atual | Situação-alvo (template) |
|----|-------------|----------------|---------------------------|
| C-4 | **Logo superdimensionado.** A versão de trabalho renderiza o logo a **2,6 cm de largura**; o template usa **1,79 cm**. | 2,6 cm (largura) | 1,79 cm (largura); altura ~1,87 cm na capa / ~1,97 cm nas internas |

---

## 3. Rodapé de página

> ✅ **R-1 corrigido** (§6). Referências do rodapé ainda a confirmar.

| ID | Elemento | Template (MOD-Gabin-039) | Versão de trabalho | Ação |
|----|----------|--------------------------|--------------------|------|
| R-1 | **Rodapé institucional obrigatório.** | Linha em **todas as páginas**: `MOD-Gabin-039 - Rev. 02 – Publicado Jan/22 – Responsabilidade: Gabin – Referência(s): NIG-Gabin-040`. | **Ausente.** A versão de trabalho não gera rodapé. | **Decisão tomada (§5.2):** criar rodapé `DOQ-DIMCI-020 - Rev. 01 – Publicado Jun/2026 – Responsabilidade: Dmtic`, em todas as páginas. As referências (`Referência(s): …`) ficam **a confirmar**. |

---

## 4. Quadros obrigatórios da seção de Histórico

> ✅ **Q-1 e Q-2 corrigidos** (§6). Na versão de trabalho, esta é a
> seção **13** (Histórico da Revisão e Quadro de Aprovação).

O template define, na sua seção de histórico (nº 9 no template; nº 13 na
versão de trabalho), **dois quadros** distintos:

### 4.1 Quadro "Histórico da Revisão"

| Revisão | Data | Itens Revisados |
|---------|------|-----------------|
| (nº atual) | Xxx/yyyy | ▪ item; ▪ item. |

- **Versão de trabalho:** tem a tabela `Histórico da Revisão` (seção 4),
  porém **vazia** (uma linha em branco).
- **Divergência Q-1:** o quadro existe mas está na posição errada
  (seção 4, não 9) e sem conteúdo.

### 4.2 Quadro "Quadro de Aprovação"

| | Nome | Atribuição |
|--|------|------------|
| Elaborado por: | | |
| Verificado por: | | |
| Aprovado por: | | |

- **Versão de trabalho:** **ausente.** No lugar, há um quadro
  `Controle de Versões` (Versão / Data / Descrição / Autor) ao final do
  documento, que **não corresponde** ao Quadro de Aprovação exigido.
- **Divergência Q-2:** falta o Quadro de Aprovação (Elaborado/Verificado/
  Aprovado por); o `Controle de Versões` atual não o substitui.
- **Decisão tomada (§5.3):** **manter ambos** — adicionar o Quadro de
  Aprovação exigido pelo template e **preservar** o `Controle de Versões`
  existente.

---

## 5. Decisões tomadas

As decisões abaixo foram confirmadas pelo responsável e passam a orientar
as correções da §6.

1. **Texto do cabeçalho da capa (C-1):** adotar **"Instituto Nacional de
   Metrologia, Qualidade e Tecnologia"** (como no template MOD-Gabin-039),
   substituindo "Diretoria de Metrologia Científica e Industrial".
2. **Conteúdo do rodapé (R-1):** montar o rodapé a partir dos dados da
   capa: **"DOQ-DIMCI-020 - Rev. 01 – Publicado Jun/2026 –
   Responsabilidade: Dmtic"**. A área responsável (Dmtic) segue a seção 3
   do documento. As **referências** (`Referência(s): …`) ficam **a
   confirmar** — deixar em branco até indicação dos documentos aplicáveis.
3. **Substituição do "Controle de Versões" (Q-2):** **manter ambos** —
   adicionar o Quadro de Aprovação (Elaborado/Verificado/Aprovado por)
   exigido pelo template e **preservar** o quadro `Controle de Versões`
   existente.
4. **Hierarquia de headings após troca de fonte (F-1):** adotar o
   **padrão do template** — corpo e títulos de seção ambos em **Times New
   Roman 12 pt**, distinguidos apenas pelo negrito (sem variação de
   tamanho entre níveis de heading).

---

## 6. Plano de correção (uma não conformidade por vez)

Ordem sugerida, da maior para a menor prioridade de conformidade, cada
item aplicado e verificado isoladamente antes de passar ao seguinte.

**Status: todos os 11 itens concluídos**, cada um verificado no `.docx`
gerado e commitado individualmente.

| Ordem | ID | Ação | Onde corrigir | Status |
|-------|-----|------|----------------|--------|
| 1 | E-1 | Reordenar seções para `4 Documentos de referência`, `5 Documentos complementares`. | `.md` (ordem dos headings) | ✅ `128b918` |
| 2 | E-2 | Mover `Histórico da Revisão` para o fim (seção **13**, última numerada antes dos anexos — a numeração canônica final foi consolidada no item 4). | `.md` | ✅ `a515c47` |
| 3 | E-4 | Renomear `Definições` → `Termos e definições`. | `.md` | ✅ `3227625` |
| 4 | E-3 / E-5 | Renumerar todas as seções conforme a ordem canônica do template (blocos temáticos sequenciais 8–12, Histórico=13 — decisão de §1.3/§5). | `.md` | ✅ `18da801` |
| 5 | Q-2 | Adicionar o Quadro de Aprovação (Elaborado/Verificado/Aprovado por) na seção 13, **mantendo** o `Controle de Versões` existente (§5.3). | `.md` | ✅ `7576729` |
| 6 | Q-1 | Preencher o quadro Histórico da Revisão (Rev. 01 / Jun/2026 / "Emissão inicial do documento."). | `.md` | ✅ `d67cfa4` |
| 7 | R-1 | Gerar rodapé institucional em todas as páginas (§5.2). | `markdown2doq_docx.py` | ✅ `4e96f08` |
| 8 | C-1 | Ajustar texto do cabeçalho da capa para "Instituto Nacional de Metrologia, Qualidade e Tecnologia" (§5.1). | `markdown2doq_docx.py` | ✅ `8316c8b` |
| 9 | F-1 | Trocar a fonte do corpo/headings (e cabeçalho/capa) para Times New Roman 12 pt (§5.4). | `markdown2doq_docx.py` | ✅ `5eda4b1` |
| 10 | F-2 | Aplicar Arial 8 pt (negrito) ao rodapé (feito junto de R-1). | `markdown2doq_docx.py` | ✅ `4e96f08` |
| 11 | C-4 | Reduzir o logo para 1,79 cm de largura (altura proporcional, para não distorcer o PNG atual). | `markdown2doq_docx.py` | ✅ `bfa3026` |

### Pendências remanescentes

- **Referências do rodapé (R-1):** o campo `Referência(s): …` do rodapé
  ficou em branco, aguardando indicação dos documentos aplicáveis
  (decisão §5.2).

### Observações sobre o conversor

As correções **E-1 a Q-1** são de **conteúdo/ordem** e se resolvem
editando o arquivo `.md` fonte — o conversor as reflete automaticamente.
As correções **R-1, C-1, C-4, F-1 e F-2** exigem alteração no
`markdown2doq_docx.py`:

- **R-1 (rodapé):** hoje o conversor monta apenas o cabeçalho
  (`build_header` / `build_cover_header`); é preciso adicionar uma função
  análoga para o rodapé (`section.footer`), com a linha de codificação em
  fonte reduzida, replicada nas duas seções (capa e corpo).
- **C-1 (texto da capa):** o texto do cabeçalho da capa está fixado em
  `build_cover_header`; basta trocar a string após a decisão §5.1.
- **C-4 (dimensão do logo):** a largura está fixada em `add_logo_run`
  (hoje 2,6 cm); ajustar para 1,79 cm. Como capa e páginas internas têm
  alturas ligeiramente diferentes no template, avaliar se vale
  parametrizar a altura por tipo de cabeçalho ou manter proporção
  automática pela largura.
- **F-1 (fonte):** trocar `Arial` por `Times New Roman` e 11 pt por 12 pt
  no estilo `Normal` e nos headings em `setup_styles`; rever a hierarquia
  de tamanhos dos headings (decisão §5.4).
- **F-2 (fonte do rodapé):** aplicar Arial 8 pt, negrito, na função de
  rodapé criada em R-1.

---

## 7. Itens já conformes

Para registro, os seguintes aspectos da versão de trabalho **já atendem**
ao template e não requerem ação:

- Capa: título centralizado, "Documento de caráter orientativo", código
  do DOQ em destaque e "Revisão NN – MÊS/ANO" (layout equivalente ao
  template).
- Cabeçalho das páginas internas: tabela logo | código | REV. | PÁGINA
  n/N com campos de página dinâmicos.
- Sumário navegável (campo TOC nativo do Word).
- Seções 1-3 (Objetivo, Campo de aplicação, Responsabilidade) na ordem e
  com os títulos canônicos.
- Tabelas de conteúdo com bordas simples e cabeçalho em negrito,
  aderentes ao padrão sóbrio/monocromático do template.
