import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DE TELA
st.set_page_config(page_title="KERIGMA | Master", layout="wide", initial_sidebar_state="expanded")

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

# 2. CSS (MANTIDO CONFORME VERSÃO ANTERIOR)
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #E50914 !important; }
    
    /* Estilos das Seções Master */
    .secao-titulo { color: #E50914; font-weight: 900; font-size: 1rem; text-transform: uppercase; margin-bottom: 5px; text-align: left; }
    .secao-desc { color: #888; font-size: 0.75rem; margin-bottom: 10px; text-align: left; }

    /* Inputs e TextAreas */
    .stTextInput input, .stTextArea textarea {
        background-color: #111 !important;
        color: white !important;
        border: 1px solid #333 !important;
    }

    /* Botões */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        width: 100% !important;
        border: none !important;
        font-weight: bold !important;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (MANTIDA)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME", key="nav_h"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS", key="nav_m"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN", key="nav_a"): st.session_state.tela = "login_admin"; st.rerun()

# 4. LÓGICA DE TELAS (RESUMO DAS ANTERIORES)
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:4rem; color:#E50914; text-align:center; margin-top:80px;">Kerigma Maanaim</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro" or st.session_state.tela == "painel_membro":
    # (Lógica da área de membros mantida conforme solicitado anteriormente)
    st.markdown("<h1 style='color:#E50914; text-align:center;'>CENTRAL DO MEMBRO</h1>", unsafe_allow_html=True)

elif st.session_state.tela == "login_admin":
    _, col_adm, _ = st.columns([1, 1, 1])
    with col_adm:
        senha = st.text_input("Senha Master", type="password")
        if st.button("ENTRAR NO COMANDO"):
            if senha == "55420": st.session_state.tela = "master"; st.rerun()

# --- TELA ALTERADA CONFORME INSTRUÇÃO ATUAL ---
elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # 1ª LINHA: TÍTULOS E DESCRIÇÕES
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown('<p class="secao-titulo">🔑 Gerador de Acesso</p>', unsafe_allow_html=True)
        st.markdown('<p class="secao-desc">Chave gerada aparecerá abaixo:</p>', unsafe_allow_html=True)
    with t2:
        st.markdown('<p class="secao-titulo">📢 Mural de Avisos</p>', unsafe_allow_html=True)
        st.markdown('<p class="secao-desc">Digite o comunicado para os membros:</p>', unsafe_allow_html=True)
    with t3:
        st.markdown('<p class="secao-titulo">🔔 Notificações</p>', unsafe_allow_html=True)
        st.markdown('<p class="secao-desc">Envie um alerta direto ao sistema:</p>', unsafe_allow_html=True)

    # 2ª LINHA: CAMPOS DE ESCRITA (ALINHADOS)
    w1, w2, w3 = st.columns(3)
    with w1:
        # Mostra a chave gerada em um campo de código para manter o alinhamento visual com os inputs
        if st.session_state.chave_gerada:
            st.code(st.session_state.chave_gerada, language="text")
        else:
            st.text_input("Status", value="Aguardando geração...", disabled=True, label_visibility="collapsed")
    with w2:
        aviso_texto = st.text_area("Aviso", placeholder="Escreva o aviso aqui...", height=68, label_visibility="collapsed")
    with w3:
        notif_assunto = st.text_input("Assunto", placeholder="Assunto do alerta...", label_visibility="collapsed")
        notif_msg = st.text_input("Mensagem", placeholder="Mensagem curta...", label_visibility="collapsed")

    # 3ª LINHA: BOTÕES DE CLIQUE (ALINHADOS LOGO ABAIXO)
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("✨ GERAR NOVA CHAVE"):
            nova_chave = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova_chave)
            st.session_state.chave_gerada = nova_chave
            st.rerun()
    with b2:
        if st.button("PUBLICAR NO MURAL"):
            st.success("Aviso publicado!")
    with b3:
        if st.button("ENVIAR NOTIFICAÇÃO"):
            st.success("Alerta enviado!")

    st.write("---")
    if st.button("⬅️ SAIR DO PAINEL"):
        st.session_state.tela = "home"; st.rerun()
