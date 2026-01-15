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

ARQUIVO_ATIVAS = "chaves_ativas.txt"
ARQUIVO_CHAT = "chat_log.txt"

for arq in [ARQUIVO_ATIVAS, ARQUIVO_CHAT]:
    if not os.path.exists(arq):
        with open(arq, "w", encoding="utf-8") as f: f.write("")

# --- FUNÇÕES ---
def listar_chaves():
    with open(ARQUIVO_ATIVAS, "r") as f: return [l.strip() for l in f.readlines()]

def salvar_chave(chave):
    with open(ARQUIVO_ATIVAS, "a") as f: f.write(chave + "\n")

def enviar_msg(remetente, texto):
    if texto:
        timestamp = datetime.now().strftime("%H:%M")
        with open(ARQUIVO_CHAT, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {remetente}: {texto}\n")

def ler_chat():
    if os.path.exists(ARQUIVO_CHAT):
        with open(ARQUIVO_CHAT, "r", encoding="utf-8") as f: return f.readlines()
    return []

# 2. CSS AJUSTADO PARA CELULAR
st.markdown("""
    <style>
    /* Remove o cabeçalho padrão mas mantém o botão do menu lateral no mobile */
    [data-testid="stHeader"] { background-color: rgba(0,0,0,0) !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #E50914 !important; }
    
    /* Inputs Brancos */
    .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border: 1px solid #ccc !important; }
    
    /* Botões Gerais */
    .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important; border: none !important; font-weight: 800 !important;
        text-transform: uppercase; border-radius: 8px !important; width: 100% !important;
    }

    /* Chat Styling */
    .chat-box { background-color: #111; border: 1px solid #333; border-radius: 10px; padding: 15px; height: 250px; overflow-y: auto; margin-bottom: 10px; }
    .msg { margin-bottom: 8px; font-size: 0.85rem; border-bottom: 1px solid #222; padding-bottom: 4px; }

    /* Estilos Master */
    .secao-titulo { color: #E50914; font-weight: 900; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 2px; }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVEGAÇÃO (SIDEBAR + SUPORTE MOBILE)
def navegacao():
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>FERRAMENTAS</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("💬 CHAT"): st.session_state.tela = "chat_membro"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN"): st.session_state.tela = "login_admin"; st.rerun()

with st.sidebar:
    navegacao()

# --- EXCLUSIVO PARA CELULAR (Menu rápido se a sidebar estiver fechada) ---
with st.expander("📱 MENU DE NAVEGAÇÃO RÁPIDA"):
    navegacao()

# 4. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:2.5rem; color:#E50914; text-align:center; margin-top:40px; font-weight:900;">SEJA BEM-VINDO A EQUIPE MIDIA...</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "chat_membro":
    st.markdown("<h3 style='color:#E50914; text-align:center;'>💬 CHAT AO VIVO</h3>", unsafe_allow_html=True)
    msgs = ler_chat()
    chat_html = "".join([f'<div class="msg">{m}</div>' for m in msgs])
    st.markdown(f'<div class="chat-box">{chat_html}</div>', unsafe_allow_html=True)
    input_msg = st.text_input("Sua mensagem...", key="in_mem")
    if st.button("ENVIAR"):
        enviar_msg("MEMBRO", input_msg); st.rerun()

elif st.session_state.tela == "login_membro":
    st.markdown("<h2 style='color:#E50914; text-align:center;'>ÁREA DE MEMBROS</h2>", unsafe_allow_html=True)
    chave = st.text_input("Chave", type="password")
    if st.button("ENTRAR"):
        if chave in listar_chaves() or chave == "55420":
            st.session_state.tela = "painel_membro"; st.rerun()

elif st.session_state.tela == "painel_membro":
    st.markdown("<h2 style='color:#E50914; text-align:center;'>CENTRAL DO MEMBRO</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.button("📅 ESCALAS")
    with c2: st.button("🕒 HORÁRIOS")
    c3, c4 = st.columns(2)
    with c3: st.button("🛠️ EQUIP.")
    with c4: st.button("🗓️ DIAS")

elif st.session_state.tela == "login_admin":
    st.markdown("<h2 style='color:#E50914; text-align:center;'>ACESSO LIDERANÇA</h2>", unsafe_allow_html=True)
    senha = st.text_input("Senha", type="password")
    if st.button("ACESSAR COMANDO"):
        if senha == "55420": st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL MASTER</h2>", unsafe_allow_html=True)
    
    # Grid Master (Ajustado para Mobile)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="secao-titulo">🔑 Chave</p>', unsafe_allow_html=True)
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "...", language="text")
        if st.button("✨ GERAR"):
            st.session_state.chave_gerada = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(st.session_state.chave_gerada); st.rerun()
    with col2:
        st.markdown('<p class="secao-titulo">📢 Avisos</p>', unsafe_allow_html=True)
        st.text_area("Aviso", height=68, label_visibility="collapsed")
        st.button("PUBLICAR")

    st.write("---")
    st.markdown('<p class="secao-titulo">💬 Resposta Chat</p>', unsafe_allow_html=True)
    msg_adm = st.text_input("Resposta", key="in_adm", label_visibility="collapsed")
    if st.button("RESPONDER"):
        enviar_msg("ADMIN", msg_adm); st.rerun()
    
    if st.button("⬅️ VOLTAR"): st.session_state.tela = "home"; st.rerun()
