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
if 'membro_logado' not in st.session_state:
    st.session_state.membro_logado = False

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

# 3. CSS PREMIUM (CARDS E ESTILO KERIGMA)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;900&display=swap');
    
    /* REMOVE ELEMENTOS PADRÃO */
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    
    /* BOTÕES FIXOS VERMELHOS */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        height: 48px !important;
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

    /* ESTILO DAS JANELAS (CARDS) DE MEMBROS */
    .card-membro {
        background: rgba(20, 20, 20, 0.9);
        border: 1px solid #333;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        transition: 0.3s;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }
    
    .card-membro:hover {
        border-color: #E50914;
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(229, 9, 20, 0.2);
    }

    .card-icon { font-size: 2.5rem; margin-bottom: 10px; }
    .card-title { font-weight: 900; color: #E50914; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL (SISTEMA KERIGMA)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME", use_container_width=True):
        st.session_state.tela = "home"
        st.session_state.membro_logado = False
        st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS", use_container_width=True):
        st.session_state.tela = "login_membro"
        st.rerun()
    if st.button("⚙️ ACESSO ADMIN", use_container_width=True):
        st.session_state.tela = "login_admin"
        st.rerun()

# 5. LÓGICA DE TELAS

# --- TELA HOME ---
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-family:serif; font-size:4rem; color:#E50914; text-align:center;">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        entrada = st.text_input("ACESSO RÁPIDO", placeholder="INSIRA SUA CHAVE SAGRADA", type="password")
        if st.button("ENTRAR NO MAANAIM", use_container_width=True):
            if entrada == "55420":
                st.session_state.tela = "master"
                st.rerun()
            elif entrada in listar_chaves():
                st.session_state.tela = "painel_membro"
                st.session_state.membro_logado = True
                st.rerun()

# --- TELA LOGIN ADMIN ---
elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>AUTENTICAÇÃO ADMIN</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        senha_adm = st.text_input("SENHA MASTER", type="password")
        if st.button("CONFIRMAR LIDERANÇA", use_container_width=True):
            if senha_adm == "55420":
                st.session_state.tela = "master"
                st.rerun()

# --- TELA LOGIN MEMBRO ---
elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>ACESSO DO MEMBRO</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<p style='text-align:center;'>Para acessar o conteúdo exclusivo, utilize sua chave de membro.</p>", unsafe_allow_html=True)
        chave_m = st.text_input("CHAVE DE ACESSO", type="password")
        if st.button("VALIDAR CHAVE", use_container_width=True):
            if chave_m in listar_chaves() or chave_m == "55420":
                st.session_state.tela = "painel_membro"
                st.session_state.membro_logado = True
                st.rerun()
            else:
                st.error("Chave inválida. Solicite uma nova à liderança.")

# --- TELA PAINEL DO MEMBRO (JANELAS) ---
elif st.session_state.tela == "painel_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Grid de Janelas (Cards)
    col_c1, col_c2 = st.columns(2)
    col_c3, col_c4 = st.columns(2)
    
    with col_c1:
        st.markdown("""<div class="card-membro"><div class="card-icon">📅</div><div class="card-title">Escalas</div><p>Consulte sua escala de serviço</p></div>""", unsafe_allow_html=True)
    with col_c2:
        st.markdown("""<div class="card-membro"><div class="card-icon">🏛️</div><div class="card-title">Dias de Culto</div><p>Horários e programações</p></div>""", unsafe_allow_html=True)
    with col_c3:
        st.markdown("""<div class="card-membro"><div class="card-icon">📢</div><div class="card-title">Avisos</div><p>Informações importantes da igreja</p></div>""", unsafe_allow_html=True)
    with col_c4:
        st.markdown("""<div class="card-membro"><div class="card-icon">🔥</div><div class="card-title">Eventos</div><p>Próximas programações Kerigma</p></div>""", unsafe_allow_html=True)

# --- TELA PAINEL MASTER ---
elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>PAINEL MASTER</h1>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        if st.button("✨ GERAR NOVA CHAVE", use_container_width=True):
            nova_chave = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova_chave)
            st.session_state.chave_gerada = nova_chave
            
        if st.session_state.chave_gerada:
            st.code(st.session_state.chave_gerada, language="text")
        
        st.write("#### CHAVES ATIVAS NO SISTEMA")
        st.code("\n".join(listar_chaves()), language="text")
