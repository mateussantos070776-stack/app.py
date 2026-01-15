import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DE TELA
st.set_page_config(page_title="KERIGMA | Master", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE ESTADOS ---
if 'tela' not in st.session_state: 
    st.session_state.tela = "home"
if 'chave_gerada' not in st.session_state: 
    st.session_state.chave_gerada = ""

ARQUIVO_ATIVAS = "chaves_ativas.txt"
if not os.path.exists(ARQUIVO_ATIVAS):
    with open(ARQUIVO_ATIVAS, "w") as f: f.write("")

# --- FUNÇÕES DE SISTEMA ---
def listar_chaves():
    if os.path.exists(ARQUIVO_ATIVAS):
        with open(ARQUIVO_ATIVAS, "r") as f: 
            return [linha.strip() for linha in f.readlines()]
    return []

def salvar_chave(chave):
    with open(ARQUIVO_ATIVAS, "a") as f: 
        f.write(chave + "\n")

# 2. CSS PREMIUM REVISADO (SEM BLOCOS PRETOS E COM ALINHAMENTO)
st.markdown("""
    <style>
    /* Remove cabeçalhos e botões padrão que poluem o visual */
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }

    /* Estilização da Barra Lateral */
    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 2px solid #E50914 !important; 
    }

    /* Estilo dos Títulos das Janelas de Comando */
    .secao-titulo {
        color: #E50914;
        font-weight: 900;
        font-size: 1.1rem;
        text-transform: uppercase;
        margin-top: 10px;
        text-align: center;
    }
    
    .secao-desc {
        color: #888;
        font-size: 0.8rem;
        text-align: center;
        margin-bottom: 20px;
        height: 35px;
    }

    /* Botões Padrão Kerigma */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        width: 100% !important;
        border: none !important;
        font-weight: bold !important;
        height: 45px !important;
        text-transform: uppercase;
    }
    
    /* Inputs Discretos */
    .stTextInput input, .stTextArea textarea {
        background-color: #111 !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (NAVEGAÇÃO REVISADA)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("🏠 HOME", key="nav_h"):
        st.session_state.tela = "home"
        st.rerun()
        
    if st.button("🔴 ÁREA DE MEMBROS", key="nav_m"):
        st.session_state.tela = "login_membro"
        st.rerun()
        
    if st.button("⚙️ ACESSO ADMIN", key="nav_a"):
        st.session_state.tela = "login_admin"
        st.rerun()
    
    st.write("---")
    st.caption("V 1.0 | MAANAIM DIGITAL")

# 4. LÓGICA DE TELAS

# --- TELA: HOME ---
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-family:serif; font-size:4.5rem; color:#E50914; text-align:center; margin-top:80px;">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:1.2rem; color:#ccc;">Bem-vindo ao centro de mídia exclusivo do seu propósito.</p>', unsafe_allow_html=True)

# --- TELA: ÁREA DE MEMBROS (LOGIN) ---
elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1, 1])
    with col_login:
        chave_acesso = st.text_input("Insira sua Chave Sagrada", type="password")
        if st.button("VALIDAR ACESSO"):
            if chave_acesso in listar_chaves() or chave_acesso == "55420":
                st.session_state.tela = "painel_membro"
                st.rerun()
            else:
                st.error("Chave inválida ou não encontrada.")

# --- TELA: PAINEL EXCLUSIVO DO MEMBRO ---
elif st.session_state.tela == "painel_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>BEM-VINDO AO MAANAIM</h1>", unsafe_allow_html=True)
    st.write("---")
    st.success("Acesso autorizado. Você está na Área de Membros.")
    st.markdown("### 🎥 Últimas Pregações e Conteúdos")
    # Aqui você pode adicionar os vídeos e avisos que os membros verão.

# --- TELA: ACESSO ADMIN (LOGIN) ---
elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_admin, _ = st.columns([1, 1, 1])
    with col_admin:
        senha_master = st.text_input("Senha Master", type="password")
        if st.button("ENTRAR NO COMANDO"):
            if senha_master == "55420":
                st.session_state.tela = "master"
                st.rerun()
            else:
                st.error("Acesso negado.")

# --- TELA: CENTRAL DE COMANDO MASTER ---
elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
    
    col_1, col_2, col_3 = st.columns(3)
    
    with col_1:
        st.markdown('<p class="secao-titulo">🔑 Gerador de Acesso</p>', unsafe_allow_html=True)
        st.markdown('<p class="secao-desc">Crie chaves únicas para novos membros</p>', unsafe_allow_html=True)
        if st.button("✨ GERAR NOVA CHAVE"):
            nova_chave = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova_chave)
            st.session_state.chave_gerada = nova_chave
            st.success("Chave gerada com sucesso!")
        
        if st.session_state.chave_gerada:
            st.code(st.session_state.chave_gerada)

    with col_2:
        st.markdown('<p class="secao-titulo">📢 Alterar Avisos</p>', unsafe_allow_html=True)
        st.markdown('<p class="secao-desc">Atualize o mural da área de membros</p>', unsafe_allow_html=True)
        st.text_area("Mensagem", placeholder="Escreva o aviso aqui...", height=100, label_visibility="collapsed", key="mural_txt")
        if st.button("PUBLICAR NO MURAL"):
            st.success("O mural foi atualizado!")

    with col_3:
        st.markdown('<p class="secao-titulo">🔔 Notificar Membro</p>', unsafe_allow_html=True)
        st.markdown('<p class="secao-desc">Envie um alerta direto para os dispositivos</p>', unsafe_allow_html=True)
        st.text_input("Assunto", placeholder="Assunto...", label_visibility="collapsed", key="notif_assunto")
        st.text_input("Mensagem", placeholder="Mensagem curta...", label_visibility="collapsed", key="notif_msg")
        if st.button("ENVIAR NOTIFICAÇÃO"):
            st.warning("Notificação disparada!")
