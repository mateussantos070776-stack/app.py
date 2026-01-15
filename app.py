import streamlit as st

# 1. ORQUESTRAÇÃO DA PÁGINA
st.set_page_config(
    page_title="KERIGMA MAANAIM | Hub de Mídia",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS DE ALTA PERFORMANCE (UI/UX PREMIUM)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;900&display=swap');

    /* Background com textura de profundidade */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #1e1e1e 0%, #050505 100%);
        color: #f5f5f5;
        font-family: 'Montserrat', sans-serif;
    }

    /* Esconder elementos nativos */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}

    /* Logo Centralizada Animada */
    .logo-container {
        display: flex;
        justify-content: center;
        padding: 40px 0 10px 0;
    }
    
    .main-title {
        font-family: 'Montserrat', sans-serif;
        font-weight: 900;
        font-size: 3.5rem;
        letter-spacing: -3px;
        color: #E50914;
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 5px;
        background: linear-gradient(180deg, #ff1e1e 0%, #a80000 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 20px rgba(229, 9, 20, 0.3));
    }

    .tagline {
        font-size: 0.9rem;
        color: #888;
        text-align: center;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-bottom: 50px;
        font-weight: 300;
    }

    /* Card de Login Estilo Neumorphism Dark */
    .login-card {
        background: rgba(20, 20, 20, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 60px;
        box-shadow: 0 40px 100px rgba(0,0,0,0.8);
        backdrop-filter: blur(20px);
    }

    /* Inputs Estilizados */
    .stTextInput input {
        background-color: #1a1a1a !important;
        border: 1px solid #333 !important;
        color: white !important;
        border-radius: 10px !important;
        height: 55px !important;
        padding-left: 20px !important;
        font-size: 16px !important;
    }
    
    .stTextInput input:focus {
        border-color: #E50914 !important;
        box-shadow: 0 0 15px rgba(229, 9, 20, 0.3) !important;
    }

    /* Botão de Ação Massivo */
    div.stButton > button {
        background: #E50914 !important;
        border: none !important;
        padding: 15px 0 !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        width: 100% !important;
        height: 60px !important;
    }

    div.stButton > button:hover {
        background: #ff1e2d !important;
        transform: scale(1.02);
        box-shadow: 0 15px 30px rgba(229, 9, 20, 0.4) !important;
    }

    /* Rodapé discreto */
    .footer-note {
        text-align: center;
        color: #444;
        font-size: 0.75rem;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGICA E CONTEÚDO
if 'auth' not in st.session_state:
    st.session_state.auth = False

# Link da imagem que você forneceu
IMAGE_URL = "https://lh3.googleusercontent.com/d/1B8LjYZmHsjpyZPC96FaYAODskWrwOVJC"

if not st.session_state.auth:
    # --- HEADER ---
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">KERIGMA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">The Digital Media Experience</p>', unsafe_allow_html=True)

    # --- LAYOUT CENTRALIZADO ---
    col_left, col_center, col_right = st.columns([1, 1.8, 1])

    with col_center:
        # Imagem Proporcional
        st.image(IMAGE_URL, use_container_width=True)
        st.write("##")

        # Container de Login
        with st.container():
            st.markdown('<div class="login-card">', unsafe_allow_html=True)
            
            st.markdown("<h2 style='text-align:center; font-size:1.5rem; margin-bottom:30px;'>Acessar Conteúdo Privado</h2>", unsafe_allow_html=True)
            
            user = st.text_input("Identificação", placeholder="E-mail ou Usuário")
            password = st.text_input("Chave de Acesso", type="password", placeholder="Sua senha")
            
            st.write("##")
            if st.button("INICIAR EXPERIÊNCIA"):
                if user == "admin" and password == "1234":
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Acesso negado. Credenciais não reconhecidas.")
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('<p class="footer-note">© 2026 MÍDIA KERIGMA. TODOS OS DIREITOS RESERVADOS.</p>', unsafe_allow_html=True)

else:
    # --- INTERFACE PÓS-LOGIN (ESTILO STREAMING) ---
    st.markdown('<h2 style="color:#E50914; font-weight:900;">MÍDIA KERIGMA</h2>', unsafe_allow_html=True)
    
    # Barra de categorias
    st.write("---")
    st.markdown("### 🍿 Continue Assistindo")
    
    # Grid de Vídeos/Estudos
    cols = st.columns(4)
    titles = ["O Kerigma", "Maanaim: O Lugar", "A Palavra Viva", "Poder e Unção"]
    for i, col in enumerate(cols):
        with col:
            st.image(f"https://picsum.photos/400/225?random={i}", use_container_width=True)
            st.markdown(f"**{titles[i]}**")
            st.button(f"Assistir Agora", key=f"btn_{i}")

    if st.sidebar.button("Sair da Conta"):
        st.session_state.auth = False
        st.rerun()
