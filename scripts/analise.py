import pandas as pd

# carregar dados
df = pd.read_csv("vendas.csv")

print("\n📄 Dados brutos:")
print(df)

# criar coluna faturamento
df["faturamento"] = df["quantidade"] * df["preco"]

print("\n💰 Faturamento por linha:")
print(df)

# resumo geral
print("\n📊 Resumo estatístico:")
print(df.describe())

# faturamento por categoria
resumo_categoria = df.groupby("categoria")["faturamento"].sum()

print("\n🏷️ Faturamento por categoria:")
print(resumo_categoria)

# produto mais vendido (quantidade)
mais_vendido = df.groupby("produto")["quantidade"].sum().idxmax()
print("\n🔥 Produto mais vendido:", mais_vendido)
