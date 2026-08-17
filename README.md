# Mini-Projeto Avaliativo — Análise de Dados com Python

**Aluno:** Luiz Aflalo  
**Turma:** Analise_de_Dados_T1

## Objetivo

Realizar uma Análise Exploratória de Dados (AED) sobre uma base de varejo utilizando Python e pandas.

O projeto verifica a qualidade dos dados, realiza a limpeza e apresenta estatísticas e agrupamentos.

## Como executar

1. Abra esta pasta no VS Code.
2. Verifique se o arquivo `Base Varejo.csv` está na mesma pasta do script.
3. Abra o terminal do VS Code.
4. Execute:

```bash
python Miniprojeto_LuizAflalo_T1.py
```

O programa apresenta os resultados no terminal e gera o arquivo `df_limpo.csv`.

## Etapas realizadas

- Importação da base CSV.
- Verificação de registros, colunas e tipos.
- Identificação de valores nulos.
- Identificação de duplicatas.
- Verificação de datas inválidas.
- Tratamento de categorias com `#N/D`.
- Remoção de colunas completamente vazias.
- Conversão da coluna `DATA` para datetime.
- Remoção de duplicatas completas.
- Estatísticas da coluna de número de filhos.
- Agrupamento por gênero, categoria e segmento.
- Exportação da base limpa.

## ETL e qualidade dos dados

ETL significa Extract, Transform e Load.

**Extract (Extração):** os dados são carregados do arquivo `Base Varejo.csv`.

**Transform (Transformação):** os dados são verificados e tratados. São removidas colunas vazias, categorias sem informação são padronizadas, a data é convertida para datetime e duplicatas são removidas.

**Load (Carregamento):** a base tratada é salva como `df_limpo.csv`.

A qualidade dos dados é importante porque duplicidades, informações ausentes e tipos incorretos podem prejudicar os resultados de uma análise.

## Insights

1. A base possui 830.000 registros inicialmente e 733.447 após a remoção das duplicatas.
2. Foram encontradas 96.553 duplicatas completas.
3. Não foram identificadas datas inválidas.
4. A categoria ALIMENTOS apresentou a maior quantidade de registros.
5. O gênero F apresentou mais registros que o gênero M.
6. O número de filhos apresentou média de aproximadamente 1,15, mediana 0 e máximo 4.

## Reflexão final

A análise mostrou que a limpeza é uma etapa importante antes da utilização dos dados. Através do pandas foi possível identificar problemas, padronizar informações e criar uma base mais adequada para análises futuras.

Os agrupamentos também ajudaram a encontrar padrões na distribuição dos registros entre gêneros, categorias de produtos e segmentos de clientes.

## Sugestão de versionamento

Os commits podem demonstrar a evolução do projeto:

```bash
git add .
git commit -m "feat: adiciona base e estrutura inicial"

git add .
git commit -m "feat: adiciona verificacao e limpeza dos dados"

git add .
git commit -m "feat: adiciona estatisticas e agrupamentos"

git add .
git commit -m "docs: adiciona README e conclusoes"
```
Projeto desenvolvido por Luiz Aflalo como atividade avaliativa do Módulo 1 de Análise de Dados com Python.