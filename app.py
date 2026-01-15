import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="KERIGMA MAANAIM | Área Restrita",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded" # Inicia com a barra lateral visível para o login
)

# 2. CSS PARA ESTILO IMPECÁVEL E BOTÃO LATERAL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;900&display=swap');

    .stApp {
        background: radial-gradient(circle at 50% -20%, #1a1a1a 0%, #000000 100%);
        color: #f5f5f5;
        font-family: 'Montserrat', sans-serif;
    }

    /* Estilização da Sidebar (Barra Lateral) */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 15, 15, 0.95);
        border-right: 1px solid rgba(229, 9, 20, 0.2);
        min-width: 350px !important;
    }

    /* Título na Sidebar */
    .sidebar-title {
        color: #E50914;
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 20px;
        text-transform: uppercase;
        text-align: center;
    }

    /* Título Principal Central */
    .main-title {
        font-weight: 900;
        font-size: 4rem;
        color: #E50914;
        text-transform: uppercase;
        text-align: center;
        margin-top: 100px;
        background: linear-gradient(180deg, #ff1e1e 0%, #a80000 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 15px rgba(229, 9, 20, 0.3));
    }

    /* Botão de Validação */
    div.stButton > button {
        background: #E50914 !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 5px !important;
        width: 100%;
        height: 45px;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background: #ff1e2d !important;
        box-shadow: 0 0 20px rgba(229, 9, 20, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE ESTADO E CHAVE DE ACESSO
CHAVE_MESTRA = "1234567890" # Defina aqui a sua chave de 10 dígitos

if 'membro_logado' not in st.session_state:
    st.session_state.membro_logado = False

# 4. BARRA LATERAL (ACESSAR CREDENCIAL)
with st.sidebar:
    st.markdown('<p class="sidebar-title">🔐 Acesso Integrante</p>', unsafe_allow_html=True)
    st.image("https://lh3.googleusercontent.com/d/1B8LjYZmHsjpyZPC96FaYAODskWrwOVJC", use_container_width=True)
    
    with st.expander("Digitar Chave de Acesso"):
        chave_input = st.text_input("Insira os 10 dígitos", type="password", help="Chave exclusiva para equipe de mídia.")
        
        if st.button("Validar Credencial"):
            if chave_input == CHAVE_MESTRA:
                st.session_state.membro_logado = True
                st.success("Acesso Autorizado!")
                st.rerun()
            else:
                st.error("Chave inválida.")

    if st.session_state.membro_logado:
        st.write("---")
        st.info("Você está no modo: **EDITORA DE MÍDIA**")
        if st.button("Sair do Sistema"):
            st.session_state.membro_logado = False
            st.rerun()

# 5. CONTEÚDO PRINCIPAL
if not st.session_state.membro_logado:
    # Tela de espera/pública
    st.markdown('<h1 class="main-title">KERIGMA<br>MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing:8px; color:#666;'>DIGITAL MEDIA HUB</p>", unsafe_allow_html=True)
    
    st.write("##")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.warning("⚠️ Utilize a barra lateral à esquerda para acessar com sua chave de 10 dígitos.")

else:
    # TELA EXCLUSIVA PARA QUEM TEM A CHAVE
    st.markdown('<h1 style="color:#E50914;">PAINEL DE MÍDIA KERIGMA</h1>', unsafe_allow_html=True)
    st.write("---")
    
    # Exemplo de Dashboard Profissional
    c1, c2, c3 = st.columns(3)
    c1.metric("Vídeos Ativos", "42")
    c2.metric("Uploads Pendentes", "5")
    c3.metric("Espaço em Nuvem", "85%")
    
    st.write("### 🎬 Gerenciamento de Conteúdo")
    st.file_uploader("Enviar novo arquivo de vídeo (MP4, MKV)")
    
    st.table({
        "Arquivo": ["Culto_Domingo.mp4", "Estudo_Jeremias.mp4", "Intro_Maanaim.mov"],
        "Status": ["Processado", "Em edição", "Aguardando"],
        "Data": ["10/01", "12/01", "14/01"]
    })
