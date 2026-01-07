import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# carregar dados
df = pd.read_csv("vendas.csv")

# criar faturamento
df["faturamento"] = df["quantidade"] * df["preco"]

# features e alvo
X = df[["quantidade", "preco"]]
y = df["faturamento"]

# dividir dados
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# previsões
y_pred = modelo.predict(X_test)

# avaliação
erro = mean_absolute_error(y_test, y_pred)

print("📉 Erro médio absoluto:", erro)
print("\nCoeficientes:")
print("Quantidade:", modelo.coef_[0])
print("Preço:", modelo.coef_[1])
