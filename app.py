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
    # Valida formato (XX) 9XXXX-XXXX ou apenas números com 11 dígitos
    padrao = r"^\(?\d{2}\)?\s?9\d{4}-?\d{4}$"
    return re.match(padrao, tel)

# 2. CSS
st.markdown("""
    <style>
    [data-testid="stHeader"] { background-color: rgba(0,0,0,0) !important; }
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #E50914 !important; }
    
    .stTextInput input { 
        background-color: white !important; 
        color: black !important; 
        border: 1px solid #ccc !important;
        font-weight: 500 !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        border: none !important;
        padding: 15px 10px !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border-radius: 8px !important;
        width: 100% !important;
    }

    .secao-titulo { color: #E50914; font-weight: 900; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 2px; }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVEGAÇÃO
def render_menu():
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>FERRAMENTAS</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN"): st.session_state.tela = "login_admin"; st.rerun()

with st.sidebar:
    render_menu()

with st.expander("📱 MENU DE NAVEGAÇÃO RÁPIDA"):
    render_menu()

# 4. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:3.5rem; color:#E50914; text-align:center; margin-top:80px; font-weight:900;">SEJA BEM-VINDO A EQUIPE MIDIA...</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; margin-top:30px;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col_login, _ = st.columns([1, 2, 1])
    with col_login:
        nome = st.text_input("Nome Completo")
        telefone = st.text_input("Número de Telefone (DDD + Número)", placeholder="Ex: 11912345678")
        chave = st.text_input("Chave de Acesso", type="password")
        
        if st.button("ENTRAR"):
            if not nome or len(nome.split()) < 2:
                st.error("Por favor, insira seu nome completo.")
            elif not validar_telefone(telefone):
                st.error("Formato de telefone inválido! Use: DDD + Número com dígito 9.")
            elif chave in listar_chaves() or chave == "55420":
                st.success(f"Bem-vindo, {nome}!")
                st.session_state.tela = "painel_membro"; st.rerun()
            else:
                st.error("Chave de acesso incorreta.")

elif st.session_state.tela == "painel_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>CENTRAL DO MEMBRO</h1>", unsafe_allow_html=True)
    # Conteúdo da central permanece o mesmo...
    st.write("<br>", unsafe_allow_html=True)
    _, central_grid, _ = st.columns([0.1, 0.8, 0.1])
    with central_grid:
        m1, m2 = st.columns(2)
        m1.button("📅 ESCALAS")
        m2.button("🕒 HORÁRIOS")
        m3, m4 = st.columns(2)
        m3.button("🛠️ EQUIPAMENTOS")
        m4.button("🗓️ DIAS")

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
    # Área Master permanece a mesma...
    t1, t2, t3 = st.columns(3)
    t1.markdown('<p class="secao-titulo">🔑 Gerador</p>', unsafe_allow_html=True)
    t2.markdown('<p class="secao-titulo">📢 Mural</p>', unsafe_allow_html=True)
    t3.markdown('<p class="secao-titulo">🔔 Notif.</p>', unsafe_allow_html=True)
    
    w1, w2, w3 = st.columns(3)
    with w1: st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "...", language="text")
    with w2: st.text_area("Aviso", height=68, label_visibility="collapsed")
    with w3: st.text_input("Notif", label_visibility="collapsed")

    if st.button("✨ GERAR NOVA CHAVE"):
        st.session_state.chave_gerada = "".join([str(random.randint(0, 9)) for _ in range(10)])
        salvar_chave(st.session_state.chave_gerada); st.rerun()

    st.write("---")
    if st.button("⬅️ VOLTAR"): st.session_state.tela = "home"; st.rerun()
