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
if 'menu_aberto' not in st.session_state:
    st.session_state.menu_aberto = False

# 2. CSS MASTER (FIXO PC + RESPONSIVO MOBILE)
# Define se o menu mobile está visível baseado no estado
mobile_menu_css = "block" if st.session_state.menu_aberto else "none"

st.markdown(f"""
    <style>
    header {{visibility: hidden;}}
    .block-container {{ padding-top: 1rem !important; }}
    
    /* --- LAYOUT PARA PC (Telas > 768px) --- */
    [data-testid="stSidebar"] {{
        background-color: #080808 !important;
        border-right: 2px solid #E50914 !important;
        min-width: 260px !important;
        display: block !important; /* Sempre visível no PC */
    }}

    /* Esconder o botão de menu no PC */
    .btn-mobile {{ display: none; }}

    /* --- LAYOUT PARA CELULAR (Telas <= 768px) --- */
    @media (max-width: 768px) {{
        [data-testid="stSidebar"] {{
            display: {mobile_menu_css} !important;
            position: fixed !important;
            width: 85% !important;
            z-index: 99999;
            border-right: 3px solid #E50914 !important;
        }}
        
        .btn-mobile {{
            display: block !important;
            margin-bottom: 20px;
        }}
    }}

    /* Estilos Gerais */
    .stApp {{ background-color: #050505; }}
    [data-testid="sidebar-button"] {{ display: none !important; }}
    
    .stSidebar .stButton > button {{
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        width: 100% !important;
    }}

    .stTextInput input {{ background-color: white !important; color: black !important; font-weight: 600 !important; }}
    h1, h2, h3, p {{ color: white !important; font-family: 'Montserrat', sans-serif; }}
    </style>
    """, unsafe_allow_html=True)

# 3. BOTÃO DE MENU (Aparece apenas no celular via CSS)
st.markdown('<div class="btn-mobile">', unsafe_allow_html=True)
if st.button("☰ MENU" if not st.session_state.menu_aberto else "✖ FECHAR"):
    st.session_state.menu_aberto = not st.session_state.menu_aberto
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# 4. BARRA LATERAL (SIDEBAR)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("🏠 HOME"): 
        st.session_state.tela = "home"; st.session_state.menu_aberto = False; st.rerun()
    
    if st.button("🔴 MEMBROS MÍDIA"): 
        st.session_state.tela = "painel_membro" if st.session_state.autenticado else "login_membro"
        st.session_state.menu_aberto = False; st.rerun()
        
    if st.button("⚙️ KERIGMA ADM"): 
        st.session_state.tela = "master" if st.session_state.autenticado else "login_admin"
        st.session_state.menu_aberto = False; st.rerun()
    
    if st.session_state.autenticado:
        st.write("---")
        if st.button("🚪 SAIR DA CONTA"):
            st.session_state.autenticado = False; st.session_state.tela = "home"
            st.session_state.menu_aberto = False; st.rerun()
    st.write("---")

# 5. CONTEÚDO PRINCIPAL
if st.session_state.tela == "home":
    st.markdown('<h1 style="color:#E50914; text-align:center; margin-top:20px; font-weight:900;">EQUIPE MIDIA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align:center; margin-top:30px; padding:40px; border:1px solid #E50914; border-radius:10px;"><p style="color:#E50914; font-weight:bold; font-size:12px;">MURAL DE AVISOS</p><h2 style="font-weight:300;">{st.session_state.texto_mural}</h2></div>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    nome_i = st.text_input("Nome Completo").strip().upper()
    chave_i = st.text_input("Chave", type="password").strip()
    if st.button("ENTRAR", use_container_width=True):
        reg = carregar_usuarios()
        if nome_i in reg and reg[nome_i] == chave_i:
            st.session_state.autenticado = True; st.session_state.tela = "painel_membro"; st.rerun()
        elif chave_i not in reg.values() and nome_i not in reg and nome_i != "":
            salvar_usuario_no_arquivo(nome_i, chave_i)
            st.session_state.autenticado = True; st.session_state.tela = "painel_membro"; st.rerun()
        else: st.error("Dados inválidos ou em uso.")

elif st.session_state.tela == "master":
    if not st.session_state.autenticado: st.session_state.tela = "login_admin"; st.rerun()
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>PAINEL ADM</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<h3 style='text-align:center;'>🔑 Chaves</h3>", unsafe_allow_html=True)
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "---")
        if st.button("GERAR NOVA CHAVE", use_container_width=True):
            st.session_state.chave_gerada = str(random.randint(100000, 999999)); st.rerun()
    with c2:
        st.markdown("<h3 style='text-align:center;'>👥 Membros</h3>", unsafe_allow_html=True)
        if st.button("VER USUÁRIOS INSCRITOS", use_container_width=True):
            st.session_state.tela = "lista_usuarios"; st.rerun()

elif st.session_state.tela == "lista_usuarios":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>MEMBROS</h1>", unsafe_allow_html=True)
    usrs = carregar_usuarios()
    for u, c in usrs.items():
        col_t, col_d = st.columns([0.8, 0.2])
        col_t.markdown(f'<div style="background:#1a1a1a; padding:10px; border-radius:5px; border-left:3px solid #E50914;">{u} - {c}</div>', unsafe_allow_html=True)
        if col_d.button("🗑️", key=u): remover_usuario_do_arquivo(u); st.rerun()
    if st.button("VOLTAR"): st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ACESSO ADM</h1>", unsafe_allow_html=True)
    senha_m = st.text_input("Senha Master", type="password")
    if st.button("ENTRAR ADM", use_container_width=True):
        if senha_m == "55420":
            st.session_state.autenticado = True; st.session_state.tela = "master"; st.rerun()
