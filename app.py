import streamlit as st

# 1. CONFIGURAÇÃO E DESIGN (ESTILO NETFLIX)
st.set_page_config(page_title="Midia Kerigma Maanaim", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS CUSTOMIZADO PARA ESTILO NETFLIX
st.markdown("""
    <style>
    /* Fundo preto e esconder elementos padrão */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}

    /* Título Estilo Netflix */
    .netflix-logo {
        color: #E50914;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        letter-spacing: -2px;
        text-transform: uppercase;
    }

    /* Card de Login */
    .login-box {
        background-color: rgba(0, 0, 0, 0.75);
        padding: 60px;
        border-radius: 10px;
        border: 1px solid #333;
        max-width: 450px;
        margin: auto;
    }

    /* Botão Vermelho Netflix */
    div.stButton > button {
        background-color: #E50914 !important;
        color: white !important;
        width: 100%;
        border-radius: 4px;
        border: none;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #B20710 !important;
    }

    /* Inputs estilizados */
    .stTextInput input {
        background-color: #333 !important;
        color: white !important;
        border-radius: 4px !important;
        border: none !important;
        height: 50px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INICIALIZAÇÃO DE ESTADOS
if 'logado' not in st.session_state: st.session_state.logado = False
if 'view' not in st.session_state: st.session_state.view = "login"

# 4. LÓGICA DE TELAS

# TELA DE LOGIN ESTILO NETFLIX
if not st.session_state.logado:
    st.markdown('<div class="netflix-logo">MIDIA KERIGMA MAANAIM</div>', unsafe_allow_html=True)
    
    # Criando colunas para centralizar o formulário
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.subheader("Entrar")
        
        email = st.text_input("Email ou número de telefone")
        senha = st.text_input("Senha", type="password")
        
        if st.button("Entrar"):
            # Lógica simples de acesso para teste
            if email == "admin" and senha == "1234":
                st.session_state.logado = True
                st.session_state.view = "home"
                st.rerun()
            else:
                st.error("Senha incorreta ou usuário não encontrado.")
        
        st.markdown("""
            <p style='color: #737373; font-size: 14px; margin-top: 20px;'>
            Novo por aqui? <b>Assine agora.</b><br>
            Esta página é protegida pelo Google reCAPTCHA para garantir que você não é um robô.
            </p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# TELA DE CONTEÚDO (APÓS LOGIN)
else:
    st.markdown('<div style="color: #E50914; font-size: 30px; font-weight: bold;">MIDIA KERIGMA MAANAIM</div>', unsafe_allow_html=True)
    
    # Menu de navegação simples
    menu = st.tabs(["Início", "Séries Bíblicas", "Estudos", "Minha Lista"])
    
    with menu[0]:
        st.write("---")
        st.subheader("Populares na Midia Kerigma")
        
        # Exemplo de vitrine estilo Netflix
        col_img1, col_img2, col_img3 = st.columns(3)
        with col_img1:
            st.image("https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=400", caption="Jeremias 29: Planos de Paz")
        with col_img2:
            st.image("https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=400", caption="Salmos 23: O Pastor")
        with col_img3:
            st.image("https://images.unsplash.com/photo-1438263301115-f01b87352e43?w=400", caption="O Kerigma: O Anúncio")

    if st.sidebar.button("Sair"):
        st.session_state.logado = False
        st.rerun()
