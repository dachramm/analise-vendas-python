import sqlite3
import pandas as pd

# carregar dados
df = pd.read_csv("vendas.csv")
df["faturamento"] = df["quantidade"] * df["preco"]

# criar conexão SQLite
conn = sqlite3.connect("vendas.db")

# salvar dados no banco
df.to_sql("vendas", conn, if_exists="replace", index=False)

print("📦 Dados salvos no banco SQLite")

# consultas SQL reais
query1 = """
SELECT categoria, SUM(faturamento) AS total_faturamento
FROM vendas
GROUP BY categoria
ORDER BY total_faturamento DESC
"""

query2 = """
SELECT produto, SUM(quantidade) AS total_vendido
FROM vendas
GROUP BY produto
ORDER BY total_vendido DESC
LIMIT 1
"""

df_categoria = pd.read_sql(query1, conn)
df_produto = pd.read_sql(query2, conn)

print("\n📊 Faturamento por categoria (SQL):")
print(df_categoria)

print("\n🔥 Produto mais vendido (SQL):")
print(df_produto)

conn.close()
