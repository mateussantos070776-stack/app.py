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
if 'texto_mural' not in st.session_state:
    st.session_state.texto_mural = "Bem-vindo à Equipe Mídia Maanaim"
if 'sorteados' not in st.session_state:
    st.session_state.sorteados = []

# LISTA DE MEMBROS PARA SORTEIO
membros_equipe = ["Lucas Silva", "Ana Souza", "Mateus Oliveira", "Bárbara Reis", "João Pedro", "Clara Mendes", "Rafael Vaz"]

# 2. CSS MASTER (Com correção para remover a borda branca superior)
st.markdown("""
    <style>
    /* REMOVE A BARRA BRANCA/HEADER DO STREAMLIT */
    header {visibility: hidden;}
    
    /* ELIMINA O ESPAÇO NO TOPO DO CONTEÚDO */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
    }

    /* FORÇA A BARRA LATERAL A FICAR EXPOSTA E SEM SETA */
    [data-testid="sidebar-button"], 
    button[title="Collapse sidebar"], 
    button[title="Expand sidebar"] {
        display: none !important;
    }

    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 2px solid #E50914 !important;
        min-width: 260px !important;
        margin-left: 0 !important;
        transform: none !important;
    }

    .stApp { background-color: #050505; }

    /* BOTÕES DA SIDEBAR */
    .stSidebar .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        height: 40px !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100% !important;
        margin-bottom: 5px !important;
    }

    /* BOTÕES GERAIS */
    div[data-testid="stVerticalBlock"] div[data-testid="stButton"] button {
        background-color: #E50914 !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 5px !important;
    }

    /* INPUTS BRANCOS */
    .stTextInput input {
        background-color: white !important;
        color: black !important;
        font-weight: 600 !important;
    }

    h1, h2, h3, p { color: white !important; font-family: 'Montserrat', sans-serif; }
    
    /* CARD DE SORTEIO COM BORDA VERDE */
    .nome-sorteado {
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME"): 
        st.session_state.tela = "home"
        st.rerun()
    if st.button("🔴 MEMBROS MÍDIA"): 
        st.session_state.tela = "login_membro"
        st.rerun()
    if st.button("💬 CHAT"): 
        st.session_state.tela = "chat"
        st.rerun()
    if st.button("⚙️ KERIGMA ADM"): 
        st.session_state.tela = "login_admin"
        st.rerun()
    st.write("---")

# 4. LÓGICA DE TELAS

# TELA HOME
if st.session_state.tela == "home":
    st.markdown('<h1 style="color:#E50914; text-align:center; margin-top:50px; font-weight:900;">EQUIPE MIDIA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown(f"""
        <div style="text-align:center; margin-top:30px; padding:40px; border:1px solid #E50914; border-radius:10px;">
            <p style="color:#E50914; font-weight:bold; font-size:12px;">MURAL DE AVISOS</p>
            <h2 style="font-weight:300;">{st.session_state.texto_mural}</h2>
        </div>
    """, unsafe_allow_html=True)

# TELA ÁREA DE MEMBROS
elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        nome = st.text_input("Nome Completo", placeholder="Digite seu nome...")
        chave = st.text_input("Chave de Acesso", type="password", placeholder="Sua chave...")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("ENTRAR"):
                if nome and chave:
                    st.session_state.tela = "painel_membro"
                    st.rerun()
        with c2:
            if st.button("VOLTAR"):
                st.session_state.tela = "home"
                st.rerun()

# TELA CENTRAL MÍDIA (ADMIN)
elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL MÍDIA</h1>", unsafe_allow_html=True)
    st.write("---")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("<p style='color:#E50914; font-weight:bold;'>🔑 GERADOR</p>", unsafe_allow_html=True)
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "---")
        if st.button("NOVA CHAVE"):
            st.session_state.chave_gerada = str(random.randint(100000, 999999))
            st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🎲 SORTEIO DE MÍDIA"):
            st.session_state.tela = "sorteio"
            st.rerun()

    with c2:
        st.markdown("<p style='color:#E50914; font-weight:bold;'>📢 MURAL</p>", unsafe_allow_html=True)
        novo_aviso = st.text_area("Novo aviso", height=100, label_visibility="collapsed")
        if st.button("PUBLICAR"):
            st.session_state.texto_mural = novo_aviso
            st.rerun()

# TELA DE SORTEIO
elif st.session_state.tela == "sorteio":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>SORTEIO DE ESCALA</h1>", unsafe_allow_html=True)
    _, col_sorteio, _ = st.columns([1, 2, 1])
    with col_sorteio:
        if st.button("REALIZAR SORTEIO"):
            st.session_state.sorteados = random.sample(membros_equipe, 2)
        
        if st.session_state.sorteados:
            for pessoa in st.session_state.sorteados:
                st.markdown(f"""
                    <div class="nome-sorteado">
                        <span style="color:white; font-size:18px;">{pessoa}</span>
                        <span style="float:right;">✅</span>
                    </div>
                """, unsafe_allow_html=True)
        
        if st.button("VOLTAR PARA CENTRAL"):
            st.session_state.tela = "master"
            st.rerun()

# TELA LOGIN ADMIN
elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1.2, 1])
    with col_adm:
        senha = st.text_input("Senha Master", type="password")
        if st.button("ACESSAR"):
            if senha == "55420": 
                st.session_state.tela = "master"
                st.rerun()
