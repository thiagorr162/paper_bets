# Bets e saúde mental: análises do artigo

Notebooks que reproduzem os gráficos e as tabelas do site
[Bets e saúde mental no Brasil](https://thiagorr162.github.io/assets/html/bets.html) (parte de saúde mental) e
gravam tudo no repositório do artigo no Overleaf (`../artigo/`).

## Como rodar

```bash
uv sync
uv run jupyter execute notebooks/*.ipynb   # roda tudo sem gravar saídas nos notebooks
# ou, para abrir e ler: uv run jupyter lab
```

| Notebook | Seção do site | Saídas em `../artigo/` |
|---|---|---|
| `01_series_mensais` | Busca por apostas e procura por tratamento; Não é só o SUS registrando mais | `figuras/figura1` a `figura5` |
| `02_perfil_sexo_idade` | Quem está sendo atendido | `figuras/figura6`, `figura7` |
| `03_conduta_aps` | Na atenção primária, o que acontece depois do atendimento | `tabelas/tabela1.tex` |
| `04_caps_pacientes` | No CAPS: gente nova chegando; o que aparece depois do diagnóstico | `figuras/figura8`, `tabelas/tabela2.tex` |

Os notebooks ficam salvos **sem saídas**; o que eles gravam são só as figuras e tabelas do artigo, em `../artigo/`.
Os números citados no texto aparecem na última célula de cada notebook.

## Dados (`data/raw/`, fora do git)

| Arquivo | Fonte | O que é |
|---|---|---|
| `atencao_primaria/sisab_aps.parquet` | SISAB, relatório de produção | Atendimentos individuais por mês, CID e recorte (total, sexo, faixa, sexo × faixa) |
| `atencao_primaria/sisab_conduta.parquet` | SISAB | Conduta ao fim do atendimento, por diagnóstico |
| `caps/sia_f63_registros.parquet` | DATASUS, SIA-PS (RAAS) | Pessoa × mês com algum F63 (código pseudonimizado) |
| `caps/sia_f63_historico.parquet` | DATASUS, SIA-PS (RAAS) | Todos os atendimentos no CAPS das pessoas que tiveram F63 |
| `caps/sia_perfil.parquet` | DATASUS, SIA-PS (RAAS) | Pacientes por mês, grupo, sexo e faixa etária (só totais) |
| `caps/sia_trajetorias.parquet` | DATASUS, SIA-PS (RAAS) | Todos os pacientes de saúde mental: pessoa × mês × grupo de CID (38,7 milhões de linhas) |
| `exposicao/google_trends_uf.parquet` | Google Trends | Índice de busca por apostas, por mês e UF |

Por enquanto, essas tabelas são uma cópia das geradas pelo pipeline da branch `saude-mental` de `thiagorr162/bets`
(pasta `../dados/*/processed/`). **A fazer:** script de download do zero (FTP do DATASUS, formulário do SISAB e
Google Trends), estimado em 2 a 4 horas de execução.

Os dados por pessoa nunca vão para o git: são dado de saúde (LGPD), com código de paciente pseudonimizado. Só saem
agregados, com contagens abaixo de 5 suprimidas.

## Formato das figuras e tabelas (normas da CSP)

`src/util.py` aplica as normas de `../csp_normas_formato.md`:
- figuras em PNG com 300 dpi (RGB) para a submissão, e SVG/EPS (vetor gerado pelo código) para depois do aceite;
  largura de até 17 cm; sem título na imagem; linhas diferenciadas só pela cor; fonte Times New Roman (ou Liberation
  Serif, que tem as mesmas métricas);
- tabelas com Times 9, um dado por célula, sem células mescladas, largura de até 17 cm.

Outros arquivos: `src/config.py` (caminhos, períodos e códigos CID) e `src/util.py` (formatação de números, figuras e
tabelas).
