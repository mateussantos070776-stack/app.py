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

# 2. CSS MASTER (RESTAURAÇÃO TOTAL DA BARRA LATERAL)
st.markdown("""
    <style>
    /* Remover cabeçalhos e ajustar espaçamento */
    header {visibility: hidden;}
    .block-container { padding-top: 1rem !important; }
    
    /* RESTAURAÇÃO DA SIDEBAR (PC E MOBILE) */
    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 2px solid #E50914 !important; /* LINHA VERMELHA */
        min-width: 260px !important;
        max-width: 260px !important;
        display: block !important;
    }

    /* OCULTAR O BOTÃO DE SETA QUE ESCONDE A BARRA */
    [data-testid="sidebar-button"], 
    button[title="Collapse sidebar"], 
    button[title="Expand sidebar"] {
        display: none !important;
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
        margin-bottom: 10px !important;
    }

    /* ESTILO DE TÍTULOS E TEXTOS */
    h1, h2, h3, p, label { color: white !important; font-family: 'Montserrat', sans-serif; }
    
    /* INPUTS BRANCOS */
    .stTextInput input { 
        background-color: white !important; 
        color: black !important; 
        font-weight: 600 !important; 
    }

    /* QUADRO DE AVISOS HOME */
    .mural-avisos {
        text-align: center; 
        margin-top: 30px; 
        padding: 40px; 
        border: 1px solid #E50914; 
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTEÚDO DA BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
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

# 4. LÓGICA DE TELAS (CONTEÚDO PRINCIPAL)
if st.session_state.tela == "home":
    st.markdown('<h1 style="color:#E50914; text-align:center; margin-top:50px; font-weight:900;">EQUIPE MIDIA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown(f'''
        <div class="mural-avisos">
            <p style="color:#E50914; font-weight:bold; font-size:12px;">MURAL DE AVISOS</p>
            <h2 style="font-weight:300;">{st.session_state.texto_mural}</h2>
        </div>
    ''', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ACESSO À CENTRAL</h1>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        user_input = st.text_input("ID DE USUÁRIO (ALFANUMÉRICO)").strip().upper()
        chave_i = st.text_input("CHAVE (NUMÉRICA)", type="password").strip()
        if st.button("ENTRAR", use_container_width=True):
            reg = carregar_usuarios()
            if user_input in reg and reg[user_input] == chave_i:
                st.session_state.autenticado = True; st.session_state.tela = "painel_membro"; st.rerun()
            else:
                st.error("Credenciais inválidas. Fale com seu ADM.")

elif st.session_state.tela == "master":
    if not st.session_state.autenticado: st.session_state.tela = "login_admin"; st.rerun()
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>PAINEL ADM</h1>", unsafe_allow_html=True)
    st.write("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<h3 style='text-align:center;'>🔑 Gerar Credenciais</h3>", unsafe_allow_html=True)
        st.markdown(f"""
            <div style="background-color:#1a1a1a; padding:20px; border-radius:10px; border:1px solid #E50914; text-align:center;">
                <p style="color:#888; margin:0;">USUÁRIO ID</p>
                <h2 style="color:white; margin:0;">{st.session_state.id_gerado if st.session_state.id_gerado else '---'}</h2>
                <p style="color:#888; margin:10px 0 0 0;">CHAVE</p>
                <h2 style="color:white; margin:0;">{st.session_state.chave_gerada if st.session_state.chave_gerada else '---'}</h2>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("GERAR NOVO ACESSO", use_container_width=True):
            st.session_state.id_gerado = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            st.session_state.chave_gerada = ''.join(random.choices(string.digits, k=6))
            salvar_usuario_no_arquivo(st.session_state.id_gerado, st.session_state.chave_gerada)
            st.rerun()
            
    with c2:
        st.markdown("<h3 style='text-align:center;'>👥 Membros</h3>", unsafe_allow_html=True)
        if st.button("LISTAR USUÁRIOS ATIVOS", use_container_width=True):
            st.session_state.tela = "lista_usuarios"; st.rerun()

elif st.session_state.tela == "lista_usuarios":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>MEMBROS CADASTRADOS</h1>", unsafe_allow_html=True)
    usrs = carregar_usuarios()
    for u, c in usrs.items():
        col_t, col_d = st.columns([0.85, 0.15])
        col_t.markdown(f'<div style="background-color:#1a1a1a; padding:10px; border-radius:5px; border-left:3px solid #E50914;">ID: <b>{u}</b> <span style="color:#888; float:right;">Chave: {c}</span></div>', unsafe_allow_html=True)
        if col_d.button("🗑️", key=u): remover_usuario_do_arquivo(u); st.rerun()
    if st.button("VOLTAR"): st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "painel_membro":
    st.markdown('<div style="border: 2px solid #E50914; border-radius: 15px; padding: 60px; text-align: center; background-color: #0a0a0a; margin-top: 100px;"><h1>MÍDIA LOGADA</h1><p>Equipe Maanaim - Kerigma</p></div>', unsafe_allow_html=True)

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ACESSO ADM</h1>", unsafe_allow_html=True)
    senha_m = st.text_input("Senha Master", type="password")
    if st.button("ENTRAR ADM", use_container_width=True):
        if senha_m == "55420":
            st.session_state.autenticado = True; st.session_state.tela = "master"; st.rerun()
