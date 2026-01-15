import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO INICIAL (BARRA LATERAL SEMPRE EXPANDIDA)
st.set_page_config(
    page_title="KERIGMA | Exclusivo Mídia", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicialização de estados
if 'tela' not in st.session_state:
    st.session_state.tela = "home"
if 'membro_autenticado' not in st.session_state:
    st.session_state.membro_autenticado = False

ARQUIVO_ATIVAS = "chaves_ativas.txt"

if not os.path.exists(ARQUIVO_ATIVAS):
    with open(ARQUIVO_ATIVAS, "w") as f: f.write("")

# 2. FUNÇÕES
def listar_chaves():
    with open(ARQUIVO_ATIVAS, "r") as f: return f.read().splitlines()

def salvar_chave(chave):
    with open(ARQUIVO_ATIVAS, "a") as f: f.write(chave + "\n")

# 3. CSS PREMIUM (REMOVENDO A SETA E TRAVANDO A BARRA)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300;400;700;900&display=swap');
    
    /* ESCONDE O BOTÃO DE RECOLHER (A SETA) */
    [data-testid="sidebar-button"] {
        display: none !important;
    }
    
    /* REMOVE O HEADER PARA LIMPEZA TOTAL */
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
        border-bottom: none !important;
    }

    /* Fundo do App */
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    
    /* Títulos */
    .main-title { 
        font-family: 'Great Vibes', cursive; font-size: 5.5rem; color: #E50914; 
        text-align: center; margin-top: -2vh;
    }
    .sub-title {
        text-align: center; letter-spacing: 10px; color: #555; font-size: 0.8rem;
        text-transform: uppercase; margin-bottom: 30px;
    }

    /* Botões da Sidebar */
    section[data-testid="stSidebar"] .stButton button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        width: 100% !important;
        border-radius: 8px !important;
        border: none !important;
        height: 48px !important;
        font-weight: bold !important;
        margin-bottom: 10px;
    }

    /* Barra Lateral Fixa */
    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 2px solid #E50914 !important;
        min-width: 280px !important;
    }

    /* Estilo dos Cards */
    .card-janela {
        background: rgba(20, 20, 20, 0.9);
        border: 1px solid #E50914;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(229, 9, 20, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL (FIXA E SEM SETA)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("🏠 HOME"):
        st.session_state.tela = "home"
        st.rerun()
        
    if st.button("🔴 ÁREA DE MEMBROS"):
        st.session_state.tela = "login_membro"
        st.rerun()
        
    if st.button("⚙️ ACESSO ADMIN"):
        st.session_state.tela = "login_admin"
        st.rerun()
    
    st.write("---")
    st.markdown("<p style='text-align:center; color:#333; font-size:10px;'>V 1.0 | MAANAIM DIGITAL</p>", unsafe_allow_html=True)

# 5. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 class="main-title">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Digital Media Hub</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        chave = st.text_input("", placeholder="INSIRA SUA CHAVE SAGRADA", type="password")
        if st.button("ENTRAR NO MAANAIM"):
            if chave == "55420":
                st.session_state.tela = "master"
                st.rerun()
            elif chave in listar_chaves():
                st.session_state.tela = "membro"
                st.rerun()

elif st.session_state.tela == "login_admin":
    st.markdown("<h2 style='text-align:center; color:#E50914;'>RESTRITO: LIDERANÇA</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        senha = st.text_input("Senha Admin", type="password")
        if st.button("ACESSAR PAINEL"):
            if senha == "55420":
                st.session_state.tela = "master"
                st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>PAINEL MASTER</h1>", unsafe_allow_html=True)
    st.markdown('<div class="card-janela">', unsafe_allow_html=True)
    if st.button("✨ GERAR NOVA CHAVE PARA MEMBRO"):
        nova = "".join([str(random.randint(0, 9)) for _ in range(10)])
        salvar_chave(nova)
        st.success(f"Chave Gerada: {nova}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("### Chaves Ativas")
    st.json(listar_chaves())

elif st.session_state.tela == "login_membro":
    st.markdown("<h2 style='text-align:center; color:#E50914;'>VALIDAÇÃO DE MEMBRO</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        chave_m = st.text_input("Sua Chave", type="password")
        if st.button("VALIDAR"):
            if chave_m in listar_chaves() or chave_m == "55420":
                st.session_state.tela = "membro"
                st.rerun()

elif st.session_state.tela == "membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>CONTEÚDO EXCLUSIVO</h1>", unsafe_allow_html=True)
