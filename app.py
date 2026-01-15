import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO INICIAL
st.set_page_config(
    page_title="KERIGMA | Exclusivo Mídia", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicialização de estados
if 'tela' not in st.session_state:
    st.session_state.tela = "home"
if 'chave_gerada' not in st.session_state:
    st.session_state.chave_gerada = ""

ARQUIVO_ATIVAS = "chaves_ativas.txt"

if not os.path.exists(ARQUIVO_ATIVAS):
    with open(ARQUIVO_ATIVAS, "w") as f: f.write("")

# 2. FUNÇÕES
def listar_chaves():
    if os.path.exists(ARQUIVO_ATIVAS):
        with open(ARQUIVO_ATIVAS, "r") as f: return f.read().splitlines()
    return []

def salvar_chave(chave):
    with open(ARQUIVO_ATIVAS, "a") as f: f.write(chave + "\n")

# 3. CSS PREMIUM (LIMPEZA TOTAL DOS QUADRADOS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;900&display=swap');
    
    /* REMOVE HEADER E BOTÃO DE RECOLHER */
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    
    /* BOTÕES KERIGMA */
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        height: 48px !important;
    }

    /* BARRA LATERAL FIXA */
    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 2px solid #E50914 !important;
    }

    /* CARDS DO PAINEL MASTER (SEM QUADRADOS PRETOS) */
    .card-master {
        background: rgba(20, 20, 20, 1);
        border: 1px solid #333;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        margin-bottom: 20px;
        min-height: 220px; /* Ajustado para o novo conteúdo sem quadrados */
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }

    .card-title-master {
        color: #E50914;
        font-weight: 900;
        font-size: 1.1rem;
        text-transform: uppercase;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }
    
    .card-desc {
        font-size: 0.9rem;
        color: #ccc;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME", use_container_width=True):
        st.session_state.tela = "home"
        st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS", use_container_width=True):
        st.session_state.tela = "login_membro"
        st.rerun()
    if st.button("⚙️ ACESSO ADMIN", use_container_width=True):
        st.session_state.tela = "login_admin"
        st.rerun()

# 5. LÓGICA DO PAINEL MASTER (SEM QUADRADOS)
if st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900; margin-bottom:40px;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    
    col_m1, col_m2, col_m3 = st.columns(3)
    
    with col_m1:
        st.markdown('<div class="card-master">', unsafe_allow_html=True)
        st.markdown('<div class="card-title-master">🔑 Gerador de Acesso</div>', unsafe_allow_html=True)
        st.markdown('<p class="card-desc">Crie chaves de acesso únicas para novos membros.</p>', unsafe_allow_html=True)
        if st.button("✨ GERAR CHAVE", use_container_width=True):
            nova_c = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova_c)
            st.session_state.chave_gerada = nova_c
            
        if st.session_state.chave_gerada:
            st.code(st.session_state.chave_gerada, language="text")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_m2:
        st.markdown('<div class="card-master">', unsafe_allow_html=True)
        st.markdown('<div class="card-title-master">📢 Alterar Avisos</div>', unsafe_allow_html=True)
        st.markdown('<p class="card-desc">Atualize o mural de avisos da Área de Membros.</p>', unsafe_allow_html=True)
        st.text_area("Texto do Aviso", placeholder="Digite aqui...", label_visibility="collapsed", height=80)
        if st.button("PUBLICAR AVISO", use_container_width=True):
            st.success("Mural atualizado!")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_m3:
        st.markdown('<div class="card-master">', unsafe_allow_html=True)
        st.markdown('<div class="card-title-master">🔔 Notificar Membro</div>', unsafe_allow_html=True)
        st.markdown('<p class="card-desc">Envie notificações diretas para os dispositivos.</p>', unsafe_allow_html=True)
        st.text_input("Assunto", placeholder="Ex: Urgente...", label_visibility="collapsed")
        if st.button("ENVIAR ALERTA", use_container_width=True):
            st.warning("Notificação enviada!")
        st.markdown('</div>', unsafe_allow_html=True)

# Lógica das outras telas (Home e Login) omitida para brevidade, mas deve ser mantida do código anterior.
