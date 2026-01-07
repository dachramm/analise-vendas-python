import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("📊 Dashboard de Vendas")

# carregar dados
conn = sqlite3.connect("vendas.db")
df = pd.read_sql("SELECT * FROM vendas", conn)
conn.close()

# filtros
categoria = st.selectbox(
    "Selecione a categoria",
    ["Todas"] + sorted(df["categoria"].unique().tolist())
)

if categoria != "Todas":
    df = df[df["categoria"] == categoria]

# métricas
total_faturamento = df["faturamento"].sum()
total_vendas = df["quantidade"].sum()

col1, col2 = st.columns(2)
col1.metric("💰 Faturamento Total", f"R$ {total_faturamento:,.2f}")
col2.metric("📦 Total de Itens Vendidos", total_vendas)

# gráfico
fig = px.bar(
    df.groupby("produto", as_index=False)["faturamento"].sum(),
    x="produto",
    y="faturamento",
    title="Faturamento por Produto"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df)
