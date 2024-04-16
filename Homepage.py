import pandas as pd
import streamlit as st
import pygsheets
import os

# Configuração da página
#st.set_page_config(layout="wide") # original
st.set_page_config(layout="wide", page_title="Leste conecta")
st.subheader(':green[LESTE CONECTA]', divider='rainbow')
st.markdown('<h1 style="text-align: center; color: green;">Bem vindo a Leste Conecta!</h1><br>', unsafe_allow_html=True)
st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.header("CONSULTAR VIABILIDADE")
    st.link_button("VIABILIDADE", "https://www.lestetelecom.com.br/viabilidade")

with col2:
    st.header("CONSULTA FAQ")
    st.link_button("FAQ - LESTE", "https://www.lestetelecom.com.br/faq")

with col3:
    st.header("LESTE MOVEL")
    st.link_button("IR", "https://www.lestemovel.com.br/")

st.divider()
