import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# conectar ao banco
conn = sqlite3.connect("vendas.db")

# consulta SQL
query = """
SELECT categoria, SUM(faturamento) AS faturamento_total
FROM vendas
GROUP BY categoria
"""

df = pd.read_sql(query, conn)
conn.close()

print(df)

# gráfico
df.set_index("categoria")["faturamento_total"].plot(
    kind="bar",
    title="Faturamento por Categoria (SQL + Pandas)"
)

plt.xlabel("Categoria")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.show()
