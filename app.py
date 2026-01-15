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

# 2. CSS COMPLETO E REVISADO (SEM BLOCOS PRETOS)
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }

    /* Barra Lateral */
    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 2px solid #E50914 !important; 
    }

    /* Janelas de Membros (Compactas) */
    .card-membro {
        background: #111;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        aspect-ratio: 1 / 1;
        max-width: 160px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        justify-content: center;
        transition: 0.3s;
    }
    .card-membro:hover { border-color: #E50914; }
    .t-membro { color: #E50914; font-weight: 800; font-size: 0.8rem; text-transform: uppercase; margin-bottom: 10px; }

    /* Estilos da Central Master */
    .secao-titulo { color: #E50914; font-weight: 900; font-size: 1.1rem; text-transform: uppercase; margin-top: 10px; text-align: center; }
    .secao-desc { color: #888; font-size: 0.8rem; text-align: center; margin-bottom: 20px; height: 35px; }

    /* Botões Estilizados */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        width: 100% !important;
        border: none !important;
        font-weight: bold !important;
        text-transform: uppercase;
        border-radius: 5px !important;
    }
    
    .stTextInput input, .stTextArea textarea {
        background-color: #111 !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
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
    st.write("---")
    st.caption("V 1.0 | MAANAIM DIGITAL")

# 4. LÓGICA DE TELAS

if st.session_state.tela == "home":
    st.markdown('<h1 style="font-family:serif; font-size:4rem; color:#E50914; text-align:center; margin-top:80px;">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#888;">Centro de Mídia e Gestão Eclesiástica</p>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1, 1])
    with col_login:
        chave = st.text_input("Insira sua Chave Sagrada", type="password")
        if st.button("VALIDAR ACESSO"):
            if chave in listar_chaves() or chave == "55420":
                st.session_state.tela = "painel_membro"; st.rerun()
            else: st.error("Chave inválida.")

elif st.session_state.tela == "painel_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>CENTRAL DO MEMBRO</h1>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
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
            else: st.error("Senha incorreta.")

elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
    
    m_col1, m_col2, m_col3 = st.columns(3)
    
    with m_col1:
        st.markdown('<p class="secao-titulo">🔑 Gerador de Acesso</p>', unsafe_allow_html=True)
        st.markdown('<p class="secao-desc">Crie chaves para novos membros</p>', unsafe_allow_html=True)
        if st.button("✨ GERAR NOVA CHAVE"):
            nova_chave = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova_chave)
            st.session_state.chave_gerada = nova_chave
        if st.session_state.chave_gerada:
            st.code(st.session_state.chave_gerada)

    with m_col2:
        st.markdown('<p class="secao-titulo">📢 Mural de Avisos</p>', unsafe_allow_html=True)
        st.markdown('<p class="secao-desc">Atualize a Área de Membros</p>', unsafe_allow_html=True)
        st.text_area("Aviso", placeholder="Digite aqui...", height=70, label_visibility="collapsed")
        st.button("PUBLICAR NO MURAL")

    with m_col3:
        st.markdown('<p class="secao-titulo">🔔 Notificações</p>', unsafe_allow_html=True)
        st.markdown('<p class="secao-desc">Envie alertas aos dispositivos</p>', unsafe_allow_html=True)
        st.text_input("Assunto", placeholder="Assunto...", label_visibility="collapsed")
        st.button("ENVIAR ALERTA")
    
    st.write("---")
    if st.button("⬅️ SAIR DO PAINEL MASTER"):
        st.session_state.tela = "home"; st.rerun()
