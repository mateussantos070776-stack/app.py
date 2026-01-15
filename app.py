import streamlit as st
import os
import random
from PIL import Image
import io

# 1. CONFIGURAÇÃO INICIAL
st.set_page_config(page_title="KERIGMA | Exclusivo Mídia", layout="wide")

# Inicialização CRUCIAL do Session State (Evita o NameError)
if 'tela' not in st.session_state:
    st.session_state.tela = "home"
if 'sub_view' not in st.session_state:
    st.session_state.sub_view = None

PASTA_GALERIA = "galeria_kerigma"
ARQUIVO_ATIVAS = "chaves_ativas.txt"

if not os.path.exists(PASTA_GALERIA):
    os.makedirs(PASTA_GALERIA)

# 2. CSS PREMIUM
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    .card-janela {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #333;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        transition: 0.3s;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .card-janela:hover { border-color: #E50914; background: rgba(229, 9, 20, 0.1); }
    .main-title { font-weight: 900; font-size: 4rem; color: #E50914; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR (LOGS E ACESSO)
with st.sidebar:
    st.title("SISTEMA KERIGMA")
    if st.button("SAIR / INÍCIO"):
        st.session_state.tela = "home"
        st.session_state.sub_view = None
        st.rerun()

# 4. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 class="main-title">KERIGMA MAANAIM</h1>', unsafe_allow_html=True)
    col_entrar, _ = st.columns([1, 2])
    with col_entrar:
        chave = st.text_input("Insira sua Chave de Integrante", type="password")
        if st.button("ACESSAR EXCLUSIVO MÍDIA"):
            # Aqui você adicionaria sua lógica de conferir chaves.txt
            st.session_state.tela = "membro"
            st.rerun()

elif st.session_state.tela == "membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>EXCLUSIVO MÍDIA</h1>", unsafe_allow_html=True)
    st.write("---")

    # GRID 3x3 DE JANELAS
    # Linha 1
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card-janela"><h3>📸 FOTOS</h3><p>Galeria Coletiva</p></div>', unsafe_allow_html=True)
        if st.button("ABRIR", key="f1"): st.session_state.sub_view = "fotos"
    with c2:
        st.markdown('<div class="card-janela"><h3>🎥 VÍDEOS</h3><p>Brutos e Reels</p></div>', unsafe_allow_html=True)
        st.button("ABRIR", key="f2")
    with c3:
        st.markdown('<div class="card-janela"><h3>🎨 IDENTIDADE</h3><p>Logos e Branding</p></div>', unsafe_allow_html=True)
        st.button("ABRIR", key="f3")

    # Linha 2
    c4, c5, c6 = st.columns(3)
    with c4:
        st.markdown('<div class="card-janela"><h3>📝 ROTEIROS</h3><p>Scripts Cultos</p></div>', unsafe_allow_html=True)
        st.button("ABRIR", key="f4")
    with c5:
        st.markdown('<div class="card-janela"><h3>🎵 ÁUDIOS</h3><p>Trilhas e SFX</p></div>', unsafe_allow_html=True)
        st.button("ABRIR", key="f5")
    with c6:
        st.markdown('<div class="card-janela"><h3>🗓️ AGENDA</h3><p>Escala de Mídia</p></div>', unsafe_allow_html=True)
        st.button("ABRIR", key="f6")

    # ÁREA DE CONTEÚDO (Aparece abaixo do grid quando selecionado)
    if st.session_state.sub_view == "fotos":
        st.write("---")
        st.subheader("📸 Galeria de Fotos")
        # Aqui entra o seu código de listar os arquivos na pasta
        arquivos = os.listdir(PASTA_GALERIA)
        if not arquivos:
            st.info("Nenhuma foto disponível.")
        else:
            cols = st.columns(4)
            for i, img in enumerate(arquivos):
                with cols[i % 4]:
                    st.image(os.path.join(PASTA_GALERIA, img))
