import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO INICIAL
st.set_page_config(
    page_title="KERIGMA | Exclusivo Mídia", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicialização de estados
if 'tela' not in st.session_state:
    st.session_state.tela = "home"
if 'chave_gerada' not in st.session_state:
    st.session_state.chave_gerada = ""

ARQUIVO_ATIVAS = "chaves_ativas.txt"

if not os.path.exists(ARQUIVO_ATIVAS):
    with open(ARQUIVO_ATIVAS, "w") as f: f.write("")

# 2. FUNÇÕES
def listar_chaves():
    if os.path.exists(ARQUIVO_ATIVAS):
        with open(ARQUIVO_ATIVAS, "r") as f: return f.read().splitlines()
    return []

def salvar_chave(chave):
    with open(ARQUIVO_ATIVAS, "a") as f: f.write(chave + "\n")

# 3. CSS PREMIUM
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;900&display=swap');
    
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        height: 48px !important;
    }
    
    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 2px solid #E50914 !important;
    }

    .master-container {
        background-color: #111;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #222;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME", use_container_width=True):
        st.session_state.tela = "home"
        st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS", use_container_width=True):
        st.session_state.tela = "login_membro"
        st.rerun()
    if st.button("⚙️ ACESSO ADMIN", use_container_width=True):
        st.session_state.tela = "login_admin"
        st.rerun()

# 5. LÓGICA DE TELAS (CORRIGIDA)

# --- TELA HOME ---
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-family:serif; font-size:4rem; color:#E50914; text-align:center;">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        entrada = st.text_input("ACESSO", placeholder="CHAVE SAGRADA", type="password")
        if st.button("ENTRAR", use_container_width=True):
            if entrada == "55420":
                st.session_state.tela = "master"
                st.rerun()
            elif entrada in listar_chaves():
                st.session_state.tela = "membro"
                st.rerun()

# --- TELA LOGIN ADMIN ---
elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>AUTENTICAÇÃO ADMIN</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        senha_adm = st.text_input("SENHA DE ACESSO MASTER", type="password")
        if st.button("CONFIRMAR LIDERANÇA", use_container_width=True):
            if senha_adm == "55420":
                st.session_state.tela = "master"
                st.rerun()
            else:
                st.error("Senha Master Incorreta.")

# --- TELA PAINEL MASTER ---
elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>PAINEL MASTER</h1>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        st.markdown('<div class="master-container">', unsafe_allow_html=True)
        if st.button("✨ GERAR NOVA CHAVE", use_container_width=True):
            nova_chave = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova_chave)
            st.session_state.chave_gerada = nova_chave
            
        if st.session_state.chave_gerada:
            st.write("---")
            st.markdown("<p style='color:#E50914; font-weight:bold;'>CHAVE PARA CÓPIA:</p>", unsafe_allow_html=True)
            st.code(st.session_state.chave_gerada, language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("#### CHAVES ATIVAS")
        st.code("\n".join(listar_chaves()), language="text")

# --- OUTRAS TELAS ---
elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    # Lógica de login de membro aqui...
