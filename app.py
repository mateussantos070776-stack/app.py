import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DE TELA
st.set_page_config(page_title="KERIGMA | Master", layout="wide", initial_sidebar_state="expanded")

# Estados do sistema
if 'tela' not in st.session_state: st.session_state.tela = "master"
if 'chave_gerada' not in st.session_state: st.session_state.chave_gerada = ""

# 2. CSS AVANÇADO (EXTERMINANDO QUADRADOS PRETOS E ALINHANDO TUDO)
st.markdown("""
    <style>
    /* Limpeza de containers fantasmas do Streamlit */
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    [data-testid="stVerticalBlock"] > div:empty { display: none !important; }
    [data-testid="stVerticalBlock"] { gap: 0rem !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }

    /* Estilo da Barra Lateral */
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #E50914 !important; }

    /* CONTAINER UNIFICADO (SEM BLOCOS SOLTOS) */
    .central-comando {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 10px;
    }

    .card-fixo {
        background: #111;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        min-height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .t-red { color: #E50914; font-weight: 900; font-size: 1.1rem; text-transform: uppercase; margin-bottom: 5px; }
    .d-gray { color: #888; font-size: 0.8rem; margin-bottom: 15px; }

    /* Ajuste dos botões para não saírem do lugar */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        width: 100% !important;
        border: none !important;
        font-weight: bold !important;
        height: 42px !important;
    }
    
    /* Inputs discretos */
    input, textarea { background-color: #1a1a1a !important; color: white !important; border: 1px solid #333 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR FIXA
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    st.button("🏠 HOME", key="side_h")
    st.button("🔴 ÁREA DE MEMBROS", key="side_m")
    st.button("⚙️ ACESSO ADMIN", key="side_a")

# 4. PAINEL DE COMANDO (ESTRUTURA LIMPA)
st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
st.write("---")

# Criando as colunas reais do Streamlit sem containers de imagem
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card-fixo"><div class="t-red">🔑 Gerador de Acesso</div><div class="d-gray">Crie chaves únicas para novos membros</div>', unsafe_allow_html=True)
    if st.button("✨ GERAR NOVA CHAVE", key="gen"):
        st.session_state.chave_gerada = "".join([str(random.randint(0, 9)) for _ in range(10)])
    if st.session_state.chave_gerada:
        st.code(st.session_state.chave_gerada, language="text")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card-fixo"><div class="t-red">📢 Alterar Avisos</div><div class="d-gray">Atualize o mural da área de membros</div>', unsafe_allow_html=True)
    st.text_area("Aviso", placeholder="Escreva o aviso...", height=100, label_visibility="collapsed", key="txt_aviso")
    if st.button("PUBLICAR NO MURAL", key="pub"):
        st.success("Publicado!")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card-fixo"><div class="t-red">🔔 Notificar Membro</div><div class="d-gray">Envie um alerta para o dispositivo</div>', unsafe_allow_html=True)
    st.text_input("Assunto", placeholder="Assunto...", label_visibility="collapsed", key="not_ass")
    st.text_input("Mensagem", placeholder="Mensagem...", label_visibility="collapsed", key="not_msg")
    if st.button("ENVIAR NOTIFICAÇÃO", key="notif"):
        st.warning("Enviada!")
    st.markdown('</div>', unsafe_allow_html=True)
