import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO INICIAL
st.set_page_config(
    page_title="KERIGMA | Central Master", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicialização de estados
if 'tela' not in st.session_state:
    st.session_state.tela = "master"
if 'chave_gerada' not in st.session_state:
    st.session_state.chave_gerada = ""

# 2. CSS PARA LIMPEZA TOTAL E ALINHAMENTO (SEM QUADRADOS PRETOS)
st.markdown("""
    <style>
    /* REMOVE ELEMENTOS DESNECESSÁRIOS */
    [data-testid="stHeader"], [data-testid="sidebar-button"], [data-testid="stVerticalBlock"] > div:empty {
        display: none !important;
    }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }

    /* BARRA LATERAL */
    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 2px solid #E50914 !important;
    }

    /* JANELAS MASTER LIMPAS E ALINHADAS */
    .card-master-final {
        background: #111111;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 25px;
        height: 350px; /* Altura fixa para simetria total */
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        transition: 0.3s;
    }

    .card-master-final:hover {
        border-color: #E50914;
    }

    .title-red {
        color: #E50914;
        font-weight: 900;
        font-size: 1.1rem;
        text-transform: uppercase;
        margin-bottom: 5px;
        text-align: center;
    }

    .desc-gray {
        font-size: 0.85rem;
        color: #888;
        text-align: center;
        margin-bottom: 20px;
    }

    /* ESTILIZAÇÃO DE INPUTS PARA FICAREM DISCRETOS */
    .stTextInput input, .stTextArea textarea {
        background-color: #1a1a1a !important;
        color: white !important;
        border: 1px solid #333 !important;
    }

    /* BOTÃO PADRÃO KERIGMA */
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

# 3. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    st.button("🏠 HOME", use_container_width=True)
    st.button("🔴 ÁREA DE MEMBROS", use_container_width=True)
    st.button("⚙️ ACESSO ADMIN", use_container_width=True)

# 4. PAINEL CENTRAL (SEM OS BLOCOS PRETOS DAS IMAGENS)
st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card-master-final">', unsafe_allow_html=True)
    st.markdown('<p class="title-red">🔑 Gerador de Acesso</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-gray">Crie chaves únicas para novos membros</p>', unsafe_allow_html=True)
    st.write("###") # Espaçador
    if st.button("✨ GERAR NOVA CHAVE"):
        st.session_state.chave_gerada = "".join([str(random.randint(0, 9)) for _ in range(10)])
    
    if st.session_state.chave_gerada:
        st.info(f"Chave: {st.session_state.chave_gerada}")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card-master-final">', unsafe_allow_html=True)
    st.markdown('<p class="title-red">📢 Alterar Avisos</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-gray">Atualize o mural da área de membros</p>', unsafe_allow_html=True)
    aviso = st.text_area("Mensagem", placeholder="Digite o aviso...", height=100, label_visibility="collapsed")
    if st.button("PUBLICAR NO MURAL"):
        st.success("Mural atualizado!")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card-master-final">', unsafe_allow_html=True)
    st.markdown('<p class="title-red">🔔 Notificar Membro</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-gray">Envie um alerta para o dispositivo</p>', unsafe_allow_html=True)
    st.text_input("Assunto", placeholder="Assunto...", label_visibility="collapsed")
    st.text_input("Mensagem", placeholder="Mensagem curta...", label_visibility="collapsed")
    if st.button("ENVIAR NOTIFICAÇÃO"):
        st.warning("Alerta disparado!")
    st.markdown('</div>', unsafe_allow_html=True)
