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
if 'membro_autenticado' not in st.session_state:
    st.session_state.membro_autenticado = False

PASTA_GALERIA = "galeria_kerigma"
ARQUIVO_ATIVAS = "chaves_ativas.txt"

if not os.path.exists(PASTA_GALERIA):
    os.makedirs(PASTA_GALERIA)
if not os.path.exists(ARQUIVO_ATIVAS):
    with open(ARQUIVO_ATIVAS, "w") as f: f.write("")

# 2. FUNÇÕES
def listar_chaves():
    with open(ARQUIVO_ATIVAS, "r") as f: return f.read().splitlines()

def salvar_chave(chave):
    with open(ARQUIVO_ATIVAS, "a") as f: f.write(chave + "\n")

# 3. CSS PREMIUM (ESTILO DA SETA PERSONALIZADO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300;400;700;900&display=swap');
    
    /* REMOVE A LINHA DO TOPO */
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
        border-bottom: none !important;
    }

    /* CUSTOMIZAÇÃO DA SETA (SVG): FUNDO BRANCO REDONDO E SETA VERMELHA */
    button[kind="headerNoContext"] svg {
        fill: #E50914 !important; /* Cor da seta */
        background-color: white !important; /* Fundo redondo */
        border-radius: 50% !important;
        padding: 2px !important;
    }

    /* Fundo do App */
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    
    /* Títulos */
    .main-title { 
        font-family: 'Great Vibes', cursive; font-size: 5.5rem; color: #E50914; 
        text-align: center; margin-top: 0vh;
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
        height: 45px !important;
        font-weight: bold !important;
    }

    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 1px solid rgba(229, 9, 20, 0.2) !important; 
    }

    /* Estilo dos Cards */
    .card-janela {
        background: rgba(20, 20, 20, 0.8);
        border: 1px solid #E50914;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA</h2>", unsafe_allow_html=True)
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

# 5. LÓGICA DE TELAS

# TELA HOME
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

# TELA LOGIN ADMIN
elif st.session_state.tela == "login_admin":
    st.markdown("<h2 style='text-align:center; color:#E50914;'>RESTRITO: LIDERANÇA</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        senha = st.text_input("Senha Admin", type="password")
        if st.button("ACESSAR PAINEL"):
            if senha == "55420":
                st.session_state.tela = "master"
                st.rerun()

# TELA PAINEL MASTER
elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>PAINEL MASTER</h1>", unsafe_allow_html=True)
    st.markdown('<div class="card-janela">', unsafe_allow_html=True)
    if st.button("✨ GERAR NOVA CHAVE PARA MEMBRO"):
        nova = "".join([str(random.randint(0, 9)) for _ in range(10)])
        salvar_chave(nova)
        st.success(f"Chave Gerada: {nova}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("### Chaves Disponíveis")
    st.json(listar_chaves())

# TELA LOGIN MEMBRO
elif st.session_state.tela == "login_membro":
    st.markdown("<h2 style='text-align:center; color:#E50914;'>VALIDAÇÃO DE MEMBRO</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        chave_m = st.text_input("Sua Chave", type="password")
        if st.button("VALIDAR"):
            if chave_m in listar_chaves() or chave_m == "55420":
                st.session_state.tela = "membro"
                st.rerun()

# TELA MEMBRO
elif st.session_state.tela == "membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>CONTEÚDO EXCLUSIVO</h1>", unsafe_allow_html=True)
