import streamlit as st
import os
import random
from datetime import datetime

# 1. CONFIGURAÇÃO DE TELA
st.set_page_config(page_title="KERIGMA | Sistema", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE ESTADOS E ARQUIVOS ---
if 'tela' not in st.session_state: 
    st.session_state.tela = "home"
if 'chave_gerada' not in st.session_state: 
    st.session_state.chave_gerada = ""

# Arquivos de Dados
ARQUIVO_ATIVAS = "chaves_ativas.txt"
ARQUIVO_CHAT = "chat_log.txt"

for arq in [ARQUIVO_ATIVAS, ARQUIVO_CHAT]:
    if not os.path.exists(arq):
        with open(arq, "w", encoding="utf-8") as f: f.write("")

# --- FUNÇÕES DE SISTEMA ---
def listar_chaves():
    with open(ARQUIVO_ATIVAS, "r") as f: 
        return [linha.strip() for linha in f.readlines()]

def salvar_chave(chave):
    with open(ARQUIVO_ATIVAS, "a") as f: f.write(chave + "\n")

def enviar_msg(remetente, texto):
    if texto:
        timestamp = datetime.now().strftime("%H:%M")
        with open(ARQUIVO_CHAT, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {remetente}: {texto}\n")

def ler_chat():
    if os.path.exists(ARQUIVO_CHAT):
        with open(ARQUIVO_CHAT, "r", encoding="utf-8") as f:
            return f.readlines()
    return []

# 2. CSS
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #E50914 !important; }
    .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border: 1px solid #ccc !important; }
    
    /* Estilo Chat */
    .chat-box { 
        background-color: #111; border: 1px solid #333; border-radius: 10px; 
        padding: 15px; height: 300px; overflow-y: auto; margin-bottom: 10px;
    }
    .msg { margin-bottom: 8px; font-size: 0.9rem; }
    .msg-adm { color: #E50914; font-weight: bold; }
    .msg-mem { color: #00ff00; font-weight: bold; }

    .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important; border: none !important; font-weight: 800 !important;
        text-transform: uppercase; border-radius: 8px !important; width: 100% !important;
    }
    .secao-titulo { color: #E50914; font-weight: 900; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 2px; }
    .secao-desc { color: #666; font-size: 0.7rem; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (NOVO BOTÃO CHAT ADICIONADO)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>FERRAMENTAS</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("💬 CHAT"): st.session_state.tela = "chat_membro"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN"): st.session_state.tela = "login_admin"; st.rerun()

# 4. LÓGICA DE TELAS

if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:3.5rem; color:#E50914; text-align:center; margin-top:80px; font-weight:900;">SEJA BEM-VINDO A EQUIPE MIDIA...</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "chat_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>CHAT COM ADMIN</h1>", unsafe_allow_html=True)
    _, chat_col, _ = st.columns([1, 2, 1])
    with chat_col:
        msgs = ler_chat()
        chat_html = "".join([f'<div class="msg">{m}</div>' for m in msgs])
        st.markdown(f'<div class="chat-box">{chat_html}</div>', unsafe_allow_html=True)
        
        input_msg = st.text_input("Sua mensagem...", key="input_mem")
        if st.button("ENVIAR MENSAGEM"):
            enviar_msg("MEMBRO", input_msg)
            st.rerun()

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
    _, central_grid, _ = st.columns([0.15, 0.7, 0.15])
    with central_grid:
        m1, m2, m3, m4 = st.columns(4)
        m1.button("📅 ESCALAS", key="b1")
        m2.button("🕒 HORÁRIOS", key="b2")
        m3.button("🛠️ EQUIPAMENTOS", key="b3")
        m4.button("🗓️ DIAS", key="b4")

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1, 1])
    with col_adm:
        senha = st.text_input("Senha", type="password")
        if st.button("ACESSAR COMANDO"):
            if senha == "55420": st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Camada Master Original + Chat
    t1, t2, t3, t4 = st.columns(4)
    t1.markdown('<p class="secao-titulo">🔑 Gerador</p>', unsafe_allow_html=True)
    t2.markdown('<p class="secao-titulo">📢 Mural</p>', unsafe_allow_html=True)
    t3.markdown('<p class="secao-titulo">🔔 Notif.</p>', unsafe_allow_html=True)
    t4.markdown('<p class="secao-titulo">💬 Chat com Membro</p>', unsafe_allow_html=True)

    w1, w2, w3, w4 = st.columns(4)
    with w1:
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "...", language="text")
    with w2:
        st.text_area("Aviso", height=68, label_visibility="collapsed")
    with w3:
        st.text_input("Notif", placeholder="Assunto...", label_visibility="collapsed")
    with w4:
        msgs_master = ler_chat()
        st.markdown(f'<div class="chat-box" style="height:68px; font-size:0.6rem;">{"".join(msgs_master[-3:])}</div>', unsafe_allow_html=True)

    b1, b2, b3, b4 = st.columns(4)
    with b1:
        if st.button("✨ GERAR"):
            st.session_state.chave_gerada = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(st.session_state.chave_gerada); st.rerun()
    with b2: st.button("PUBLICAR")
    with b3: st.button("ENVIAR")
    with b4:
        msg_adm = st.text_input("Resp. Chat", key="input_adm", label_visibility="collapsed")
        if st.button("RESPONDER"):
            enviar_msg("ADMIN", msg_adm); st.rerun()

    st.write("---")
    if st.button("⬅️ VOLTAR"): st.session_state.tela = "home"; st.rerun()
