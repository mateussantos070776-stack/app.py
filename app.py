import streamlit as st

# 1. CONFIGURAÇÃO E DESIGN (ESTILO NETFLIX)
st.set_page_config(page_title="Midia Kerigma Maanaim", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS CUSTOMIZADO PARA ESTILO NETFLIX
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}

    .netflix-logo {
        color: #E50914;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        letter-spacing: -2px;
        text-transform: uppercase;
    }

    .login-box {
        background-color: rgba(0, 0, 0, 0.75);
        padding: 40px;
        border-radius: 10px;
        border: 1px solid #333;
        max-width: 450px;
        margin: auto;
    }

    div.stButton > button {
        background-color: #E50914 !important;
        color: white !important;
        width: 100%;
        border-radius: 4px;
        border: none;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
    }

    .stTextInput input {
        background-color: #333 !important;
        color: white !important;
        border-radius: 4px !important;
        border: none !important;
        height: 50px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Link direto para a imagem do Google Drive 
# O ID do arquivo foi extraído do seu link: 1B8LjYZmHsjpyZPC96FaYAODskWrwOVJC
IMAGE_URL = "https://lh3.googleusercontent.com/d/1B8LjYZmHsjpyZPC96FaYAODskWrwOVJC"

if 'logado' not in st.session_state: st.session_state.logado = False

if not st.session_state.logado:
    # Título Estilo Netflix
    st.markdown('<div class="netflix-logo">MIDIA KERIGMA MAANAIM</div>', unsafe_allow_html=True)
    
    # Exibição da Imagem Proporcional 
    col_a, col_b, col_c = st.columns([1, 1.5, 1])
    with col_b:
        st.image(IMAGE_URL, use_container_width=True)
    
    # Card de Login
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.subheader("Entrar")
        email = st.text_input("Email ou número de telefone")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if email == "admin" and senha == "1234":
                st.session_state.logado = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.title("Bem-vindo à Midia Kerigma Maanaim")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
