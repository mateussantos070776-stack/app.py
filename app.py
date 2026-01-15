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
    
    /* BOTÃO QUE NÃO MUDA DE COR */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        height: 45px !important;
    }
    
    div.stButton > button:hover {
        box-shadow: 0 0 15px rgba(229, 9, 20, 0.4) !important;
        color: white !important;
    }

    /* BARRA LATERAL FIXA */
    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 2px solid #E50914 !important;
    }

    /* PAINEL MASTER */
    .master-card {
        background: rgba(20, 20, 20, 1);
        border: 1px solid #333;
        border-radius: 15px;
        padding: 30px;
        margin-bottom: 20px;
    }

    .label-chave {
        color: #E50914;
        font-weight: 900;
        font-size: 1.2rem;
        margin-bottom: 10px;
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

# 5. LÓGICA DE TELAS
if st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>PAINEL MASTER</h1>", unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns([1, 3, 1])
    
    with col_b:
        st.markdown('<div class="master-card">', unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-weight:700;'>GERADOR DE ACESSOS</p>", unsafe_allow_html=True)
        
        if st.button("✨ GERAR NOVA CHAVE", use_container_width=True):
            nova = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova)
            st.session_state.chave_gerada = nova
            
        if st.session_state.chave_gerada:
            st.write("---")
            st.markdown('<p class="label-chave">CHAVE GERADA:</p>', unsafe_allow_html=True)
            # Mostra a chave com o botão de copiar nativo do st.code
            st.code(st.session_state.chave_gerada, language="text")
            st.caption("Clique no ícone à direita da chave para copiar")
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("### LISTA DE CHAVES ATIVAS")
        chaves = listar_chaves()
        if chaves:
            # Lista compacta para visualização
            st.code("\n".join(chaves), language="text")
        else:
            st.info("Nenhuma chave no sistema.")

elif st.session_state.tela == "home":
    st.markdown('<h1 style="font-family:serif; font-size:4rem; color:#E50914; text-align:center;">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    # Restante da lógica da home...
