# Diferenças entre MOD-Gabin-39 (DOQ) e MOD-Gabin-40 (NIT)

Levantamento comparativo entre os dois modelos institucionais do Inmetro:

- **MOD-Gabin-39_02** — modelo do DOQ (Documento Orientativo da Qualidade), `.docx`.
- **MOD-Gabin-40_02** — modelo da NIT (Norma Inmetro Técnica), originalmente `.doc`
  (Compound File binário legado); convertido para `.docx` via Word para permitir a
  inspeção do XML interno (`document.xml`, `styles.xml`, `numbering.xml`,
  headers/footers).

Método: extração e comparação direta do OOXML dos dois arquivos de modelo (não dos
documentos finais preenchidos), já que ambos são os templates em branco que definem o
padrão visual de cada família de documento.

> **Nota sobre a fonte do cabeçalho da NIT:** o `MOD-Gabin-40_02.doc` em
> `normas/` é um template genérico em branco (campos preenchidos só com "XX") e,
> ao ser inspecionado via XML, mostrava um cabeçalho de página de 1 linha ×
> 4 colunas — estruturalmente idêntico ao do DOQ. Documentos NIT publicados
> reais, porém, usam um cabeçalho diferente na 1ª página (ver
> [Cabeçalho de página](#cabeçalho-de-página) abaixo), confirmado a partir de
> prints de uma NIT real fornecidos durante a implementação. Ou seja: **o
> template MOD-40 em `normas/` não reflete fielmente o cabeçalho da 1ª página
> usado na prática** — o restante deste documento já descreve o comportamento
> corrigido, validado contra o exemplo real, não o que o template sozinho
> sugeria.

## Resumo

O corpo do documento (headings numerados, parágrafos, tabelas, listas, rodapé, mecânica
de sumário) é **igual** nos dois formatos — mesma fonte, mesmo tamanho, mesmas margens.
As diferenças reais estão no **cabeçalho da 1ª página** e em **ter ou não página de
capa** antes do sumário.

## O que é idêntico

| Aspecto | Valor | Observação |
|---|---|---|
| Tamanho de página | A4 (`w:w="11907" w:h="16840"`, twips) | igual nos dois |
| Margem superior | 567 twips ≈ 1,0 cm | igual |
| Margem inferior | 851 twips ≈ 1,5 cm | igual |
| Margem esquerda | 851 twips ≈ 1,5 cm | igual |
| Margem direita | 851 twips ≈ 1,5 cm | igual |
| Distância do cabeçalho | 1134 twips ≈ 2,0 cm | igual |
| Distância do rodapé | 567 twips ≈ 1,0 cm | igual |
| Fonte do corpo | Times New Roman, 12 pt (`w:sz="24"` half-points) | confirmado tanto em `rPrDefault` quanto nos runs reais do corpo (356 ocorrências de `sz=24` no DOQ, 402 na NIT) |
| Cabeçalho de página (a partir da 2ª página) | Tabela de 1 linha × 4 colunas: logo INMETRO \| CODIFICAÇÃO (código do doc + "REV. XX") \| PÁGINA (campo `PAGE`/`NUMPAGES`) | mesma estrutura de tabela, mesmos campos de Word — mas na NIT isso só vale a partir da 2ª página; a 1ª tem cabeçalho próprio, ver [Cabeçalho de página](#cabeçalho-de-página) |
| Rodapé | Linha fina + texto em Arial 8 pt, negrito: `<código> - Rev. XX – Publicado <mês/ano> – Pg. X/Y – Responsabilidade: <sigla> – Referência(s): <norma>` | mesma estrutura, Arial é a única exceção à fonte Times New Roman em ambos os modelos |
| Tabelas | Bordas simples, `sz="4"`, `tblCellMar` de 70 twips | igual (ex.: tabela "Histórico da Revisão e Quadro de Aprovação" na NIT usa exatamente os mesmos valores de borda do padrão DOQ) |
| Mecânica do sumário | Lista numerada automática do Word (`w:numPr`, `w:numFmt="decimal"`), nível 0 com `ind left="720" hanging="360"` na definição base, sobrescrito para `left="0" firstLine="0"` no parágrafo, mais uma tab em 284 twips | **igual nos dois** — o DOQ usa `numId=11` → `abstractNumId=0` (decimal), a NIT usa `numId=15` → `abstractNumId=2` (também decimal). Nenhum dos dois usa bullet (`•`) no sumário; isso só aparece como artefato ao extrair texto puro com `textutil -convert txt`, que renderiza qualquer item de lista numerada como bullet genérico |

## O que é diferente

| Aspecto | DOQ (MOD-39) | NIT (MOD-40) |
|---|---|---|
| Página de capa | **Tem capa própria**: título do documento, "Diretoria de ...", "Documento de caráter orientativo", código (`DOQ-XXXXX-YYY`), "Revisão YY - MÊS/ANO" — tudo centralizado, antes do sumário | **Não tem capa** — o documento abre direto no SUMÁRIO |
| Cabeçalho da 1ª página | Reduzido: logo + "Instituto Nacional de Metrologia, Qualidade e Tecnologia" (sem código/revisão/página) | **Cabeçalho especial de 2 linhas × 4 colunas** (título, norma/código, revisão, data de publicação, página) — diferente tanto da capa do DOQ quanto do cabeçalho padrão da própria NIT nas páginas seguintes. Ver [Cabeçalho de página](#cabeçalho-de-página) |
| Cabeçalho a partir da 2ª página | Completo: logo + CODIFICAÇÃO + REV. + PÁGINA | **Idêntico ao do DOQ** — mesma tabela de 1 linha × 4 colunas |
| Quebra entre sumário e corpo | Força quebra de página (`w:br type="page"`) logo após o campo `TOC` — sumário sempre numa página própria | **Sem quebra forçada** — o texto flui do sumário direto para o primeiro heading do corpo (ex. "1 OBJETIVO"), podendo ficar na mesma página se couber |
| Seções de página (`w:sectPr`) | 3 seções: capa (cabeçalho reduzido) → transição → corpo (cabeçalho completo) | **2 seções**: 1ª página (cabeçalho especial 2×4) → corpo (cabeçalho padrão, igual ao DOQ a partir da 2ª página) |
| Listas "a) b) c)" no corpo de texto corrido | Não aplicável a este nível (varia por documento) | No modelo MOD-40, são **texto literal digitado** (`a)`, `b)` como runs em negrito seguidos do texto), não listas automáticas do Word — diferente do sumário, que usa numeração automática |
| Nomes de estilo no `styles.xml` | Em português (`Ttulo1`...`Ttulo9`, `Corpodetexto`, `Cabealho`, `Rodap`) | Em inglês (`Heading1`...`Heading5`, `Header`, `Footer`) — indica que os dois `.doc`/`.docx` têm histórico de edição/template distinto, mas isso é só nomenclatura interna do Word, não afeta a renderização |

## Cabeçalho de página

A diferença mais significativa entre os dois formatos está no cabeçalho — e ela não é
uniforme dentro do próprio documento NIT: a 1ª página usa um layout, as demais usam
outro.

### DOQ — cabeçalho único (exceto capa)

- **Capa** (1ª página): reduzido — logo + "Instituto Nacional de Metrologia, Qualidade
  e Tecnologia", sem código/revisão/página.
- **A partir do sumário (2ª página em diante)**: tabela de **1 linha × 4 colunas** —
  logo | CODIFICAÇÃO (rótulo + código do documento) | REV. (rótulo + revisão) | PÁGINA
  (rótulo + campo `PAGE`/`NUMPAGES`).

### NIT — cabeçalho da 1ª página diferente de todo o resto

- **1ª página** (onde fica o SUMÁRIO): tabela de **2 linhas × 4 colunas**:
  - Coluna 1 (mesclada verticalmente): logo INMETRO.
  - Coluna 2 (mesclada verticalmente): **TÍTULO** do documento, centralizado.
  - Coluna 3, linha 1: rótulo "NORMA Nº / CODIFICAÇÃO" + código do documento.
  - Coluna 3, linha 2: rótulo "PUBLICADO EM" + mês/ano de publicação.
  - Coluna 4, linha 1: rótulo "REV. Nº" + número da revisão.
  - Coluna 4, linha 2: rótulo "PÁGINA" + campo `PAGE`/`NUMPAGES`.
- **A partir da 2ª página** (primeiro heading do corpo em diante, ex. "1 OBJETIVO"):
  volta a ser a mesma tabela de **1 linha × 4 colunas** do DOQ — logo | CODIFICAÇÃO |
  REV. | PÁGINA.

Ou seja, a NIT tem *três* variações de cabeçalho ao longo do documento se comparada à
régua do DOQ: nenhuma capa reduzida, mas uma 1ª página com informação extra (título,
data de publicação) que nem o DOQ nem o resto da própria NIT mostram.

## Implicação para a ferramenta de conversão

Como o corpo do documento (headings numerados, parágrafos, tabelas, listas, rodapé) é
idêntico entre os dois formatos, **não foi necessário um script de conversão novo**. Em
vez disso, [`markdown2inmetro_docx.py`](../markdown2inmetro_docx.py) recebeu um knob de
linha de comando e um conjunto de argumentos para os dados de identificação do
documento (ver [QUICKSTART.md](../QUICKSTART.md) para a lista completa):

```
python markdown2inmetro_docx.py <input.md> --format {doq,nit} \
  --doc-code CÓDIGO --doc-rev REVISÃO --doc-title TÍTULO --doc-date MÊS/ANO
```

- `--format doq` (padrão): gera a página de capa própria e usa o cabeçalho reduzido na
  primeira página, como no MOD-Gabin-39. `--doc-title`/`--doc-date` são ignorados nesse
  formato (o título vem do H1 da capa; a data não aparece no cabeçalho do DOQ).
- `--format nit`: pula a capa — se o markdown de entrada tiver um H1 antes do
  `## SUMÁRIO`, seu texto é usado como `DOC_TITLE` do cabeçalho da 1ª página (a menos
  que `doc-title` já tenha sido definido via CLI ou front matter) e depois descartado
  do corpo. O documento usa **duas seções de página**, replicando a estrutura real do
  MOD-Gabin-40 descrita acima: a 1ª seção cobre só a 1ª página (SUMÁRIO), com o
  cabeçalho especial de 2 linhas × 4 colunas (`build_header_nit()`); ao encontrar o
  primeiro heading do corpo, uma nova seção (`WD_SECTION.CONTINUOUS`, sem quebra de
  página manual) assume o cabeçalho padrão de 1 linha (`build_header()`, igual ao
  usado pelo DOQ a partir da 2ª página).

Os quatro campos `--doc-code`/`--doc-rev`/`--doc-title`/`--doc-date` também podem ser
definidos direto no markdown, num bloco de front matter (`doc-code:`/`doc-rev:`/
`doc-title:`/`doc-date:`, delimitado por `---` na 1ª linha do arquivo) lido por
`extract_front_matter()` — a CLI tem prioridade sobre o front matter quando os dois
definem o mesmo campo. Essa é a forma recomendada para documentos que são convertidos
repetidamente (como os fixtures em `testes/`), evitando repetir as flags a cada
execução. Ver [QUICKSTART.md](../QUICKSTART.md#definindo-os-dados-do-documento-via-front-matter-alternativa-às-flags)
para a sintaxe completa.

A constante `FOOTER_TEXT_PREFIX`/`FOOTER_TEXT_SUFFIX` no topo do script continua fixa
por enquanto — deve ser ajustada manualmente no arquivo para cada norma até que, se
necessário, seja exposta também como argumento de CLI ou chave de front matter.
