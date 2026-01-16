import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DE TELA
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

# 2. CSS MASTER - CORREÇÃO DO BOTÃO ENTRAR E LIMPEZA VISUAL
st.markdown("""
    <style>
    /* REMOVE A BARRA BRANCA SUPERIOR (HEADER) */
    header, [data-testid="stHeader"] {
        display: none !important;
    }
    
    .stApp {
        margin-top: -50px !important;
        background-color: #050505;
    }

    /* BARRA LATERAL FIXA */
    button[title="Collapse sidebar"], [data-testid="sidebar-button"] {
        display: none !important;
    }

    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 2px solid #E50914 !important;
        min-width: 260px !important;

        
    /* BOTÕES DA SIDEBAR (VERMELHOS) */
    .stSidebar .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: #E50914 !important; /* LETRA BRANCA */
        font-weight: 700 !important;
        height: 48px !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100% !important;
        margin-bottom: 5px !important;
    }

    /* --- BOTÃO ESPECÍFICO: ENTRAR (ÁREA DE MEMBROS) --- */
    /* Este seletor busca o botão dentro da área central quando a tela é login_membro */
    div[data-testid="stVerticalBlock"] div[data-testid="stButton"] button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-weight: 800 !important;
        border: none !important;
        width: 100% !important;
        height: 45px !important;
        transition: 0.3s;
    }
    
    div[data-testid="stVerticalBlock"] div[data-testid="stButton"] button:hover {
        background-color: #E0E0E0 !important;
        color: #000000 !important;

        
    /* INPUTS BRANCOS */
    .stTextInput input, .stTextArea textarea {
        background-color: white !important;
        color: #000000 !important; /* Letra preta ao digitar */
        font-weight: 600 !important;
        border-radius: 5px !important;
    }

    h1, h2, h3, p { font-family: 'Montserrat', sans-serif; color: white; }
    
    .block-container {
        padding-top: 2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (SEM ALTERAÇÃO)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900; margin-bottom:20px;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("💬 CHAT"): st.session_state.tela = "chat"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN"): st.session_state.tela = "login_admin"; st.rerun()
    st.write("---")

# 4. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:3.5rem; color:#E50914; text-align:center; margin-top:100px; font-weight:900;">EQUIPE MIDIA MAANAIM</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        st.text_input("Nome Completo")
        st.text_input("Chave de Acesso", type="password")
        # O botão abaixo agora será BRANCO com LETRA PRETA conforme o CSS acima
        if st.button("ENTRAR"): st.session_state.tela = "painel_membro"; st.rerun()

elif st.session_state.tela == "chat":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>💬 CHAT AO VIVO</h1>", unsafe_allow_html=True)
    st.text_area("Mensagens", value="Sistema pronto.", height=300, label_visibility="collapsed")
    c_msg, c_send = st.columns([4, 1])
    with c_msg: st.text_input("Sua mensagem...", label_visibility="collapsed")
    with c_send: st.button("ENVIAR")

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1.2, 1])
    with col_adm:
        senha = st.text_input("Senha Master", type="password")
        if st.button("ACESSAR COMANDO"):
            if senha == "55420": st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
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
