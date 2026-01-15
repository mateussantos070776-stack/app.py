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

# 2. CSS REVISADO (FUNDO BRANCO NOS INPUTS CONFORME SOLICITADO)
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #E50914 !important; }
    
    /* Campos de Escrita com Fundo Branco */
    .stTextInput input, .stTextArea textarea { 
        background-color: white !important; 
        color: black !important; 
        border: 1px solid #ccc !important;
        font-weight: 500 !important;
    }

    /* Botões da Central do Membro (Mantidos da versão anterior) */
    .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        border: none !important;
        padding: 20px 10px !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border-radius: 8px !important;
        width: 100% !important;
    }

    /* Estilos Master */
    .secao-titulo { color: #E50914; font-weight: 900; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 2px; }
    .secao-desc { color: #666; font-size: 0.7rem; margin-bottom: 10px; }
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
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:4rem; color:#E50914; text-align:center; margin-top:80px;">Kerigma Maanaim</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 1, 1])
    with col_login:
        chave = st.text_input("Chave", type="password")
        if st.button("ENTRAR"):
            if chave in listar_chaves() or chave == "55420":
                st.session_state.tela = "painel_membro"; st.rerun()

elif st.session_state.tela == "painel_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>CENTRAL DO MEMBRO</h1>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    _, central_grid, _ = st.columns([0.15, 0.7, 0.15])
    with central_grid:
        m1, m2, m3, m4 = st.columns(4)
        m1.button("📅 ESCALAS", key="btn_escalas")
        m2.button("🕒 HORÁRIOS", key="btn_horarios")
        m3.button("🛠️ EQUIPAMENTOS", key="btn_equip")
        m4.button("🗓️ DIAS", key="btn_dias")

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1, 1])
    with col_adm:
        senha = st.text_input("Senha", type="password")
        if st.button("ACESSAR COMANDO"):
            if senha == "55420": st.session_state.tela = "master"; st.rerun()

# --- TELA: MASTER (FUNDO BRANCO NOS CAMPOS) ---
elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
    
    t1, t2, t3 = st.columns(3)
    t1.markdown('<p class="secao-titulo">🔑 Gerador de Acesso</p><p class="secao-desc">Chaves de novos membros</p>', unsafe_allow_html=True)
    t2.markdown('<p class="secao-titulo">📢 Mural de Avisos</p><p class="secao-desc">Atualize o Maanaim</p>', unsafe_allow_html=True)
    t3.markdown('<p class="secao-titulo">🔔 Notificações</p><p class="secao-desc">Envie alertas diretos</p>', unsafe_allow_html=True)

    # LINHA DE ESCRITA (Fundo Branco via CSS)
    w1, w2, w3 = st.columns(3)
    with w1:
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "Aguardando...", language="text")
    with w2:
        st.text_area("Aviso", placeholder="Digite o aviso...", height=68, label_visibility="collapsed")
    with w3:
        st.text_input("Notif", placeholder="Assunto do alerta...", label_visibility="collapsed")

    # LINHA DE BOTÕES
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
