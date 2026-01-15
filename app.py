import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DE TELA (Sem bordas e com sidebar expandida)
st.set_page_config(
    page_title="KERIGMA | Sistema", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE ESTADOS ---
if 'tela' not in st.session_state: 
    st.session_state.tela = "home"
if 'chave_gerada' not in st.session_state: 
    st.session_state.chave_gerada = ""

# --- CSS PARA REMOVER BORDA BRANCA E AJUSTAR PROPORÇÕES ---
st.markdown("""
    <style>
    /* Remove o cabeçalho branco e qualquer borda superior */
    [data-testid="stHeader"], .st-emotion-cache-18ni73i, .st-emotion-cache-6qob1r {
        display: none !important;
    }
    
    /* Remove a seta de recolhimento da sidebar */
    button[title="Collapse sidebar"], [data-testid="sidebar-button"] {
        display: none !important;
    }

    /* Fundo Total Black */
    .stApp {
        background-color: #050505;
        color: white;
        font-family: 'Montserrat', sans-serif;
    }

    /* Estilização da Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 2px solid #E50914 !important;
        min-width: 260px !important;
    }

    /* Botões da Sidebar Proporcionais */
    .stSidebar .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        height: 45px !important;
        border-radius: 10px !important;
        margin-bottom: 10px !important;
        border: none !important;
        width: 100%;
    }

    /* Inputs e Áreas de Texto Proporcionais */
    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-weight: 600 !important;
    }

    /* Centralização de Títulos */
    .titulo-central {
        color: #E50914;
        text-align: center;
        font-weight: 900;
        text-transform: uppercase;
        margin-top: -30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. BARRA LATERAL (ORIGINAL E FIXA)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("💬 CHAT"): st.session_state.tela = "chat"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN"): st.session_state.tela = "login_admin"; st.rerun()
    st.write("---")

# 3. LÓGICA DE TELAS PROPORCIONAIS
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:3.5rem; color:#E50914; text-align:center; margin-top:150px; font-weight:900;">EQUIPE MIDIA MAANAIM</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 class='titulo-central'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        st.text_input("Nome Completo")
        st.text_input("Chave de Acesso", type="password")
        if st.button("ENTRAR"): st.session_state.tela = "painel_membro"; st.rerun()

elif st.session_state.tela == "chat":
    st.markdown("<h1 class='titulo-central'>💬 CHAT AO VIVO</h1>", unsafe_allow_html=True)
    st.text_area("Histórico", value="Aguardando mensagens...", height=300)
    col_msg, col_btn = st.columns([4, 1])
    with col_msg: st.text_input("Mensagem", label_visibility="collapsed")
    with col_btn: st.button("ENVIAR")

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 class='titulo-central'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1.2, 1])
    with col_adm:
        senha = st.text_input("Senha Master", type="password")
        if st.button("ACESSAR COMANDO"):
            if senha == "55420": st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h1 class='titulo-central'>CENTRAL DE COMANDO</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<p style='color:#E50914; font-weight:bold;'>🔑 GERADOR</p>", unsafe_allow_html=True)
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "---")
        if st.button("NOVA CHAVE"):
            st.session_state.chave_gerada = str(random.randint(100000, 999999))
            st.rerun()
    with c2:
        st.markdown("<p style='color:#E50914; font-weight:bold;'>📢 MURAL</p>", unsafe_allow_html=True)
        st.text_area("Aviso", height=68, label_visibility="collapsed")
        st.button("PUBLICAR")
    with c3:
        st.markdown("<p style='color:#E50914; font-weight:bold;'>🔔 NOTIF.</p>", unsafe_allow_html=True)
        st.text_input("Assunto", label_visibility="collapsed")
        st.button("ENVIAR")
