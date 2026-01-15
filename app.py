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
    st.session_state.tela = "master" # Definido como master para visualização direta
if 'chave_gerada' not in st.session_state:
    st.session_state.chave_gerada = ""

# 2. CSS PARA REGULAR O ALINHAMENTO (REMOVENDO OS QUADRADOS)
st.markdown("""
    <style>
    /* REMOVE HEADER E SETA */
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }

    /* ESTILO DA BARRA LATERAL FIXA */
    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 2px solid #E50914 !important;
    }

    /* REGULAGEM DAS JANELAS (CARDS) */
    .card-master-fix {
        background: rgba(20, 20, 20, 1);
        border: 1px solid #333;
        border-radius: 15px;
        padding: 30px;
        margin-bottom: 10px;
        height: 380px; /* ALTURA FIXA PARA TODAS AS JANELAS */
        display: flex;
        flex-direction: column;
        justify-content: space-between; /* GARANTE QUE O BOTÃO FIQUE NA BASE */
    }

    .card-header {
        text-align: center;
    }

    .card-title-kerigma {
        color: #E50914;
        font-weight: 900;
        font-size: 1.2rem;
        text-transform: uppercase;
        margin-bottom: 5px;
    }

    .card-desc-kerigma {
        font-size: 0.85rem;
        color: #888;
        margin-bottom: 20px;
    }

    /* BOTÕES UNIFORMES */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        width: 100% !important;
        border: none !important;
        font-weight: bold !important;
        height: 45px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (FIXA CONFORME SOLICITADO)
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    st.button("🏠 HOME", use_container_width=True)
    st.button("🔴 ÁREA DE MEMBROS", use_container_width=True)
    st.button("⚙️ ACESSO ADMIN", use_container_width=True)

# 4. PAINEL MASTER ORGANIZADO (CENTRAL DE COMANDO)
st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
st.write("---")

col_1, col_2, col_3 = st.columns(3)

# COLUNA 1: GERADOR
with col_1:
    st.markdown('<div class="card-master-fix">', unsafe_allow_html=True)
    st.markdown('<div class="card-header"><div class="card-title-kerigma">🔑 Gerador de Acesso</div><div class="card-desc-kerigma">Crie chaves únicas para novos membros</div></div>', unsafe_allow_html=True)
    
    # Espaçamento para alinhar com os inputs das outras colunas
    st.write("") 
    if st.button("✨ GERAR NOVA CHAVE", key="btn_gen"):
        st.session_state.chave_gerada = "".join([str(random.randint(0, 9)) for _ in range(10)])
    
    if st.session_state.chave_gerada:
        st.code(st.session_state.chave_gerada, language="text")
    else:
        st.info("Aguardando geração...")
    st.markdown('</div>', unsafe_allow_html=True)

# COLUNA 2: AVISOS
with col_2:
    st.markdown('<div class="card-master-fix">', unsafe_allow_html=True)
    st.markdown('<div class="card-header"><div class="card-title-kerigma">📢 Alterar Avisos</div><div class="card-desc-kerigma">Atualize o mural da área de membros</div></div>', unsafe_allow_html=True)
    
    aviso_txt = st.text_area("Mensagem do Mural", placeholder="Digite o aviso aqui...", height=120, label_visibility="collapsed")
    
    if st.button("PUBLICAR NO MURAL", key="btn_aviso"):
        st.success("Mural atualizado!")
    st.markdown('</div>', unsafe_allow_html=True)

# COLUNA 3: NOTIFICAR
with col_3:
    st.markdown('<div class="card-master-fix">', unsafe_allow_html=True)
    st.markdown('<div class="card-header"><div class="card-title-kerigma">🔔 Notificar Membro</div><div class="card-desc-kerigma">Envie um alerta direto para o dispositivo</div></div>', unsafe_allow_html=True)
    
    assunto = st.text_input("Assunto do Alerta", placeholder="Ex: Urgente...")
    msg_alerta = st.text_input("Mensagem Curta", placeholder="Ex: Reunião às 19h")
    
    if st.button("ENVIAR NOTIFICAÇÃO", key="btn_notif"):
        st.warning("Alerta disparado!")
    st.markdown('</div>', unsafe_allow_html=True)
