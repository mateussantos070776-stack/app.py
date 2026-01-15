import streamlit as st
import os
import random
import re

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
if 'mensagens' not in st.session_state:
    st.session_state.mensagens = []

ARQUIVO_ATIVAS = "chaves_ativas.txt"
if not os.path.exists(ARQUIVO_ATIVAS):
    with open(ARQUIVO_ATIVAS, "w", encoding="utf-8") as f: f.write("")

# --- FUNÇÕES ---
def listar_chaves():
    with open(ARQUIVO_ATIVAS, "r", encoding="utf-8") as f: 
        return [linha.strip() for linha in f.readlines()]

def salvar_chave(chave):
    with open(ARQUIVO_ATIVAS, "a", encoding="utf-8") as f: 
        f.write(chave + "\n")

def validar_telefone(tel):
    padrao = r"^\(?\d{2}\)?\s?9\d{4}-?\d{4}$"
    return re.match(padrao, tel)

# 2. CSS MASTER (BARRA FIXA E ESTILIZAÇÃO)
st.markdown("""
    <style>
    /* Esconde botões de fechar e cabeçalho */
    [data-testid="stHeader"], 
    button[title="Collapse sidebar"], 
    [data-testid="sidebar-button"] {
        display: none !important;
    }
    
    /* Fixa a Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 2px solid #E50914 !important;
        min-width: 280px !important;
    }

    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    
    /* Estilo dos Botões da Sidebar */
    .stSidebar [data-testid="stButton"] button {
        background: #111 !important;
        border: 1px solid #333 !important;
        color: #eee !important;
        text-align: left !important;
        justify-content: flex-start !important;
        padding: 10px !important;
        margin-bottom: -10px;
    }
    
    .stSidebar [data-testid="stButton"] button:hover {
        border-color: #E50914 !important;
        color: #E50914 !important;
    }

    /* Inputs Brancos */
    .stTextInput input, .stTextArea textarea { 
        background-color: white !important; 
        color: black !important; 
        font-weight: 600 !important;
    }

    /* Botão de Ação Vermelho */
    .btn-ver button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        font-weight: 800 !important;
        text-transform: uppercase;
    }
    
    .titulo-sidebar { color: #E50914; font-size: 0.8rem; font-weight: 800; margin-top: 20px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL UNIFICADA (TODAS AS FUNÇÕES)
with st.sidebar:
    st.markdown("<h1 style='color:#E50914; font-size:1.5rem; font-weight:900;'>SISTEMA KERIGMA</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # SEÇÃO NAVEGAÇÃO
    st.markdown('<p class="titulo-sidebar">📍 Navegação Principal</p>', unsafe_allow_html=True)
    if st.button("🏠 HOME"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN"): st.session_state.tela = "login_admin"; st.rerun()
    
    # SEÇÃO FERRAMENTAS DO MEMBRO (SÓ APARECE SE LOGADO OU PARA ATALHO)
    st.markdown('<p class="titulo-sidebar">🛠️ Ferramentas Membro</p>', unsafe_allow_html=True)
    if st.button("📅 ESCALAS"): st.toast("Acessando Escalas...")
    if st.button("🕒 HORÁRIOS"): st.toast("Acessando Horários...")
    if st.button("🛠️ EQUIPAMENTOS"): st.toast("Lista de Equipamentos...")
    if st.button("💬 CHAT AO VIVO"): st.session_state.tela = "chat"; st.rerun()
    
    # SEÇÃO ADMINISTRATIVA
    st.markdown('<p class="titulo-sidebar">🔒 Gestão Master</p>', unsafe_allow_html=True)
    if st.button("🔑 GERADOR DE CHAVES"): st.session_state.tela = "master"; st.rerun()
    if st.button("📢 PUBLICAR NO MURAL"): st.session_state.tela = "master"; st.rerun()
    
    st.write("---")
    st.markdown("<p style='font-size:0.6rem; color:#444; text-align:center;'>KERIGMA v2.0 | MAANAIM</p>", unsafe_allow_html=True)

# 4. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:3.5rem; color:#E50914; text-align:center; margin-top:80px; font-weight:900;">SEJA BEM-VINDO A EQUIPE MIDIA...</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1.5, 1])
    with col_login:
        st.text_input("Nome Completo")
        st.text_input("Telefone")
        st.text_input("Chave", type="password")
        st.markdown('<div class="btn-ver">', unsafe_allow_html=True)
        if st.button("ENTRAR NO SISTEMA"): st.session_state.tela = "painel_membro"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.tela == "chat":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>💬 CHAT AO VIVO</h1>", unsafe_allow_html=True)
    # Exemplo de Chat
    chat_box = st.container(border=True)
    for msg in st.session_state.mensagens: chat_box.write(msg)
    
    msg_input = st.text_input("Sua mensagem...")
    if st.button("ENVIAR"):
        if msg_input:
            st.session_state.mensagens.append(f"Membro: {msg_input}")
            st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>COMANDO MASTER</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔑 Chave Atual")
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "---")
        if st.button("GERAR NOVA"):
            st.session_state.chave_gerada = str(random.randint(100000, 999999))
            st.rerun()
    with col2:
        st.markdown("### 📢 Aviso Global")
        st.text_area("Texto do aviso")
        st.button("PUBLICAR")
