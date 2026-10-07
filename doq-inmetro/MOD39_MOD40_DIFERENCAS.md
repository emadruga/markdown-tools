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

## Resumo

O corpo do documento é **igual** nos dois formatos — mesma fonte, mesmo tamanho, mesmas
margens, mesmo cabeçalho/rodapé de página, mesma mecânica de sumário. A diferença real
está em **ter ou não página de capa** antes do sumário.

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
| Cabeçalho de página (demais páginas) | Tabela de 4 colunas: logo INMETRO \| CODIFICAÇÃO (código do doc + "REV. XX") \| PÁGINA (campo `PAGE`/`NUMPAGES`) | mesma estrutura de tabela, mesmos campos de Word |
| Rodapé | Linha fina + texto em Arial 8 pt, negrito: `<código> - Rev. XX – Publicado <mês/ano> – Pg. X/Y – Responsabilidade: <sigla> – Referência(s): <norma>` | mesma estrutura, Arial é a única exceção à fonte Times New Roman em ambos os modelos |
| Tabelas | Bordas simples, `sz="4"`, `tblCellMar` de 70 twips | igual (ex.: tabela "Histórico da Revisão e Quadro de Aprovação" na NIT usa exatamente os mesmos valores de borda do padrão DOQ) |
| Mecânica do sumário | Lista numerada automática do Word (`w:numPr`, `w:numFmt="decimal"`), nível 0 com `ind left="720" hanging="360"` na definição base, sobrescrito para `left="0" firstLine="0"` no parágrafo, mais uma tab em 284 twips | **igual nos dois** — o DOQ usa `numId=11` → `abstractNumId=0` (decimal), a NIT usa `numId=15` → `abstractNumId=2` (também decimal). Nenhum dos dois usa bullet (`•`) no sumário; isso só aparece como artefato ao extrair texto puro com `textutil -convert txt`, que renderiza qualquer item de lista numerada como bullet genérico |

## O que é diferente

| Aspecto | DOQ (MOD-39) | NIT (MOD-40) |
|---|---|---|
| Página de capa | **Tem capa própria**: título do documento, "Diretoria de ...", "Documento de caráter orientativo", código (`DOQ-XXXXX-YYY`), "Revisão YY - MÊS/ANO" — tudo centralizado, antes do sumário | **Não tem capa** — o documento abre direto no SUMÁRIO |
| Cabeçalho da 1ª página | Reduzido: logo + "Instituto Nacional de Metrologia, Qualidade e Tecnologia" (sem código/revisão/página) | Completo desde a 1ª página: logo + CODIFICAÇÃO + REV. + PÁGINA (mesmo cabeçalho usado nas páginas seguintes) |
| Seções de página (`w:sectPr`) | 3 seções: capa (cabeçalho reduzido) → transição → corpo (cabeçalho completo) | **1 única seção** para o documento inteiro |
| `w:titlePg` | Presente (a capa é uma "primeira página" visualmente distinta dentro da mesma seção/ou seção própria) | Presente no XML do modelo em branco (`header2`/`footer2` = "first"), mas como o conteúdo real começa no sumário, a primeira página já usa o cabeçalho completo — não há uma capa reduzida de fato |
| Listas "a) b) c)" no corpo de texto corrido | Não aplicável a este nível (varia por documento) | No modelo MOD-40, são **texto literal digitado** (`a)`, `b)` como runs em negrito seguidos do texto), não listas automáticas do Word — diferente do sumário, que usa numeração automática |
| Nomes de estilo no `styles.xml` | Em português (`Ttulo1`...`Ttulo9`, `Corpodetexto`, `Cabealho`, `Rodap`) | Em inglês (`Heading1`...`Heading5`, `Header`, `Footer`) — indica que os dois `.doc`/`.docx` têm histórico de edição/template distinto, mas isso é só nomenclatura interna do Word, não afeta a renderização |

## Implicação para a ferramenta de conversão

Como o corpo do documento (headings numerados, parágrafos, tabelas, listas, rodapé,
cabeçalho de página) é idêntico entre os dois formatos, **não foi necessário um script
de conversão novo**. Em vez disso, [`markdown2inmetro_docx.py`](markdown2inmetro_docx.py) recebeu
um knob de linha de comando:

```
python markdown2inmetro_docx.py <input.md> --format {doq,nit}
```

- `--format doq` (padrão): gera a página de capa própria e usa o cabeçalho reduzido na
  primeira página, como no MOD-Gabin-39.
- `--format nit`: pula a capa — se o markdown de entrada tiver um H1 antes do
  `## SUMÁRIO`, ele é apenas descartado (a identificação do documento já aparece na
  coluna CODIFICAÇÃO do cabeçalho); o SUMÁRIO abre o documento diretamente, já sob o
  cabeçalho completo, reproduzindo a seção única do MOD-Gabin-40.

A constante `DOC_CODE` (e os textos fixos de rodapé `FOOTER_TEXT_PREFIX`/
`FOOTER_TEXT_SUFFIX`) no topo do script continuam fixas por enquanto — devem ser
ajustadas manualmente no arquivo para cada norma (DOQ-DIMCI-020, NIT-LAINF-009 etc.) até
que, se necessário, sejam expostas também como argumentos de CLI.
