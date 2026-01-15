import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DE TELA
st.set_page_config(page_title="KERIGMA | Sistema", layout="wide", initial_sidebar_state="expanded")

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

# 2. CSS COMPLETO (FOCO EM ALINHAMENTO E SIMETRIA)
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #E50914 !important; }
    
    /* Janelas de Membros (4x4 Compactas) */
    .card-membro {
        background: #111;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        aspect-ratio: 1 / 1;
        max-width: 150px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        justify-content: center;
        transition: 0.3s;
    }
    .t-membro { color: #E50914; font-weight: 800; font-size: 0.75rem; text-transform: uppercase; margin-bottom: 8px; }

    /* Estilos Master */
    .secao-titulo { color: #E50914; font-weight: 900; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 2px; }
    .secao-desc { color: #666; font-size: 0.7rem; margin-bottom: 10px; }

    /* Inputs e Botões */
    .stTextInput input, .stTextArea textarea { background-color: #111 !important; color: white !important; border: 1px solid #333 !important; }
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        width: 100% !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 0.75rem !important;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME", key="nav_h"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS", key="nav_m"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN", key="nav_a"): st.session_state.tela = "login_admin"; st.rerun()

# 4. LÓGICA DE TELAS

# --- HOME ---
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:4rem; color:#E50914; text-align:center; margin-top:80px;">Kerigma Maanaim</h1>', unsafe_allow_html=True)

# --- LOGIN MEMBRO ---
elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1, 1])
    with col_login:
        chave = st.text_input("Chave", type="password")
        if st.button("ENTRAR"):
            if chave in listar_chaves() or chave == "55420":
                st.session_state.tela = "painel_membro"; st.rerun()

# --- TELA: PAINEL DE MEMBROS (RECUPERADA) ---
elif st.session_state.tela == "painel_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>CENTRAL DO MEMBRO</h1>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    _, central_grid, _ = st.columns([0.1, 0.8, 0.1])
    with central_grid:
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown('<div class="card-membro"><div class="t-membro">📅 Escalas</div>', unsafe_allow_html=True)
            st.button("VER", key="m_esc")
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="card-membro"><div class="t-membro">🕒 Horários</div>', unsafe_allow_html=True)
            st.button("VER", key="m_hor")
            st.markdown('</div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="card-membro"><div class="t-membro">🛠️ Equipamentos</div>', unsafe_allow_html=True)
            st.button("VER", key="m_equi")
            st.markdown('</div>', unsafe_allow_html=True)
        with c4:
            st.markdown('<div class="card-membro"><div class="t-membro">🗓️ Dias</div>', unsafe_allow_html=True)
            st.button("VER", key="m_dias")
            st.markdown('</div>', unsafe_allow_html=True)

# --- LOGIN ADMIN ---
elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1, 1])
    with col_adm:
        senha = st.text_input("Senha", type="password")
        if st.button("ACESSAR COMANDO"):
            if senha == "55420": st.session_state.tela = "master"; st.rerun()

# --- TELA: MASTER (COM ALINHAMENTO SOLICITADO) ---
elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # 1ª CAMADA: TÍTULOS
    t1, t2, t3 = st.columns(3)
    t1.markdown('<p class="secao-titulo">🔑 Gerador de Acesso</p><p class="secao-desc">Chaves de novos membros</p>', unsafe_allow_html=True)
    t2.markdown('<p class="secao-titulo">📢 Mural de Avisos</p><p class="secao-desc">Atualize o Maanaim</p>', unsafe_allow_html=True)
    t3.markdown('<p class="secao-titulo">🔔 Notificações</p><p class="secao-desc">Envie alertas diretos</p>', unsafe_allow_html=True)

    # 2ª CAMADA: CAMPOS DE ESCRITA ALINHADOS
    w1, w2, w3 = st.columns(3)
    with w1:
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "Nenhuma chave gerada", language="text")
    with w2:
        st.text_area("Aviso", placeholder="Digite o aviso...", height=68, label_visibility="collapsed")
    with w3:
        st.text_input("Notif", placeholder="Assunto do alerta...", label_visibility="collapsed")

    # 3ª CAMADA: BOTÕES DE CLIQUE ALINHADOS LOGO ABAIXO
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("✨ GERAR NOVA CHAVE"):
            st.session_state.chave_gerada = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(st.session_state.chave_gerada)
            st.rerun()
    with b2:
        st.button("PUBLICAR NO MURAL")
    with b3:
        st.button("ENVIAR NOTIFICAÇÃO")

    st.write("---")
    if st.button("⬅️ VOLTAR"): st.session_state.tela = "home"; st.rerun()
