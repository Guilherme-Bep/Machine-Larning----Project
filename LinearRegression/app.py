import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

tabela = pd.read_csv("pizzas.csv")

modelo = LinearRegression()

x = tabela[["diametro"]] 
y = tabela[["preco"]]

modelo.fit(x, y)

st.title("Prevendo o valor de uma pizza")
st.divider()

diametro = st.number_input("Digite o tamanho do diametro da pizza")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com diâmetro de {diametro} cm é de R$ {preco_previsto:.2f}.")

    st.balloons()