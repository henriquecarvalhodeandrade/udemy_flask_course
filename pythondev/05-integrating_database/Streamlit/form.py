import streamlit as st
import dados

st.title("Filmes")

nome = st.text_input("Nome do filme: ")
ano = st.number_input("Ano do filme: ", min_value=2010, max_value=2024)
nota = st.slider("Nota do filme: ", min_value=0.0, max_value=10.0)


if st.button('Adicionar'):
    dados.insert_data(nome, ano, nota)
    st.success('Filme Cadastrado')

filmes = dados.view_data()
st.header('Lista de Filmes')
st.table(filmes)