# Título - Sistema de Vendas
# Seção Cadastrar vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Fone, Celular
    # Campo Quantidade
    # Campo Valor
    # Botão cadastrar venda
        # Quando eu clicar no botão -> adicionar a venda na tabela
# Seção Vendas Cadastradas
    # Tabela com as vendas
# seção dashboard
    # Card/métrica -> Faturamento total
    # Gráfico de barra/coluna -> Venda por vendedor
    # Gráficos de Pizza -> Venda por produto

# streamlit
# pandas
# plotly

# streamlit.authenticate serve para criar funções 

import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

# seção de cadastro de vendas
# st.navigation serve para criar uma barra de navegação (navbar)
# st.sidebar serve para criar uma barra lateral (sidebar)
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data", min_value="today")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# lógica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas) # diz a quantidade de linhas da tabela
    tabela_vendas.loc[ultima_linha] = nova_venda # adiciona a nova venda na última linha do banco de dados
    tabela_vendas.to_csv("vendas.csv", index=False) # atualiza a tabela sem os indices
    st.sucess("Venda cadastrada!") # exibe uma mensagem de sucesso no site 

# seção de visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

"""
id_venda = st.number_input()
botao_pesquisar = st.button
"""

# seção de dashboard
st.write("## Dashboard") 

# Card/métrica -> Faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}.:2f")

# Gráfico de barra/coluna -> Venda por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto") #color_discrete_map=[] permite dar as cores do gráfico
st.plotly_chart(grafico1) # exibe o gráfico no site, o gráfico.show() exibe apenas no terminal

# Gráficos de Pizza -> Venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico1)