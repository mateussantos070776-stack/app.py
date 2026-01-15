import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DE TELA
st.set_page_config(page_title="KERIGMA | Master", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE ESTADOS (ESSENCIAL PARA OS BOTÕES FUNCIONAREM) ---
if 'tela' not in st.session_state: 
    st.session_state.tela = "home"
if 'chave_gerada' not in st.session_state: 
    st.session_state.chave_gerada = ""

# 2. CSS AVANÇADO (LIMPEZA TOTAL E BOTÕES LATERAIS)
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    [data-testid="stVerticalBlock"] > div:empty { display: none !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }

    /* Barra Lateral */
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #E50914 !important; }

    /* Cards Master */
    .card-fixo {
        background: #111;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        min-height: 350px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }

    .t-red { color: #E50914; font-weight: 900; font-size: 1.1rem; text-transform: uppercase; margin-bottom: 10px; }
    .d-gray { color: #888; font-size: 0.85rem; margin-bottom: 20px; height: 40px; }

    /* Botões Gerais */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        width: 100% !important;
        border: none !important;
        font-weight: bold !important;
        height: 45px !important;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (FUNÇÕES RESTAURADAS)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("🏠 HOME", key="btn_side_home"):
        st.session_state.tela = "home"
        st.rerun()
        
    if st.button("🔴 ÁREA DE MEMBROS", key="btn_side_membros"):
        st.session_state.tela = "login_membro"
        st.rerun()
        
    if st.button("⚙️ ACESSO ADMIN", key="btn_side_admin"):
        st.session_state.tela = "login_admin"
        st.rerun()

# 4. LÓGICA DE TROCA DE TELAS

# --- TELA: HOME ---
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-family:serif; font-size:4rem; color:#E50914; text-align:center; margin-top:100px;">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:1.2rem;">Bem-vindo ao centro de mídia exclusivo.</p>', unsafe_allow_html=True)

# --- TELA: PAINEL MASTER ---
elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('<div class="card-fixo"><div class="t-red">🔑 Gerador de Acesso</div><div class="d-gray">Crie chaves únicas para novos membros</div>', unsafe_allow_html=True)
        if st.button("✨ GERAR NOVA CHAVE"):
            st.session_state.chave_gerada = "".join([str(random.randint(0, 9)) for _ in range(10)])
        if st.session_state.chave_gerada:
            st.code(st.session_state.chave_gerada)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card-fixo"><div class="t-red">📢 Alterar Avisos</div><div class="d-gray">Atualize o mural da área de membros</div>', unsafe_allow_html=True)
        st.text_area("Aviso", placeholder="Escreva aqui...", height=100, label_visibility="collapsed")
        if st.button("PUBLICAR MURAL"):
            st.success("Mural atualizado!")
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="card-fixo"><div class="t-red">🔔 Notificar Membro</div><div class="d-gray">Envie um alerta para os dispositivos</div>', unsafe_allow_html=True)
        st.text_input("Assunto", placeholder="Assunto...", label_visibility="collapsed")
        st.text_input("Mensagem", placeholder="Mensagem...", label_visibility="collapsed")
        if st.button("ENVIAR ALERTA"):
            st.warning("Alerta disparado!")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TELA: LOGIN ADMIN ---
elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>AUTENTICAÇÃO LIDERANÇA</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        senha = st.text_input("Senha Master", type="password")
        if st.button("ENTRAR NO COMANDO"):
            if senha == "55420":
                st.session_state.tela = "master"
                st.rerun()

# --- TELA: LOGIN MEMBRO ---
elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.text_input("Insira sua Chave", type="password")
        st.button("VALIDAR ACESSO")
