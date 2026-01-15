import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DE TELA
st.set_page_config(page_title="KERIGMA | Member", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE ESTADOS ---
if 'tela' not in st.session_state: 
    st.session_state.tela = "home"
if 'chave_gerada' not in st.session_state: 
    st.session_state.chave_gerada = ""

ARQUIVO_ATIVAS = "chaves_ativas.txt"

# --- FUNÇÕES DE SISTEMA ---
def listar_chaves():
    if os.path.exists(ARQUIVO_ATIVAS):
        with open(ARQUIVO_ATIVAS, "r") as f: 
            return [linha.strip() for linha in f.readlines()]
    return []

# 2. CSS PREMIUM REVISADO (FOCO EM SIMETRIA E LIMPEZA)
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }

    /* Barra Lateral */
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #E50914 !important; }

    /* Janelas de Opções (Quadrados 4x4) */
    .card-membro {
        background: #111;
        border: 2px solid #333;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        aspect-ratio: 1 / 1; /* Mantém o formato de quadrado perfeito */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transition: 0.4s;
        margin-bottom: 20px;
    }
    
    .card-membro:hover { border-color: #E50914; transform: scale(1.02); }

    .t-membro { color: #E50914; font-weight: 900; font-size: 1.3rem; text-transform: uppercase; margin-bottom: 15px; }

    /* Botões */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        width: 100% !important;
        border: none !important;
        font-weight: bold !important;
        height: 45px !important;
        text-transform: uppercase;
    }
    
    /* Inputs */
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

# --- HOME ---
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-family:serif; font-size:4.5rem; color:#E50914; text-align:center; margin-top:80px;">Kerigma Maanaim</h1>', unsafe_allow_html=True)

# --- LOGIN MEMBRO ---
elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1, 1])
    with col_login:
        chave = st.text_input("Insira sua Chave", type="password")
        if st.button("VALIDAR ACESSO"):
            if chave in listar_chaves() or chave == "55420":
                st.session_state.tela = "painel_membro"; st.rerun()
            else: st.error("Chave inválida.")

# --- TELA SOLICITADA: PAINEL DE MEMBROS (4 JANELAS QUADRADAS) ---
elif st.session_state.tela == "painel_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>BEM-VINDO AO MAANAIM</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Grid de 4 janelas (2x2 para manter o aspecto quadrado em telas variadas)
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)
    
    with c1:
        st.markdown('<div class="card-membro"><div class="t-membro">📅 Escalas</div>', unsafe_allow_html=True)
        if st.button("VER MINHAS ESCALAS", key="btn_esc"): pass
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="card-membro"><div class="t-membro">🕒 Horários</div>', unsafe_allow_html=True)
        if st.button("CRONOGRAMA GERAL", key="btn_hor"): pass
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c3:
        st.markdown('<div class="card-membro"><div class="t-membro">🛠️ Equipamentos</div>', unsafe_allow_html=True)
        if st.button("SOLICITAR / STATUS", key="btn_equi"): pass
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c4:
        st.markdown('<div class="card-membro"><div class="t-membro">🗓️ Dias</div>', unsafe_allow_html=True)
        if st.button("AGENDA SEMANAL", key="btn_dias"): pass
        st.markdown('</div>', unsafe_allow_html=True)

# --- LOGIN ADMIN & MASTER (Mantidos conforme original) ---
elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1, 1])
    with col_adm:
        if st.button("ENTRAR NO COMANDO"): # Simplificado para teste
            st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>CENTRAL MASTER</h1>", unsafe_allow_html=True)
    if st.button("SAIR"): st.session_state.tela = "home"; st.rerun()
