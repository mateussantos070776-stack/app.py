import streamlit as st

# 1. CONFIGURAÇÃO DE ALTO NÍVEL
st.set_page_config(
    page_title="Mídia Kerigma Maanaim | Oficial",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ESTILIZAÇÃO PROFISSIONAL (CSS AVANÇADO)
st.markdown("""
    <style>
    /* Importação de Fontes Premium */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=Oswald:wght@700&display=swap');

    /* Reset e Background Gradiente */
    .stApp {
        background: radial-gradient(circle at top, #1a1a1a 0%, #000000 100%);
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
    }

    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}

    /* Título Impactante Estilo Cinema */
    .hero-title {
        color: #E50914;
        font-family: 'Oswald', sans-serif;
        font-size: clamp(40px, 8vw, 80px);
        font-weight: 700;
        text-align: center;
        margin-top: 50px;
        margin-bottom: 0px;
        letter-spacing: -2px;
        text-transform: uppercase;
        filter: drop-shadow(0 0 15px rgba(229, 9, 20, 0.4));
    }

    /* Subtítulo Elegante */
    .hero-subtitle {
        color: #8c8c8c;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 40px;
        font-weight: 300;
        letter-spacing: 2px;
    }

    /* Card de Login Glassmorphism */
    .login-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        padding: 50px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        max-width: 480px;
        margin: auto;
        box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    }

    /* Inputs Modernos */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.07) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 8px !important;
        height: 55px !important;
        transition: all 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #E50914 !important;
        background-color: rgba(255, 255, 255, 0.12) !important;
        box-shadow: 0 0 10px rgba(229, 9, 20, 0.2) !important;
    }

    /* Botão Call-to-Action */
    div.stButton > button {
        background: linear-gradient(90deg, #E50914 0%, #B20710 100%) !important;
        color: white !important;
        width: 100%;
        border-radius: 8px !important;
        border: none !important;
        height: 55px !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: transform 0.2s, box-shadow 0.2s !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(229, 9, 20, 0.4) !important;
    }

    /* Ajuste de Imagem */
    .logo-img {
        display: block;
        margin: 0 auto;
        filter: brightness(1.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE NAVEGAÇÃO
if 'logado' not in st.session_state:
    st.session_state.logado = False

# URL DA SUA IMAGEM (Ajustada para o link direto)
IMAGE_URL = "https://lh3.googleusercontent.com/d/1B8LjYZmHsjpyZPC96FaYAODskWrwOVJC"

if not st.session_state.logado:
    # --- HERO SECTION ---
    st.markdown('<h1 class="hero-title">MIDIA KERIGMA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">PROCLAMANDO A PALAVRA E O PODER DE DEUS</p>', unsafe_allow_html=True)
    
    # Centralização da Imagem
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.image(IMAGE_URL, use_container_width=True)
    
    st.write("##") # Espaçador

    # --- LOGIN SECTION ---
    l1, l2, l3 = st.columns([1.2, 2, 1.2])
    with l2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; margin-bottom:30px; font-weight:700;'>Acessar Plataforma</h2>", unsafe_allow_html=True)
        
        email = st.text_input("E-mail corporativo ou CPF", placeholder="exemplo@kerigma.com")
        senha = st.text_input("Senha de acesso", type="password", placeholder="••••••••")
        
        st.write("##")
        if st.button("ENTRAR NA PLATAFORMA"):
            if email == "admin" and senha == "1234":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais inválidas. Verifique os dados e tente novamente.")
        
        st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #666; margin-top: 20px;'>Sistema Restrito para Membros e Colaboradores Autorizados.</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # TELA PÓS-LOGIN (DASHBOARD PROFISSIONAL)
    st.markdown(f'<h2 class="hero-title" style="font-size: 30px; text-align: left;">Mídia Kerigma</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📺 Conteúdo", "📊 Gestão", "⚙️ Configurações"])
    
    with tab1:
        st.subheader("Novos Lançamentos")
        # Aqui você pode criar um grid de vídeos ou estudos
        cols = st.columns(4)
        for i in range(4):
            with cols[i]:
                st.image("https://images.unsplash.com/photo-1585951237318-9ea5e175b891?w=400", use_container_width=True)
                st.write(f"Série Bíblica - Episódio {i+1}")
    
    if st.sidebar.button("Encerrar Sessão"):
        st.session_state.logado = False
        st.rerun()
