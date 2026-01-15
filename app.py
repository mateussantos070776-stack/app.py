import streamlit as st
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="KERIGMA MAANAIM | Hub Oficial",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. LOGICA DE PERSISTÊNCIA DAS CHAVES (Uso Único Permanente)
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

# Chaves mestras de 10 dígitos
CHAVES_MESTRAS = [
    "5294017386", "1084739522", "8472016493", "3950284716", "6621049385",
    "2173958404", "9048217362", "4539102877", "7816402931", "1394857209"
]

# 3. CSS PREMIUM (SEM IMAGEM, FOCO EM UI)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;900&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at 50% -20%, #1a1a1a 0%, #000000 100%); 
        color: #f5f5f5; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    [data-testid="stSidebar"] { 
        background-color: rgba(10, 10, 10, 0.98); 
        border-right: 1px solid #E50914; 
    }

    .main-title { 
        font-weight: 900; 
        font-size: 5rem; 
        color: #E50914; 
        text-transform: uppercase; 
        text-align: center; 
        margin-top: 15vh;
        background: linear-gradient(180deg, #ff1e1e 0%, #a80000 100%); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        filter: drop-shadow(0 0 15px rgba(229, 9, 20, 0.3));
    }

    .tagline {
        font-size: 1rem;
        color: #666;
        text-align: center;
        letter-spacing: 12px;
        text-transform: uppercase;
        margin-top: -10px;
    }

    div.stButton > button { 
        background: #E50914 !important; 
        color: white !important; 
        font-weight: 700 !important; 
        width: 100%; 
        border: none !important; 
        border-radius: 8px !important; 
        height: 50px; 
    }

    div.stButton > button:hover { 
        background: #ff1e2d !important; 
        box-shadow: 0 0 20px rgba(229,9,20,0.5) !important; 
    }
    </style>
    """, unsafe_allow_html=True)

if 'logado' not in st.session_state:
    st.session_state.logado = False

# 4. SIDEBAR DE ACESSO
with st.sidebar:
    st.markdown("<h3 style='text-align:center; color:#E50914;'>SISTEMA DE ACESSO</h3>", unsafe_allow_html=True)
    st.write("---")
    
    if not st.session_state.logado:
        st.markdown("### 🔒 Integrantes")
        chave_input = st.text_input("Chave de 10 dígitos", type="password", placeholder="Insira sua chave única")
        
        if st.button("VALIDAR CREDENCIAL"):
            usadas = carregar_chaves_usadas()
            
            if chave_input in usadas:
                st.error("Esta chave já foi utilizada.")
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
    st.markdown("<p style='text-align:center; color:#444;'>Acesse a barra lateral para validar seu acesso restrito.</p>", unsafe_allow_html=True)
else:
    # O conteúdo abaixo só aparece para quem validou a chave
    st.markdown('<h1 style="color:#E50914; font-weight:900;">PAINEL DE PRODUÇÃO</h1>', unsafe_allow_html=True)
    st.write("Sessão iniciada com sucesso. Esta chave de acesso agora foi permanentemente desativada.")
    
    tab1, tab2 = st.tabs(["🎥 Gestão de Vídeos", "👥 Comunidade"])
    with tab1:
        st.info("Repositório de mídias pronto para upload.")
        st.file_uploader("Upload Master", type=["mp4", "mov"])
