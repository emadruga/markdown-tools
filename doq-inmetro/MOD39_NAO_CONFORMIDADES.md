# Não Conformidades — DOQ-DIMCI-020 (agosto/2026) × MOD-Gabin-39_02

Verificação de **forma/formatação** do documento
`./DOQ-DIMCI-020_agosto2026.pdf` (409 páginas, A4) contra o modelo-padrão
`./referencias/MOD-Gabin-39_02.docx` (Rev. 02 – modelo oficial de DOQ do SGQI).

Escopo desta análise: **apenas o padrão de formatação do MOD-Gabin-39** — margens,
fontes, tamanhos, negrito/itálico, cor, cabeçalho, rodapé, logotipo e sua aplicação
no corpo e nos anexos. **Não** abrange conteúdo técnico nem os demais itens da
NIG-Gabin-040 (checklist do Anexo F), que são tratados em
`docs/PLANO_PARA_VERFICACAO_DA_CONFORMIDADE.md`.

- **Documento avaliado:** `DOQ-DIMCI-020_agosto2026.pdf` (fonte: `DOQ-DIMCI-020_agosto2026.docx`)
- **Norma/modelo de referência:** `referencias/MOD-Gabin-39_02.docx`
- **Data da verificação:** 2026-08-24
- **Método:** extração de propriedades OOXML do `.docx` (margens, fontes, estilos,
  cabeçalho/rodapé) + análise dos glifos renderizados no PDF (PyMuPDF) e inspeção
  visual dos recortes de cabeçalho, rodapé e logotipo.

---

## Parâmetros de referência do MOD-Gabin-39 (extraídos do modelo)

| Parâmetro | Valor no MOD-Gabin-39 |
|---|---|
| Tamanho da página | A4 (21,0 × 29,7 cm), retrato |
| Margem superior | **1,0 cm** |
| Margem inferior | **1,5 cm** |
| Margem esquerda | **1,5 cm** |
| Margem direita | **1,5 cm** |
| Distância do cabeçalho | **2,0 cm** |
| Distância do rodapé | 1,0 cm |
| Primeira página diferente | **Sim** (`different_first_page = true`) |
| Fonte padrão (docDefaults) | **Times New Roman** |
| Corpo de texto | Times New Roman **12 pt**, justificado |
| Títulos de seção | Times New Roman 12 pt, **negrito**, caixa alta |
| Cor do texto | Preto |
| Logotipo (cabeçalho) | INMETRO **monocromático preto**, ~1,79 × 1,87–1,97 cm |
| Rodapé | Arial **8 pt negrito**: `MOD-Gabin-039 - Rev. 02 – Publicado Xxx/21 – Pg.3/3 – Responsabilidade: Gabin – Referência(s): NIG-Gabin-040` |
| Cabeçalho (1ª pág.) | Tabela 1×2: [logo] + "Instituto Nacional de Metrologia, Qualidade e Tecnologia" (negrito) |
| Cabeçalho (demais) | Tabela 1×4: [logo] + **CODIFICAÇÃO** + **REV.** + **PÁGINA** |

---

## Resumo das não conformidades

| # | Item | Severidade | Onde |
|---|---|---|---|
| NC-01 | Margens da página divergentes (as 4 margens) | **Alta** | Todo o documento |
| NC-02 | Distância do cabeçalho divergente (1,0 vs 2,0 cm) | Média | Todo o documento |
| NC-03 | Logotipo em **azul** em vez de **preto monocromático** | **Alta** | Cabeçalho (todas as págs.) |
| NC-04 | Dimensão do logotipo reduzida/distorcida (altura) | Baixa | Cabeçalho (todas as págs.) |
| NC-05 | Rodapé sem os campos `Pg.X/X` e `Referência(s): NIG-...` | Média | Rodapé (todas as págs.) |
| NC-06 | Rótulo "CODIFICAÇÃO" ausente no cabeçalho | Baixa | Cabeçalho (págs. 2+) |
| NC-07 | Fonte padrão do documento é Calibri/11 pt (docDefaults) | Média (latente) | Estrutura do `.docx` |
| NC-08 | Norma de referência NIG-Gabin-040 ausente das referências e do rodapé | Média | Seção 4 (pág. 7) e rodapé |

