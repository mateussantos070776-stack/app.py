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

# 3. CSS PREMIUM
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;900&display=swap');
    
    [data-testid="stHeader"], [data-testid="sidebar-button"] { display: none !important; }
    
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    
    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        height: 48px !important;
    }
    
    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 2px solid #E50914 !important;
    }

    .card-master {
        background: rgba(15, 15, 15, 1);
        border: 1px solid #333;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        margin-bottom: 20px;
        min-height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .card-title-master {
        color: #E50914;
        font-weight: 900;
        font-size: 1.1rem;
        text-transform: uppercase;
        margin-bottom: 15px;
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

# 5. LÓGICA DE TELAS (PAINEL MASTER SEM HISTÓRICO)

if st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900; margin-bottom:30px;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    
    col_m1, col_m2, col_m3 = st.columns(3)
    
    with col_m1:
        st.markdown('<div class="card-master">', unsafe_allow_html=True)
        st.markdown('<div class="card-title-master">🔑 Gerador de Acesso</div>', unsafe_allow_html=True)
        st.write("Crie chaves de acesso únicas para novos membros.")
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
        st.write("Atualize o mural de avisos da Área de Membros.")
        novo_aviso = st.text_area("Texto do Aviso", placeholder="Digite aqui...", label_visibility="collapsed", height=100)
        if st.button("PUBLICAR AVISO", use_container_width=True):
            st.success("Mural atualizado!")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_m3:
        st.markdown('<div class="card-master">', unsafe_allow_html=True)
        st.markdown('<div class="card-title-master">🔔 Notificar Membro</div>', unsafe_allow_html=True)
        st.write("Envie notificações diretas para os dispositivos.")
        st.text_input("Assunto", placeholder="Ex: Urgente...", label_visibility="collapsed")
        if st.button("ENVIAR ALERTA", use_container_width=True):
            st.warning("Notificação enviada!")
        st.markdown('</div>', unsafe_allow_html=True)

# Lógica das outras telas (Home, Login) permanece igual para manter a navegação ativa.
elif st.session_state.tela == "home":
    st.markdown('<h1 style="font-family:serif; font-size:4.5rem; color:#E50914; text-align:center;">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    col_h1, col_h2, col_h3 = st.columns([1, 1.5, 1])
    with col_h2:
        entrada = st.text_input("ACESSO", placeholder="CHAVE SAGRADA", type="password")
        if st.button("ENTRAR", use_container_width=True):
            if entrada == "55420":
                st.session_state.tela = "master"
                st.rerun()
            elif entrada in listar_chaves():
                st.session_state.tela = "painel_membro"
                st.rerun()
