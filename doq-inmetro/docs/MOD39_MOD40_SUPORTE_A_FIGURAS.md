# Suporte a figuras no pipeline DOQ/NIT — análise e recomendação

## Problema

Os documentos gerados a partir de `MOD-Gabin-39_02.docx` (DOQ) e `MOD-Gabin-40_02.docx`
(NIT) frequentemente têm figuras (diagramas, prints, fluxogramas). Hoje, imagens
estáticas precisam ser **inseridas manualmente no `.docx`** depois que
[markdown2inmetro_docx.py](../markdown2inmetro_docx.py) termina a conversão — o parser
Markdown→DOCX não tem nenhum tratamento para imagens no corpo do documento.

Confirmado por inspeção do script: a única chamada a `add_picture()` no código é em
`add_logo_run()` (logo fixo do cabeçalho/capa); não existe regex, heading ou bloco que
reconheça sintaxe de imagem (`![alt](caminho)`) no loop principal de parsing
(`convert()`, a partir da linha ~916).

## Pergunta motivadora

Já que Markdown "não lida com figuras" neste pipeline, vale substituir Markdown por
LaTeX como formato de entrada?

## Recomendação: não migrar para LaTeX

O valor do pipeline atual está inteiramente em produzir um `.docx` **fiel aos moldes
institucionais** `MOD-Gabin-39`/`MOD-Gabin-40` — cabeçalho de 2 linhas × 4 colunas na 1ª
página da NIT, TOC nativo do Word (campo `TOC`, não texto estático), bordas de célula
customizadas, numeração de página via campos `PAGE`/`NUMPAGES`, etc. (ver
[MOD39_MOD40_DIFERENCAS.md](MOD39_MOD40_DIFERENCAS.md)). Essa fidelidade é alcançada
hoje porque [markdown2inmetro_docx.py](../markdown2inmetro_docx.py) manipula o `.docx`
diretamente via `python-docx`, replicando o OOXML do modelo peça por peça.

Trocar a entrada por LaTeX não resolve esse problema — ele só é bom em lidar com
figuras na **entrada**. Para sair em `.docx` Word nativo e editável (requisito do
Inmetro), seria necessário um passo LaTeX → DOCX, tipicamente via Pandoc. Na prática,
esse tipo de conversão:

- Não reproduz com fidelidade cabeçalhos/rodapés customizados com múltiplas colunas,
  bordas de célula e campos nativos do Word — exatamente o que este projeto mais
  precisa manter.
- Obrigaria a reescrever do zero toda a lógica de layout já validada e testada em
  [markdown2inmetro_docx.py](../markdown2inmetro_docx.py) (cobertura dos dois formatos,
  front matter, TOC, numeração, bullets com recuo especial etc. — ~1250 linhas).

Ou seja: a troca eliminaria um passo manual pequeno (inserir imagem) e introduziria um
problema muito maior (reformatar o `.docx` inteiro manualmente a cada geração, porque a
conversão automática não preservaria o padrão institucional).

**Conclusão**: o problema não é a linguagem de marcação de entrada — é que o parser
Markdown→DOCX atual não implementa a sintaxe de imagem. Isso é uma lacuna pontual de
funcionalidade, não uma limitação estrutural do Markdown nem do pipeline.

## Caminho recomendado: estender o parser atual

Adicionar suporte à sintaxe padrão de imagem do Markdown, `![legenda](caminho/arquivo.png)`,
como mais um tipo de linha reconhecida no loop principal do parser, ao lado do que já
existe para headings (`HEADING_RE`) e tabelas (`TABLE_ROW_RE`) em
[markdown2inmetro_docx.py:916](../markdown2inmetro_docx.py#L916).

Passos de implementação:

1. **Regex de reconhecimento** — nova constante, ex. `IMAGE_RE = re.compile(r'^!\[(.*)\]\((.+)\)$')`,
   testada no início do loop (antes ou depois de `TABLE_ROW_RE`, já que ambas são
   mutuamente exclusivas por linha).
2. **Método `add_figure()` no builder** (`DocxBuilder`, ao lado de `add_paragraph_text`,
   `add_bullet`, `add_table`):
   - Insere a imagem com `run.add_picture(caminho, width=...)`, limitando a largura à
     área útil da página (já calculável a partir das margens definidas em
     `setup_docDefaults`/`convert()`), para nunca estourar a margem.
   - Centraliza o parágrafo da imagem (`WD_ALIGN_PARAGRAPH.CENTER`).
   - Reaproveita `add_italic_caption()` (já existe, usado para legendas) para renderizar
     o texto `alt` do Markdown como legenda abaixo da figura, mantendo o estilo
     tipográfico já padronizado (itálico, 10pt).
3. **Resolução de caminho** — caminho da imagem no Markdown deve ser resolvido relativo
   ao diretório do `.md` de entrada (consistente com como ferramentas de Markdown en
   geral resolvem imagens locais), não ao diretório de execução do script.
4. **Validação de erro** — se o arquivo de imagem não existir, falhar a conversão com
   mensagem clara (caminho + linha do Markdown), em vez de gerar um `.docx` com erro
   silencioso ou imagem ausente.
5. **Atualizar [QUICKSTART.md](../QUICKSTART.md)** com a nova sintaxe suportada e um
   exemplo mínimo de figura no corpo do documento.

Esse caminho elimina 100% do passo manual de inserção de imagem, sem abrir mão da
fidelidade ao modelo institucional que o pipeline atual já garante.

## Status

Análise registrada; implementação ainda não iniciada (aguardando decisão de prosseguir).
