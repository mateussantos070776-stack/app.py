# 2. CSS PREMIUM (ATUALIZADO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap'); /* Fonte elegante */

    .stApp { background-color: #050505; color: white; }
    
    /* Estilo para o Título Elegante */
    .main-title { 
        font-family: 'Great Vibes', cursive; 
        font-weight: 400; 
        font-size: 5.5rem; 
        color: #E50914; 
        text-align: center; 
        margin-bottom: 0px;
    }

    /* Centralização e Estilo dos Botões */
    div.stButton > button {
        background-color: #E50914 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        font-weight: 700 !important;
        display: block;
        margin: 0 auto; /* Centraliza o botão */
    }

    /* Centralização dos Inputs */
    div[data-testid="stTextInput"] {
        width: 100%;
        max-width: 400px;
        margin: 0 auto;
    }
    
    /* Estilo dos Cards (Mantido da base) */
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
    </style>
    """, unsafe_allow_html=True)

# ... (restante do código mantido)

# 4. LÓGICA DE TELAS (AJUSTE NA HOME)
if st.session_state.tela == "home":
    st.markdown('<div style="margin-top: 15vh;">', unsafe_allow_html=True) # Espaçamento topo
    st.markdown('<h1 class="main-title">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing:10px; color:#666; margin-bottom: 30px;'>DIGITAL MEDIA HUB</p>", unsafe_allow_html=True)
    
    # Container centralizado para input e botão
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        chave = st.text_input("", placeholder="Insira sua Chave de Integrante", type="password")
        if st.button("ACESSAR EXCLUSIVO MÍDIA"):
            # Lógica de validação...
            st.session_state.tela = "membro"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
