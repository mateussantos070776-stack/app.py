import streamlit as st
import os
import random
import re

# 1. CONFIGURAÇÃO DE TELA
st.set_page_config(page_title="KERIGMA | Sistema", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE ESTADOS ---
if 'tela' not in st.session_state: 
    st.session_state.tela = "home"
if 'chave_gerada' not in st.session_state: 
    st.session_state.chave_gerada = ""

ARQUIVO_ATIVAS = "chaves_ativas.txt"
if not os.path.exists(ARQUIVO_ATIVAS):
    with open(ARQUIVO_ATIVAS, "w", encoding="utf-8") as f: f.write("")

# --- FUNÇÕES DE SISTEMA ---
def listar_chaves():
    with open(ARQUIVO_ATIVAS, "r", encoding="utf-8") as f: 
        return [linha.strip() for linha in f.readlines()]

def salvar_chave(chave):
    with open(ARQUIVO_ATIVAS, "a", encoding="utf-8") as f: 
        f.write(chave + "\n")

def validar_telefone(tel):
    padrao = r"^\(?\d{2}\)?\s?9\d{4}-?\d{4}$"
    return re.match(padrao, tel)

# 2. CSS MASTER
st.markdown("""
    <style>
    [data-testid="stHeader"] { background-color: rgba(0,0,0,0) !important; }
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #E50914 !important; }
    
    /* Campos de Escrita com Fundo Branco */
    .stTextInput input, .stTextArea textarea { 
        background-color: white !important; 
        color: black !important; 
        border: 1px solid #ccc !important;
        font-weight: 600 !important;
    }

    /* Botões Padrão Vermelhos */
    .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        border: none !important;
        padding: 12px 10px !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border-radius: 8px !important;
        width: 100% !important;
    }

    .secao-titulo { color: #E50914; font-weight: 900; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVEGAÇÃO (APENAS SIDEBAR)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>FERRAMENTAS</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN"): st.session_state.tela = "login_admin"; st.rerun()

# 4. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:3.5rem; color:#E50914; text-align:center; margin-top:80px; font-weight:900;">SEJA BEM-VINDO A EQUIPE MIDIA...</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 2, 1])
    with col_login:
        nome = st.text_input("Nome Completo")
        telefone = st.text_input("Número de Telefone (DDD + 9)")
        chave = st.text_input("Chave de Acesso", type="password")
        if st.button("ENTRAR"):
            if not nome or len(nome.split()) < 2: st.error("Insira o nome completo.")
            elif not validar_telefone(telefone): st.error("Telefone inválido (DDD + 9).")
            elif chave in listar_chaves() or chave == "55420":
                st.session_state.tela = "painel_membro"; st.rerun()

elif st.session_state.tela == "painel_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>CENTRAL DO MEMBRO</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.button("📅 ESCALAS")
    with c2: st.button("🕒 HORÁRIOS")
    c3, c4 = st.columns(2)
    with c3: st.button("🛠️ EQUIPAMENTOS")
    with c4: st.button("🗓️ DIAS")

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:50px;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 2, 1])
    with col_adm:
        senha = st.text_input("Senha", type="password")
        if st.button("ACESSAR COMANDO"):
            if senha == "55420": st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
    
    col_g, col_m, col_n = st.columns(3)

    with col_g:
        st.markdown('<p class="secao-titulo">🔑 Gerador</p>', unsafe_allow_html=True)
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "Aguardando...", language="text")
        if st.button("✨ GERAR NOVA CHAVE"):
            st.session_state.chave_gerada = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(st.session_state.chave_gerada); st.rerun()

    with col_m:
        st.markdown('<p class="secao-titulo">📢 Mural</p>', unsafe_allow_html=True)
        st.text_area("Aviso", placeholder="Digite o aviso...", height=68, label_visibility="collapsed")
        st.button("PUBLICAR NO MURAL")

    with col_n:
        st.markdown('<p class="secao-titulo">🔔 Notificações</p>', unsafe_allow_html=True)
        st.text_input("Notif", placeholder="Assunto...", label_visibility="collapsed")
        st.button("ENVIAR NOTIFICAÇÃO")

    st.write("<br>", unsafe_allow_html=True)
    if st.button("⬅️ VOLTAR"): st.session_state.tela = "home"; st.rerun()
