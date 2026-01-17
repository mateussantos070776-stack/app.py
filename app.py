import streamlit as st
import os
import random
import json

# 1. CONFIGURAÇÃO DE TELA
st.set_page_config(
    page_title="KERIGMA | Sistema", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- FUNÇÕES DE PERSISTÊNCIA ---
def carregar_usuarios():
    if os.path.exists("usuarios_kerigma.json"):
        try:
            with open("usuarios_kerigma.json", "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def salvar_usuario_no_arquivo(nome, chave):
    usuarios = carregar_usuarios()
    usuarios[nome] = chave
    with open("usuarios_kerigma.json", "w") as f:
        json.dump(usuarios, f)

def remover_usuario_do_arquivo(nome_para_remover):
    usuarios = carregar_usuarios()
    if nome_para_remover in usuarios:
        del usuarios[nome_para_remover]
        with open("usuarios_kerigma.json", "w") as f:
            json.dump(usuarios, f)

# --- INICIALIZAÇÃO DE ESTADOS ---
if 'tela' not in st.session_state: 
    st.session_state.tela = "home"
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'chave_gerada' not in st.session_state: 
    st.session_state.chave_gerada = ""
if 'texto_mural' not in st.session_state:
    st.session_state.texto_mural = "Bem-vindo à Equipe Mídia Maanaim"
if 'sorteados' not in st.session_state:
    st.session_state.sorteados = []
if 'usuarios_registrados' not in st.session_state:
    st.session_state.usuarios_registrados = carregar_usuarios()

# 2. CSS MASTER
st.markdown("""
    <style>
    header {visibility: hidden;}
    .block-container { padding-top: 0rem !important; padding-bottom: 0rem !important; }
    
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

    div[data-testid="stVerticalBlock"] div[data-testid="stButton"] button {
        background-color: #E50914 !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border-radius: 5px !important;
    }

    .stTextInput input { background-color: white !important; color: black !important; font-weight: 600 !important; }
    h1, h2, h3, p { color: white !important; font-family: 'Montserrat', sans-serif; }
    
    .janela-desenvolvimento { 
        border: 2px solid #E50914; 
        border-radius: 15px; 
        padding: 60px; 
        text-align: center; 
        background-color: #0a0a0a; 
        margin-top: 100px; 
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (OPÇÕES)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("🏠 HOME"): 
        st.session_state.tela = "home"
        st.rerun()
    
    if st.button("🔴 MEMBROS MÍDIA"): 
        if st.session_state.autenticado:
            st.session_state.tela = "painel_membro"
        else:
            st.session_state.tela = "login_membro"
        st.rerun()
        
    if st.button("⚙️ KERIGMA ADM"): 
        if st.session_state.autenticado:
            st.session_state.tela = "master"
        else:
            st.session_state.tela = "login_admin"
        st.rerun()
    
    if st.session_state.autenticado:
        st.write("---")
        if st.button("🚪 SAIR DA CONTA"):
            st.session_state.autenticado = False
            st.session_state.tela = "home"
            st.rerun()
    st.write("---")

# 4. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 style="color:#E50914; text-align:center; margin-top:50px; font-weight:900;">EQUIPE MIDIA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align:center; margin-top:30px; padding:40px; border:1px solid #E50914; border-radius:10px;"><p style="color:#E50914; font-weight:bold; font-size:12px;">MURAL DE AVISOS</p><h2 style="font-weight:300;">{st.session_state.texto_mural}</h2></div>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        nome_i = st.text_input("Nome Completo").strip().upper()
        chave_i = st.text_input("Chave", type="password").strip()
        if st.button("ENTRAR"):
            if nome_i and chave_i:
                registrados = carregar_usuarios()
                if nome_i in registrados and registrados[nome_i] == chave_i:
                    st.session_state.autenticado = True
                    st.session_state.tela = "painel_membro"
                    st.rerun()
                elif chave_i not in registrados.values() and nome_i not in registrados:
                    salvar_usuario_no_arquivo(nome_i, chave_i)
                    st.session_state.autenticado = True
                    st.session_state.tela = "painel_membro"
                    st.rerun()
                else:
                    st.error("Credenciais inválidas ou chave em uso.")

elif st.session_state.tela == "painel_membro":
    if not st.session_state.autenticado: 
        st.session_state.tela = "login_membro"
        st.rerun()
    st.markdown('<div class="janela-desenvolvimento"><h1 style="color:#E50914; font-size:40px; font-weight:900;">EM DESENVOLVIMENTO</h1><p>Seu acesso está ativo.</p></div>', unsafe_allow_html=True)

elif st.session_state.tela == "master":
    if not st.session_state.autenticado:
        st.session_state.tela = "login_admin"
        st.rerun()
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL MÍDIA</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "---")
        if st.button("GERAR CHAVE"):
            st.session_state.chave_gerada = str(random.randint(100000, 999999))
            st.rerun()
        if st.button("👥 LISTA DE USUÁRIOS"):
            st.session_state.tela = "lista_usuarios"
            st.rerun()
    with c2:
        mural = st.text_area("Mural de Avisos", value=st.session_state.texto_mural)
        if st.button("ATUALIZAR MURAL"):
            st.session_state.texto_mural = mural
            st.rerun()

elif st.session_state.tela == "lista_usuarios":
    if not st.session_state.autenticado:
        st.session_state.tela = "login_admin"
        st.rerun()
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>USUÁRIOS INSCRITOS</h1>", unsafe_allow_html=True)
    usrs = carregar_usuarios()
    for u, c in usrs.items():
        col_txt, col_del = st.columns([0.8, 0.2])
        col_txt.markdown(f"**{u}** (Chave: {c})")
        if col_del.button("🗑️", key=u):
            remover_usuario_do_arquivo(u)
            st.rerun()
    if st.button("VOLTAR"):
        st.session_state.tela = "master"
        st.rerun()

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1, 1])
    with col_adm:
        senha_m = st.text_input("Senha Master", type="password")
        if st.button("ENTRAR ADM"):
            if senha_m == "55420":
                st.session_state.autenticado = True
                st.session_state.tela = "master"
                st.rerun()
