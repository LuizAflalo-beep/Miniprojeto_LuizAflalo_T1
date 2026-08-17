import pandas as pd
import csv
from pathlib import Path

# Arquivo da base
ARQUIVO = Path("Base Varejo.csv")

# Verifica se o arquivo existe antes de começar
if not ARQUIVO.exists():
    raise FileNotFoundError("O arquivo Base Varejo.csv não foi encontrado.")

# 1. Importação dos dados
df = pd.read_csv(ARQUIVO, sep=";")

print("=" * 60)
print("ANÁLISE EXPLORATÓRIA - BASE VAREJO")
print("=" * 60)

print(f"\nNúmero de registros: {len(df):,}")
print(f"Número de colunas: {len(df.columns)}")
print("\nColunas:")
print(df.columns.tolist())

print("\nTipos de dados:")
print(df.dtypes)

# Leitura com csv.DictReader para atender ao requisito de manipulação de CSV
with open(ARQUIVO, "r", encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    primeira_linha = next(leitor, None)

print("\nPrimeira linha da base:")
print(primeira_linha)

# 2. Verificação de problemas nos dados
print("Iniciando verificação de qualidade dos dados...")
print("\n" + "=" * 60)
print("VERIFICAÇÃO DOS DADOS")
print("=" * 60)

print("\nValores nulos por coluna:")
print(df.isna().sum())

duplicatas = df.duplicated().sum()
print(f"\nDuplicatas encontradas: {duplicatas:,}")

# Verifica se existem datas inválidas
datas = pd.to_datetime(df["DATA"], dayfirst=True, errors="coerce")
print(f"Datas inválidas: {datas.isna().sum():,}")

# Verifica categorias sem informação
categorias_nd = (df["PR_CAT"].astype(str).str.strip() == "#N/D").sum()
print(f"Categorias com #N/D: {categorias_nd:,}")

# CO_ID pode aparecer em várias linhas porque uma compra pode ter vários produtos
compras_unicas = df["CO_ID"].nunique()
print(f"Compras únicas: {compras_unicas:,}")

# 3. Limpeza
print("Realizando limpeza dos dados...")
print("\n" + "=" * 60)
print("LIMPEZA DOS DADOS")
print("=" * 60)

df_limpo = df.copy()

# Remove colunas que estão completamente vazias
colunas_vazias = [
    coluna for coluna in df_limpo.columns
    if df_limpo[coluna].isna().all()
]
df_limpo = df_limpo.drop(columns=colunas_vazias)

print("Colunas vazias removidas:", colunas_vazias)

# Remove espaços extras dos textos
colunas_texto = df_limpo.select_dtypes(include="object").columns
for coluna in colunas_texto:
    df_limpo[coluna] = df_limpo[coluna].astype("string").str.strip()

# Substitui categorias vazias ou #N/D
def tratar_categoria(valor):
    if pd.isna(valor) or str(valor).strip() in ("", "#N/D"):
        return "Sem Categoria"
    return str(valor).strip()

df_limpo["PR_CAT"] = df_limpo["PR_CAT"].apply(tratar_categoria)

# Converte a data para o tipo datetime
df_limpo["DATA"] = pd.to_datetime(
    df_limpo["DATA"],
    dayfirst=True,
    errors="coerce"
)

# Garante que as principais colunas numéricas sejam numéricas
for coluna in ["CO_ID", "CL_ID", "CL_EC", "CL_FHL", "PR_ID"]:
    df_limpo[coluna] = pd.to_numeric(df_limpo[coluna], errors="coerce")

# Remove registros com informação ausente em campos essenciais
colunas_essenciais = ["DATA", "CO_ID", "CL_ID", "CL_FHL", "PR_ID", "PR_CAT"]
antes_nulos = len(df_limpo)
df_limpo = df_limpo.dropna(subset=colunas_essenciais)
print(f"Registros removidos por nulos: {antes_nulos - len(df_limpo):,}")

# Remove somente linhas completamente duplicadas
antes_duplicatas = len(df_limpo)
df_limpo = df_limpo.drop_duplicates()
print(f"Duplicatas removidas: {antes_duplicatas - len(df_limpo):,}")

# 4. Estatísticas do número de filhos
print("Calculando as estatísticas descritivas...")
print("\n" + "=" * 60)
print("ESTATÍSTICAS - NÚMERO DE FILHOS")
print("=" * 60)

filhos = df_limpo["CL_FHL"]

print(f"Contagem: {filhos.count():,}")
print(f"Média: {filhos.mean():.2f}")
print(f"Mediana: {filhos.median():.2f}")
print(f"Desvio padrão: {filhos.std():.2f}")
print(f"Moda: {filhos.mode().tolist()}")
print(f"Mínimo: {filhos.min()}")
print(f"1º Quartil: {filhos.quantile(0.25):.2f}")
print(f"2º Quartil: {filhos.quantile(0.50):.2f}")
print(f"3º Quartil: {filhos.quantile(0.75):.2f}")
print(f"Máximo: {filhos.max()}")

# 5. Agrupamentos
print("\n" + "=" * 60)
print("AGRUPAMENTOS")
print("=" * 60)

# Agrupamento 1: gênero
por_genero = (
    df_limpo.groupby("CL_GENERO")
    .size()
    .sort_values(ascending=False)
)
print("\nRegistros por gênero:")
print(por_genero)

# Agrupamento 2: categoria
por_categoria = (
    df_limpo.groupby("PR_CAT")
    .size()
    .sort_values(ascending=False)
)
print("\nRegistros por categoria:")
print(por_categoria)

# Agrupamento 3: segmento
por_segmento = (
    df_limpo.groupby("CL_SEG")
    .size()
    .sort_values(ascending=False)
)
print("\nRegistros por segmento:")
print(por_segmento)

# 6. Resumo final
print("\n" + "=" * 60)
print("CONCLUSÕES")
print("=" * 60)

print(f"1. A base passou de {len(df):,} para {len(df_limpo):,} registros após a limpeza.")
print(f"2. Foram encontradas {duplicatas:,} duplicatas completas.")
print(f"3. A categoria com mais registros foi {por_categoria.index[0]}.")
print(f"4. O gênero com mais registros foi {por_genero.index[0]}.")
print(f"5. O segmento com mais registros foi {por_segmento.index[0]}.")
print(f"6. O número médio de filhos foi {filhos.mean():.2f}, com mediana {filhos.median():.0f}.")

# Salva a base depois da limpeza
df_limpo.to_csv("df_limpo.csv", index=False, encoding="utf-8-sig")

print("\nBase limpa salva como: df_limpo.csv")
print("Projeto finalizado!")
