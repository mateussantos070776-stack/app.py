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

# 3. CSS PREMIUM (PAINEL MASTER E BOTÕES FIXOS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300;400;700;900&display=swap');
    
    /* REMOVE HEADER E SETA */
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    
    /* ESTILO DOS BOTÕES (FIXANDO A COR VERMELHA) */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        transition: none !important; /* Remove transição de cor */
    }
    
    div.stButton > button:hover, div.stButton > button:active, div.stButton > button:focus {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 0 15px rgba(229, 9, 20, 0.4) !important;
    }

    /* BARRA LATERAL */
    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 2px solid #E50914 !important;
        min-width: 280px !important;
    }

    /* CARD DO PAINEL MASTER */
    .master-card {
        background: rgba(15, 15, 15, 0.9);
        border: 2px solid #E50914;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin-top: 20px;
    }

    .chave-display {
        font-size: 2.5rem;
        color: #E50914;
        font-weight: 900;
        letter-spacing: 5px;
        margin: 20px 0;
        text-shadow: 0 0 10px rgba(229, 9, 20, 0.5);
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
    st.write("---")

# 5. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-family:\'Great Vibes\'; font-size:5rem; color:#E50914; text-align:center;">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        chave = st.text_input("", placeholder="CHAVE SAGRADA", type="password")
        if st.button("ENTRAR", use_container_width=True):
            if chave == "55420":
                st.session_state.tela = "master"
                st.rerun()
            elif chave in listar_chaves():
                st.session_state.tela = "membro"
                st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>PAINEL MASTER</h1>", unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns([1, 4, 1])
    with col_b:
        st.markdown('<div class="master-card">', unsafe_allow_html=True)
        st.write("### GERADOR DE ACESSO")
        
        if st.button("✨ GERAR NOVA CHAVE", use_container_width=True):
            nova = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova)
            st.session_state.chave_gerada = nova
            
        if st.session_state.chave_gerada:
            st.markdown(f'<div class="chave-display">{st.session_state.chave_gerada}</div>', unsafe_allow_html=True)
            st.success("Chave registrada com sucesso no sistema!")
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("---")
        st.write("### LISTA DE CHAVES ATIVAS")
        chaves = listar_chaves()
        if chaves:
            st.code("\n".join(chaves), language="text")
        else:
            st.info("Nenhuma chave gerada ainda.")

# (As outras telas login_membro, membro, etc continuam seguindo a mesma lógica)
