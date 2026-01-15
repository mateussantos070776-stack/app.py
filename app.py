import streamlit as st
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="KERIGMA MAANAIM | Hub Oficial",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. LOGICA DE PERSISTÊNCIA DAS CHAVES
ARQUIVO_USADAS = "chaves_usadas.txt"

if not os.path.exists(ARQUIVO_USADAS):
    with open(ARQUIVO_USADAS, "w") as f:
        f.write("")

def carregar_chaves_usadas():
    with open(ARQUIVO_USADAS, "r") as f:
        return f.read().splitlines()

def registrar_chave_usada(chave):
    with open(ARQUIVO_USADAS, "a") as f:
        f.write(chave + "\n")

CHAVES_MESTRAS = [
    "5294017386", "1084739522", "8472016493", "3950284716", "6621049385",
    "2173958404", "9048217362", "4539102877", "7816402931", "1394857209"
]

# 3. CSS PREMIUM (CORRIGINDO O TOPO BRANCO E MARGENS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;900&display=swap');
    
    /* Remove a barra branca superior e ajusta o preenchimento */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
        max-width: 100%;
    }
    
    /* Esconde o header padrão do Streamlit que causa a linha branca */
    header {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}

    .stApp { 
        background-color: #050505; 
        color: #f5f5f5; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    /* Estilização da Sidebar conforme a imagem */
    [data-testid="stSidebar"] { 
        background-color: #0a0a0a !important; 
        border-right: 2px solid #E50914 !important;
        width: 300px !important;
    }

    .main-title { 
        font-weight: 900; 
        font-size: 5rem; 
        color: #E50914; 
        text-transform: uppercase; 
        text-align: center; 
        margin-top: 10vh;
        letter-spacing: -2px;
    }

    .tagline {
        font-size: 1.2rem;
        color: #888;
        text-align: center;
        letter-spacing: 15px;
        text-transform: uppercase;
        margin-top: -15px;
    }

    /* Estilo do botão Validar Credencial */
    div.stButton > button { 
        background-color: #E50914 !important; 
        color: white !important; 
        font-weight: 700 !important; 
        width: 100%; 
        border: none !important; 
        border-radius: 8px !important; 
        height: 50px; 
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

if 'logado' not in st.session_state:
    st.session_state.logado = False

# 4. SIDEBAR DE ACESSO
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#E50914; font-size: 1.5rem;'>SISTEMA DE ACESSO</h2>", unsafe_allow_html=True)
    st.write("---")
    
    if not st.session_state.logado:
        st.markdown("### 🔒 Integrantes")
        chave_input = st.text_input("Chave de 10 dígitos", type="password", placeholder="Insira sua chave única")
        
        if st.button("VALIDAR CREDENCIAL"):
            usadas = carregar_chaves_usadas()
            if chave_input in usadas:
                st.error("Chave já utilizada.")
            elif chave_input in CHAVES_MESTRAS:
                registrar_chave_usada(chave_input)
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Chave inválida.")
    else:
        st.success("SESSÃO ATIVA")
        if st.button("FINALIZAR"):
            st.session_state.logado = False
            st.rerun()

# 5. ÁREA PRINCIPAL
if not st.session_state.logado:
    st.markdown('<h1 class="main-title">KERIGMA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Digital Media Hub</p>', unsafe_allow_html=True)
    st.write("##")
    st.write("---")
    st.markdown("<p style='text-align:center; color:#444; font-size: 1rem;'>Acesse a barra lateral para validar seu acesso restrito.</p>", unsafe_allow_html=True)
else:
    st.markdown('<h1 style="color:#E50914; font-weight:900;">PAINEL DE PRODUÇÃO</h1>', unsafe_allow_html=True)
    st.write("Acesso autorizado.")