Observações que **não** foram classificadas como NC formal contra o MOD-Gabin-39
(item de atenção) estão na seção [Observações](#observações).

---

## Detalhamento

### NC-01 — Margens da página divergentes (todas as quatro) — Severidade: Alta

O MOD-Gabin-39 define margens **T=1,0 / B=1,5 / E=1,5 / D=1,5 cm**. O documento
avaliado usa margens do padrão Word (Normal/Moderada), divergentes em todas:

| Margem | MOD-Gabin-39 | DOQ-DIMCI-020 | Divergência |
|---|---|---|---|
| Superior | 1,0 cm | **2,5 cm** | +1,5 cm |
| Inferior | 1,5 cm | **2,0 cm** | +0,5 cm |
| Esquerda | 1,5 cm | **2,5 cm** | +1,0 cm |
| Direita | 1,5 cm | **2,0 cm** | +0,5 cm |

> Fonte: `sectPr` de ambas as seções do `.docx` (`top=2,5 bottom=2,0 left=2,5
> right=2,0 cm`). Confirmado no PDF pela extensão do texto renderizado.

**Ação:** ajustar as margens de todas as seções para o padrão do MOD-Gabin-39.

---

### NC-02 — Distância do cabeçalho divergente — Severidade: Média

O modelo define **distância do cabeçalho = 2,0 cm**; o documento usa **1,0 cm**
(`header_distance`). A distância do rodapé (1,0 cm) está conforme.

**Ação:** definir a distância do cabeçalho em 2,0 cm.

---

### NC-03 — Logotipo em cor azul em vez de preto monocromático — Severidade: Alta

O MOD-Gabin-39 embute o logotipo do INMETRO em **preto monocromático**
(símbolo "I" + "INMETRO"). O documento avaliado usa a versão **azul institucional**
(cor dominante ≈ `#114781`), em todas as páginas do cabeçalho.

> Fonte: imagem `word/media/image1.png` do `.docx` (cores dominantes: preto +
> azul `#114781`), contra `word/media/image1.jpeg` do modelo (preto puro).

**Ação:** substituir pelo logotipo monocromático preto conforme o MOD-Gabin-39.

> **Ressalva:** o MOD-Gabin-39 é um *modelo*; caso a identidade visual vigente do
> INMETRO (rtac002120 / PAI000187) autorize/exija a versão azul, este item deve ser
> reclassificado. A comparação aqui é estritamente contra o logotipo embutido no
> MOD-Gabin-39, conforme solicitado.

---

### NC-04 — Dimensão do logotipo reduzida na altura — Severidade: Baixa

O logotipo no modelo é exibido com ~**1,79 × 1,87 cm** (1ª pág.) / **1,79 × 1,97 cm**
(demais). No documento avaliado é exibido com **1,79 × 1,60 cm** — mesma largura,
porém altura menor, indicando recorte/proporção diferente da do modelo.

**Ação:** aplicar o logotipo com as dimensões/proporção do MOD-Gabin-39.

---

### NC-05 — Rodapé sem os campos `Pg.X/X` e `Referência(s)` — Severidade: Média

Formato do rodapé no modelo (Arial 8 pt negrito):

```
MOD-Gabin-039 - Rev. 02 – Publicado Xxx/21 – Pg.3/3 – Responsabilidade: Gabin – Referência(s): NIG-Gabin-040
```

Rodapé do documento avaliado (fonte **conforme**: Arial 8 pt negrito):

```
DOQ-DIMCI-020 - Rev. 01 – Publicado Jun/2026 – Responsabilidade: Dmtic
```

- ✔ Codificação, revisão, mês/ano e responsabilidade foram preenchidos (esperado).
- ✘ **Falta o campo de paginação** `– Pg.X/X` presente no modelo.
- ✘ **Falta o campo** `– Referência(s): NIG-Gabin-040` (referência normativa) presente no modelo.

**Ação:** incluir os campos `Pg.X/X` e `Referência(s): NIG-Gabin-040` no rodapé.

> Nota: a paginação existe hoje **no cabeçalho** (célula "PÁGINA X/409"), não no
> rodapé. O modelo posiciona a paginação no rodapé (`Pg.X/X`). Padronizar conforme
> o MOD-Gabin-39.

---

### NC-06 — Rótulo "CODIFICAÇÃO" ausente no cabeçalho — Severidade: Baixa

No cabeçalho das páginas 2+, o modelo usa uma tabela 1×4 com os rótulos
**CODIFICAÇÃO / REV. / PÁGINA**. O documento mantém os rótulos "REV." e "PÁGINA"
(com os valores "01" e "X/409"), mas na primeira célula exibe diretamente o código
**"DOQ-DIMCI-020"**, **sem o rótulo "CODIFICAÇÃO"** acima.

**Ação:** restaurar o rótulo "CODIFICAÇÃO" sobre o código, alinhando ao padrão das
demais células (rótulo + valor).

> **Ressalva:** interpretação ambígua — "CODIFICAÇÃO" pode ser lido como
> texto-marcador a ser substituído pelo código. Mantido como NC de baixa
> severidade por consistência com "REV." e "PÁGINA", que preservam o rótulo.

---

### NC-07 — Fonte padrão do documento (docDefaults) é Calibri/11 pt — Severidade: Média (latente)

O `docDefaults` do `.docx` define a fonte padrão como **tema `minorHAnsi`
(Calibri) a 11 pt** — herança do modelo em branco do Word, e **não** Times New Roman
12 pt como no MOD-Gabin-39. Na prática, o texto renderizado no PDF **está em Times
New Roman 12 pt** porque os estilos/execuções sobrepõem o padrão. Ainda assim, é uma
não conformidade estrutural latente: qualquer novo parágrafo ou edição que caia no
padrão herdará Calibri 11 pt.

> Fonte: `w:docDefaults/w:rPrDefault/w:rPr/w:rFonts = minorHAnsi (Calibri)`,
> `w:sz = 22` (11 pt). Nenhum caractere Calibri foi encontrado no PDF renderizado.

**Ação:** definir Times New Roman 12 pt como fonte padrão (docDefaults) e no estilo
Normal, para robustez editorial.

---

### NC-08 — Norma de referência NIG-Gabin-040 ausente das referências e do rodapé — Severidade: Média

O rodapé do MOD-Gabin-39 declara explicitamente a norma que rege a estrutura do
documento: `Referência(s): NIG-Gabin-040`. Ou seja, o padrão do próprio modelo
determina que a **NIG-Gabin-040** seja citada como documento de referência normativa
da formatação. No DOQ-DIMCI-020 avaliado, a NIG-Gabin-040 **não aparece em nenhum
local**:

- **Seção "4 DOCUMENTOS DE REFERÊNCIA" (pág. 7):** lista apenas a Portaria Inmetro
  nº 171/2026.
- **Seção "5 DOCUMENTOS COMPLEMENTARES" (pág. 7):** ABNT NBR ISO 19011, ISO 9001 e
  ISO/IEC 17065.
- **Rodapé (todas as páginas):** omite o campo `– Referência(s): NIG-Gabin-040`
  (ver também [NC-05](#nc-05--rodapé-sem-os-campos-pgxx-e-referências--severidade-média)).
- **Bibliografia (págs. 403–409):** contém ~130 referências acadêmicas (ABNT NBR
  6023) que embasam o modelo de maturidade, mas nenhuma norma do SGQI.

> **Observação sobre o MOD-Gabin-39 em si:** o modelo (MOD-Gabin-39) **não** deve ser
> citado como documento de referência — o padrão manda referenciar a **NIG-Gabin-040**,
> que é a norma-mestra de estrutura/formatação. Portanto a lacuna a corrigir é a
> ausência da NIG-Gabin-040, não a do MOD-39. A NIG-Gabin-041 (publicação no Sidoq)
> deve ser incluída também, se aplicável ao fluxo de publicação deste DOQ.

**Ação:** incluir a **NIG-Gabin-040** na seção "4 Documentos de referência" e
restaurar o campo `– Referência(s): NIG-Gabin-040` no rodapé (corrige conjuntamente
a NC-05). Avaliar a inclusão da NIG-Gabin-041.

---

## Itens conformes (verificados)

- ✔ **Tamanho e orientação da página:** A4 (21,0 × 29,7 cm), retrato, em todas as 409 páginas.
- ✔ **Fonte do corpo:** Times New Roman 12 pt predominante no corpo, títulos e anexos.
- ✔ **Cor do texto:** 100% preto (`#000000`) — nenhum texto colorido indevido.
- ✔ **Fonte do rodapé:** Arial 8 pt negrito (idêntica ao modelo).
- ✔ **Cabeçalho da 1ª página:** [logo] + "Instituto Nacional de Metrologia, Qualidade e Tecnologia" em negrito, conforme layout do modelo.
- ✔ **Capa:** título (18 pt), diretoria (12 pt negrito), "Documento de caráter orientativo", código (20 pt negrito), "Revisão 01 – Junho/2026" — segue a estrutura da tabela de capa do modelo.
- ✔ **Anexos/Apêndices:** ANEXO I (págs. 14–335), ANEXO II (págs. 336–408), APÊNDICES A/B/C — todos em Times New Roman, títulos em negrito 12 pt, mesma padronização do corpo.

---

## Observações (atenção — não classificadas como NC formal do MOD-Gabin-39)

- **Texto a 10 pt em tabelas dos anexos:** grande volume de texto a 10 pt nas
  tabelas de avaliação (colunas "Nível", "Item de resposta", descrições de nível) e
  nas células de cabeçalho ("REV. 01", "PÁGINA X/409"). O MOD-Gabin-39 exemplifica
  o corpo a 12 pt, mas **não** apresenta tabelas de conteúdo; 10 pt em tabelas é
  prática comum e não há regra explícita no modelo que o proíba. Recomenda-se
  validar contra a NIG-Gabin-040 (Anexo B, layout de DOQ) se há restrição de tamanho
  mínimo em tabelas.
- **Uso de itálico nos anexos:** itálico é usado de forma funcional (rótulos como
  "Respostas", "Métricas/KPIs" e termos em inglês). O corpo do modelo não usa
  itálico, mas o modelo também não o veda.
- **Inconsistência de data:** a capa e o rodapé indicam **"Junho/2026" / "Jun/2026"**,
  enquanto o nome do arquivo é **"agosto2026"**. Verificar qual é a data de
  publicação correta (não é uma NC de formatação contra o MOD-Gabin-39, mas é
  inconsistência editorial relevante).
- **Paginação total = 409 páginas** no cabeçalho ("X/409"): confirmar se a contagem
  reflete a versão final publicada.

---

## Metodologia e reprodutibilidade

Ambiente: `.venv/` na raiz do projeto (`pymupdf`, `python-docx`, `pillow`).
Dados extraídos de:
- Margens/fontes/estilos/cabeçalho/rodapé: propriedades OOXML de
  `DOQ-DIMCI-020_agosto2026.docx` e `referencias/MOD-Gabin-39_02.docx`.
- Fontes/tamanhos/cores renderizados e posição de logotipo: análise dos 409
  glifos/imagens do PDF via PyMuPDF, por faixa (cabeçalho / corpo / rodapé).
- Cor/dimensão do logotipo: inspeção das imagens `word/media/image1.*` de ambos os
  arquivos e recortes renderizados do cabeçalho.
