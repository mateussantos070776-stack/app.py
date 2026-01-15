import streamlit as st
import os
import random
from PIL import Image
import io
from datetime import datetime

# 1. CONFIGURAÇÃO INICIAL E SESSION STATE
st.set_page_config(page_title="KERIGMA | Exclusivo Mídia", layout="wide")

# Inicialização de estados para navegação e segurança
if 'tela' not in st.session_state:
    st.session_state.tela = "home"
if 'sub_view' not in st.session_state:
    st.session_state.sub_view = None
if 'membro_autenticado' not in st.session_state:
    st.session_state.membro_autenticado = False

PASTA_GALERIA = "galeria_kerigma"
ARQUIVO_ATIVAS = "chaves_ativas.txt"
ARQUIVO_USADOS = "chaves_usadas.txt"

# Persistência de arquivos e pastas
if not os.path.exists(PASTA_GALERIA):
    os.makedirs(PASTA_GALERIA)

for arq in [ARQUIVO_ATIVAS, ARQUIVO_USADOS]:
    if not os.path.exists(arq):
        with open(arq, "w") as f: f.write("")

# 2. FUNÇÕES DE SUPORTE
def listar_chaves(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f: return f.read().splitlines()
    return []

def salvar_chave(chave, arquivo):
    with open(arquivo, "a") as f: f.write(chave + "\n")

# 3. CSS PREMIUM (ESTÉTICA MAANAIM)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300;400;700;900&display=swap');
    
    header {visibility: hidden !important;}
    
    .stApp { 
        background: radial-gradient(circle at center, #0f0f0f 0%, #050505 100%);
        color: white; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    .main-title { 
        font-family: 'Great Vibes', cursive; 
        font-weight: 400; 
        font-size: 6.5rem; 
        color: #E50914; 
        text-align: center; 
        text-shadow: 2px 2px 15px rgba(229, 9, 20, 0.3);
        margin-top: 5vh;
        margin-bottom: -10px;
    }

    .sub-title {
        text-align: center; 
        letter-spacing: 15px; 
        color: #555; 
        font-weight: 300;
        margin-bottom: 40px;
        font-size: 0.8rem;
        text-transform: uppercase;
    }

    /* Estilo dos Botões Vermelhos */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(229, 9, 20, 0.2);
        transition: all 0.4s ease;
        display: block;
        margin: 0 auto;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(229, 9, 20, 0.4);
    }

    /* Botões na Barra Lateral */
    [data-testid="stSidebar"] div.stButton > button {
        width: 100% !important;
        max-width: 250px !important;
        height: 45px !important;
        margin-bottom: 15px;
    }

    /* Estilo dos Cards e Inputs */
    .card-janela {
        background: linear-gradient(145deg, rgba(30, 30, 30, 0.6) 0%, rgba(10, 10, 10, 0.8) 100%);
        border: 1px solid rgba(229, 9, 20, 0.1);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 10px;
    }
    
    .card-janela:hover { border-color: #E50914; }
    .card-janela h3 { color: #E50914; font-weight: 900; letter-spacing: 2px; margin-bottom: 10px; }

    div[data-testid="stTextInput"] input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 10px !important;
        text-align: center;
    }

    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 1px solid rgba(229, 9, 20, 0.2) !important; 
    }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL (SIDEBAR)
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#E50914; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # Botão Home no topo
    if st.button("🏠 HOME"):
        st.session_state.tela = "home"
        st.session_state.sub_view = None
        st.session_state.membro_autenticado = False
        st.rerun()

    if st.button("🔴 ÁREA DE MEMBROS"):
        st.session_state.tela = "login_membro"
        st.rerun()

    if st.button("⚙️ ACESSO ADMIN"):
        st.session_state.tela = "login_admin"
        st.rerun()

    st.write("---")

# 5. LÓGICA DE TELAS

# TELA: HOME
if st.session_state.tela == "home":
    st.markdown('<div style="height: 12vh;"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Digital Media Hub</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        chave_membro = st.text_input("", placeholder="INSIRA SUA CHAVE SAGRADA", type="password")
        if st.button("ENTRAR NO MAANAIM"):
            ativas = listar_chaves(ARQUIVO_ATIVAS)
            if chave_membro == "55420":
                st.session_state.tela = "master"
                st.rerun()
            elif chave_membro in ativas:
                st.session_state.membro_autenticado = True
                st.session_state.tela = "membro"
                st.rerun()
            else:
                st.error("Chave inválida.")

# TELA: LOGIN ADMIN
elif st.session_state.tela == "login_admin":
    st.markdown('<div style="height: 15vh;"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#E50914;'>ACESSO RESTRITO LIDERANÇA</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        senha_admin = st.text_input("Insira a Senha Administrativa", type="password")
        if st.button("AUTENTICAR MASTER"):
            if senha_admin == "55420":
                st.session_state.tela = "master"
                st.rerun()
            else:
                st.error("Senha Administrativa Incorreta.")

# TELA: LOGIN MEMBRO
elif st.session_state.tela == "login_membro":
    st.markdown('<div style="height: 15vh;"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#E50914;'>VALIDAÇÃO DE INTEGRANTE</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        chave_esc = st.text_input("Chave para Escalas & Presença", type="password")
        if st.button("ACESSAR ESCALAS"):
            ativas = listar_chaves(ARQUIVO_ATIVAS)
            if chave_esc in ativas or chave_esc == "55420":
                st.session_state.membro_autenticado = True
                st.session_state.tela = "escalas"
                st.rerun()
            else:
                st.error("Acesso negado.")

# TELA: ESCALAS & PRESENÇA
elif st.session_state.tela == "escalas":
    if not st.session_state.membro_autenticado:
        st.session_state.tela = "login_membro"
        st.rerun()
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ESCALAS & PRESENÇA</h1>", unsafe_allow_html=True)
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.markdown('<div class="card-janela"><h3>📅 Escala</h3><p>Culto Domingo - 19:00</p></div>', unsafe_allow_html=True)
    with col_e2:
        st.markdown('<div class="card-janela"><h3>🙋 Confirmar</h3></div>', unsafe_allow_html=True)
        nome = st.text_input("Nome")
        if st.button("ENVIAR"): st.success("Registrado!")

# TELA: PAINEL MASTER
elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>PAINEL MASTER</h1>", unsafe_allow_html=True)
    col_adm1, col_adm2 = st.columns(2)
    with col_adm1:
        st.markdown('<div class="card-janela">', unsafe_allow_html=True)
        if st.button("✨ GERAR NOVA CHAVE"):
            nova = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova, ARQUIVO_ATIVAS)
            st.success(f"CHAVE GERADA: {nova}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_adm2:
        st.subheader("CHAVES ATIVAS")
        chaves = listar_chaves(ARQUIVO_ATIVAS)
        for c in chaves: st.code(c)

# TELA: EXCLUSIVO MÍDIA
elif st.session_state.tela == "membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>EXCLUSIVO MÍDIA</h1>", unsafe_allow_html=True)
    titulos = ["📸 FOTOS", "🎥 VÍDEOS", "🎨 ARTES", "📝 ROTEIROS", "🎵 ÁUDIOS", "🗓️ AGENDA"]
    chaves_btn = ["btn_f", "btn_v", "btn_a", "btn_r", "btn_au", "btn_ag"]
    for i in range(2):
        cols = st.columns(3)
        for j in range(3):
            idx = (i * 3) + j
            with cols[j]:
                st.markdown(f'<div class="card-janela" style="height:220px;"><h3>{titulos[idx]}</h3></div>', unsafe_allow_html=True)
                if st.button("ACESSAR", key=chaves_btn[idx]):
                    if titulos[idx] == "📸 FOTOS": st.session_state.sub_view = "fotos"
