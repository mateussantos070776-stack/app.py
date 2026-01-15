import streamlit as st
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="KERIGMA MAANAIM", layout="wide")

# 2. LOGICA DE PERSISTÊNCIA (PARA A CHAVE NÃO FUNCIONAR APÓS ATUALIZAR)
ARQUIVO_USADAS = "chaves_usadas.txt"

# Cria o arquivo de registro caso ele não exista
if not os.path.exists(ARQUIVO_USADAS):
    with open(ARQUIVO_USADAS, "w") as f:
        f.write("")

def carregar_chaves_usadas():
    with open(ARQUIVO_USADAS, "r") as f:
        return f.read().splitlines()

def registrar_chave_usada(chave):
    with open(ARQUIVO_USADAS, "a") as f:
        f.write(chave + "\n")

# Lista de chaves originais
CHAVES_MESTRAS = [
    "5294017386", "1084739522", "8472016493", "3950284716", "6621049385",
    "2173958404", "9048217362", "4539102877", "7816402931", "1394857209"
]

# 3. INTERFACE E CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&display=swap');
    .stApp { background-color: #000; color: white; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #E50914; }
    .title { color: #E50914; font-size: 50px; font-weight: 900; text-align: center; }
    div.stButton > button { background-color: #E50914 !important; color: white !important; border-radius: 8px; width: 100%; height: 50px; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

if 'logado' not in st.session_state:
    st.session_state.logado = False

# 4. BARRA LATERAL (VALIDAÇÃO REAL)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914;'>ACESSO RESTRITO</h2>", unsafe_allow_html=True)
    st.write("---")
    
    if not st.session_state.logado:
        chave_input = st.text_input("Chave de 10 dígitos", type="password")
        
        if st.button("VERIFICAR CREDENCIAL"):
            usadas = carregar_chaves_usadas()
            
            if chave_input in usadas:
                st.error("❌ ESTA CHAVE JÁ FOI UTILIZADA E ESTÁ INVÁLIDA.")
            elif chave_input in CHAVES_MESTRAS:
                registrar_chave_usada(chave_input) # Grava no arquivo permanentemente
                st.session_state.logado = True
                st.success("Acesso Autorizado!")
                st.rerun()
            else:
                st.error("❌ CHAVE INCORRETA.")
    else:
        st.success("DISPOSITIVO AUTORIZADO")
        if st.button("SAIR"):
            st.session_state.logado = False
            st.rerun()

# 5. CONTEÚDO
if not st.session_state.logado:
    st.markdown('<h1 class="title">MIDIA KERIGMA MAANAIM</h1>', unsafe_allow_html=True)
    st.image("https://lh3.googleusercontent.com/d/1B8LjYZmHsjpyZPC96FaYAODskWrwOVJC", width=400)
    st.info("Sistema protegido. Insira uma chave de uso único na lateral para prosseguir.")
else:
    st.markdown('<h1 style="color:#E50914;">PAINEL DE MÍDIA INTEGRANTE</h1>', unsafe_allow_html=True)
    st.write("Bem-vindo. Esta sessão está ativa. Se você fechar o navegador, precisará de uma NOVA chave.")
    # Coloque aqui o seu conteúdo secreto (vídeos, cadastros, etc)
