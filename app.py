import streamlit as st
import os
import random
import json
import string

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

def salvar_usuario_no_arquivo(id_usuario, chave):
    usuarios = carregar_usuarios()
    usuarios[id_usuario] = chave
    with open("usuarios_kerigma.json", "w") as f:
        json.dump(usuarios, f)

def remover_usuario_do_arquivo(id_para_remover):
    usuarios = carregar_usuarios()
    if id_para_remover in usuarios:
        del usuarios[id_para_remover]
        with open("usuarios_kerigma.json", "w") as f:
            json.dump(usuarios, f)

# --- INICIALIZAÇÃO DE ESTADOS ---
if 'tela' not in st.session_state: 
    st.session_state.tela = "home"
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'chave_gerada' not in st.session_state: 
    st.session_state.chave_gerada = ""
if 'id_gerado' not in st.session_state: 
    st.session_state.id_gerado = ""
if 'texto_mural' not in st.session_state:
    st.session_state.texto_mural = "Bem-vindo à Equipe Mídia Maanaim"

# 2. CSS MASTER (CORREÇÃO DEFINITIVA DA SIDEBAR)
st.markdown("""
    <style>
    /* Esconder elementos desnecessários */
    header {visibility: hidden;}
    [data-testid="sidebar-button"] {display: none !important;}
    
    /* FORÇAR SIDEBAR FIXA E COM BORDA */
    section[data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 2px solid #E50914 !important;
        min-width: 260px !important;
        max-width: 260px !important;
        transition: none !important;
    }
    
    /* Impedir que o conteúdo principal empurre a barra */
    section[data-testid="stSidebar"] > div {
        width: 260px !important;
    }

    .stApp { background-color: #050505; }
    
    /* BOTÕES DA SIDEBAR (GRADIENTE KERIGMA) */
    .stSidebar .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100% !important;
        margin-bottom: 10px !important;
    }

    /* INPUTS E TEXTOS */
    .stTextInput input { background-color: white !important; color: black !important; font-weight: 600 !important; }
    h1, h2, h3, p, span, label { color: white !important; font-family: 'Montserrat', sans-serif; }
    
    /* QUADRO ADM */
    .box-geracao {
        background-color: #111;
        padding: 25px;
        border: 1px dashed #E50914;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (FIXA)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900; margin-bottom:0;'>SISTEMA</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white; text-align:center; font-weight:900; margin-top:0;'>KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("🏠 HOME"): 
        st.session_state.tela = "home"; st.rerun()
    
    if st.button("🔴 MEMBROS MÍDIA"): 
        st.session_state.tela = "painel_membro" if st.session_state.autenticado else "login_membro"
        st.rerun()
        
    if st.button("⚙️ KERIGMA ADM"): 
        st.session_state.tela = "master" if st.session_state.autenticado else "login_admin"
        st.rerun()
    
    if st.session_state.autenticado:
        st.write("---")
        if st.button("🚪 SAIR DA CONTA"):
            st.session_state.autenticado = False; st.session_state.tela = "home"; st.rerun()
    st.write("---")

# 4. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 style="color:#E50914; text-align:center; margin-top:50px; font-weight:900;">EQUIPE MIDIA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align:center; margin-top:30px; padding:40px; border:1px solid #E50914; border-radius:10px;"><p style="color:#E50914; font-weight:bold; font-size:12px;">MURAL DE AVISOS</p><h2 style="font-weight:300;">{st.session_state.texto_mural}</h2></div>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>IDENTIFICAÇÃO</h1>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        user_input = st.text_input("ID DO USUÁRIO").strip().upper()
        chave_i = st.text_input("CHAVE", type="password").strip()
        if st.button("ENTRAR", use_container_width=True):
            usuarios = carregar_usuarios()
            if user_input in usuarios and usuarios[user_input] == chave_i:
                st.session_state.autenticado = True; st.session_state.tela = "painel_membro"; st.rerun()
            else:
                st.error("Credenciais não encontradas ou incorretas.")

elif st.session_state.tela == "master":
    if not st.session_state.autenticado: st.session_state.tela = "login_admin"; st.rerun()
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>PAINEL ADM</h1>", unsafe_allow_html=True)
    st.write("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<h3 style='text-align:center;'>🔑 Gerar Credenciais</h3>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="box-geracao">
            <p style="color:#888; margin:0; font-size: 14px;">NOVO ID</p>
            <h2 style="color:white; margin:0; letter-spacing: 2px;">{st.session_state.id_gerado if st.session_state.id_gerado else '------'}</h2>
            <p style="color:#888; margin:15px 0 0 0; font-size: 14px;">CHAVE</p>
            <h2 style="color:white; margin:0; letter-spacing: 2px;">{st.session_state.chave_gerada if st.session_state.chave_gerada else '------'}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("GERAR E AUTORIZAR", use_container_width=True):
            st.session_state.id_gerado = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            st.session_state.chave_gerada = ''.join(random.choices(string.digits, k=6))
            salvar_usuario_no_arquivo(st.session_state.id_gerado, st.session_state.chave_gerada)
            st.rerun()
            
    with c2:
        st.markdown("<h3 style='text-align:center;'>👥 Banco de Membros</h3>", unsafe_allow_html=True)
        if st.button("GERENCIAR LISTA ATUAL", use_container_width=True):
            st.session_state.tela = "lista_usuarios"; st.rerun()

elif st.session_state.tela == "lista_usuarios":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>Membros Autorizados</h1>", unsafe_allow_html=True)
    usrs = carregar_usuarios()
    for u, c in usrs.items():
        col_t, col_d = st.columns([0.85, 0.15])
        col_t.markdown(f'<div style="background-color:#1a1a1a; padding:12px; border-radius:5px; border-left:4px solid #E50914; margin-bottom:8px;">ID: <b>{u}</b> <span style="color:#E50914; float:right;">CHAVE: {c}</span></div>', unsafe_allow_html=True)
        if col_d.button("🗑️", key=f"del_{u}"): remover_usuario_do_arquivo(u); st.rerun()
    if st.button("VOLTAR"): st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "painel_membro":
    st.markdown('<div style="border: 2px solid #E50914; border-radius: 15px; padding: 80px; text-align: center; background-color: #080808; margin-top: 50px;"><h1 style="color:#E50914; font-size:45px; font-weight:900;">ACESSO LIBERADO</h1><p style="font-size:20px;">Você está conectado à rede Kerigma.</p></div>', unsafe_allow_html=True)

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>LOGIN LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1, 1])
    with col_adm:
        senha_m = st.text_input("Senha Master", type="password")
        if st.button("ENTRAR ADM", use_container_width=True):
            if senha_m == "55420":
                st.session_state.autenticado = True; st.session_state.tela = "master"; st.rerun()
            else: st.error("Senha Master incorreta.")
