import pandas as pd
import matplotlib.pyplot as plt

# carregar dados
df = pd.read_csv("vendas.csv")

# criar coluna faturamento
df["faturamento"] = df["quantidade"] * df["preco"]

# faturamento por categoria
resumo = df.groupby("categoria")["faturamento"].sum()

# gráfico de barras
resumo.plot(kind="bar", title="Faturamento por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.show()
