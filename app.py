import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DE TELA
st.set_page_config(page_title="KERIGMA | Member", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE ESTADOS ---
if 'tela' not in st.session_state: 
    st.session_state.tela = "home"

ARQUIVO_ATIVAS = "chaves_ativas.txt"

# --- FUNÇÕES DE SISTEMA ---
def listar_chaves():
    if os.path.exists(ARQUIVO_ATIVAS):
        with open(ARQUIVO_ATIVAS, "r") as f: 
            return [linha.strip() for linha in f.readlines()]
    return []

# 2. CSS REVISADO (FOCO EM REDUÇÃO DE TAMANHO E COMPACTAÇÃO)
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }

    /* Barra Lateral */
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #E50914 !important; }

    /* Centralizar o Grid */
    .main-container {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    /* Janelas de Opções Reduzidas (4x4 compactas) */
    .card-membro {
        background: #111;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 15px; /* Reduzido */
        text-align: center;
        aspect-ratio: 1 / 1;
        max-width: 200px; /* Limite de largura para não ficar gigante */
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        justify-content: center;
        transition: 0.3s;
    }
    
    .card-membro:hover { border-color: #E50914; background: #161616; }

    .t-membro { 
        color: #E50914; 
        font-weight: 800; 
        font-size: 0.9rem; /* Fonte menor */
        text-transform: uppercase; 
        margin-bottom: 10px; 
    }

    /* Botões Menores */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        width: 100% !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 0.7rem !important; /* Fonte do botão menor */
        height: 35px !important;
        text-transform: uppercase;
    }
    
    .stTextInput input { background-color: #111 !important; color: white !important; border: 1px solid #333 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME", key="nav_h"):
        st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS", key="nav_m"):
        st.session_state.tela = "login_membro"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN", key="nav_a"):
        st.session_state.tela = "login_admin"; st.rerun()

# 4. LÓGICA DE TELAS

if st.session_state.tela == "home":
    st.markdown('<h1 style="font-family:serif; font-size:4rem; color:#E50914; text-align:center; margin-top:80px;">Kerigma Maanaim</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1, 1])
    with col_login:
        chave = st.text_input("Insira sua Chave", type="password")
        if st.button("VALIDAR ACESSO"):
            if chave in listar_chaves() or chave == "55420":
                st.session_state.tela = "painel_membro"; st.rerun()
            else: st.error("Chave inválida.")

elif st.session_state.tela == "painel_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>CENTRAL DO MEMBRO</h1>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    
    # Grid de 4 janelas pequenas em uma única linha
    _, central_grid, _ = st.columns([0.1, 0.8, 0.1])
    
    with central_grid:
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            st.markdown('<div class="card-membro"><div class="t-membro">📅 Escalas</div>', unsafe_allow_html=True)
            st.button("VER", key="btn_esc")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with c2:
            st.markdown('<div class="card-membro"><div class="t-membro">🕒 Horários</div>', unsafe_allow_html=True)
            st.button("VER", key="btn_hor")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with c3:
            st.markdown('<div class="card-membro"><div class="t-membro">🛠️ Equipamentos</div>', unsafe_allow_html=True)
            st.button("VER", key="btn_equi")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with c4:
            st.markdown('<div class="card-membro"><div class="t-membro">🗓️ Dias</div>', unsafe_allow_html=True)
            st.button("VER", key="btn_dias")
            st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1, 1])
    with col_adm:
        senha = st.text_input("Senha Master", type="password")
        if st.button("ENTRAR NO COMANDO"):
            if senha == "55420":
                st.session_state.tela = "master"; st.rerun()
