import streamlit as st
import os
import random
import re

# 1. CONFIGURAÇÃO DE TELA (Garante que a barra comece aberta)
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

ARQUIVO_ATIVAS = "chaves_ativas.txt"
if not os.path.exists(ARQUIVO_ATIVAS):
    with open(ARQUIVO_ATIVAS, "w", encoding="utf-8") as f: f.write("")

# --- FUNÇÕES ---
def listar_chaves():
    try:
        with open(ARQUIVO_ATIVAS, "r", encoding="utf-8") as f: 
            return [linha.strip() for linha in f.readlines()]
    except: return []

def salvar_chave(chave):
    with open(ARQUIVO_ATIVAS, "a", encoding="utf-8") as f: 
        f.write(chave + "\n")

# 2. CSS MASTER (RESTAURANDO O VISUAL ORIGINAL)
st.markdown("""
    <style>
    /* Remove a seta de recolhimento para manter a barra fixa */
    [data-testid="sidebar-button"], button[title="Collapse sidebar"] {
        display: none !important;
    }
    
    /* Configuração da Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 2px solid #E50914 !important;
        min-width: 260px !important;
    }

    /* Fundo do App */
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    
    /* Inputs Brancos (Escrita Preta) */
    .stTextInput input, .stTextArea textarea { 
        background-color: white !important; 
        color: black !important; 
        font-weight: 600 !important;
    }

    /* Botões Vermelhos Estilizados */
    .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border-radius: 8px !important;
        width: 100% !important;
        border: none !important;
        padding: 10px !important;
    }
    
    .secao-titulo { color: #E50914; font-weight: 900; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVEGAÇÃO LATERAL (BARRA ORIGINAL)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>FERRAMENTAS</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # Botões de Navegação
    if st.button("🏠 HOME"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("💬 CHAT"): st.session_state.tela = "chat"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN"): st.session_state.tela = "login_admin"; st.rerun()
    
    st.write("---")
    st.markdown("<p style='text-align:center; color:#444; font-size:0.7rem;'>SISTEMA KERIGMA v1.0</p>", unsafe_allow_html=True)

# 4. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:3.5rem; color:#E50914; text-align:center; margin-top:80px; font-weight:900;">SEJA BEM-VINDO A EQUIPE MIDIA...</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 2, 1])
    with col_login:
        st.text_input("Nome Completo")
        st.text_input("Número de Telefone")
        st.text_input("Chave de Acesso", type="password")
        if st.button("ENTRAR"): st.session_state.tela = "painel_membro"; st.rerun()

elif st.session_state.tela == "chat":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>💬 CHAT AO VIVO</h1>", unsafe_allow_html=True)
    st.text_area("Conversa", value="[SISTEMA]: Chat iniciado.", height=300)
    st.text_input("Mensagem")
    st.button("ENVIAR")

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 2, 1])
    with col_adm:
        senha = st.text_input("Senha", type="password")
        if st.button("ACESSAR COMANDO"):
            if senha == "55420": st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
    col_g, col_m, col_n = st.columns(3)
    with col_g:
        st.markdown('<p class="secao-titulo">🔑 Gerador</p>', unsafe_allow_html=True)
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "---")
        if st.button("✨ GERAR NOVA CHAVE"):
            st.session_state.chave_gerada = str(random.randint(100000000, 999999999))
            salvar_chave(st.session_state.chave_gerada); st.rerun()
    with col_m:
        st.markdown('<p class="secao-titulo">📢 Mural</p>', unsafe_allow_html=True)
        st.text_area("Aviso", height=68, label_visibility="collapsed")
        st.button("PUBLICAR")
    with col_n:
        st.markdown('<p class="secao-titulo">🔔 Notificações</p>', unsafe_allow_html=True)
        st.text_input("Assunto", label_visibility="collapsed")
        st.button("ENVIAR")
