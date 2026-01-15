import streamlit as st

# 1. CONFIGURAÇÃO DE DESIGN (ESTILO VITRINE)
st.set_page_config(page_title="Viva o Propósito", layout="wide")

# CSS para criar o menu superior e o estilo de marcas
st.markdown("""
    <style>
    /* Remove elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Estilo do Menu Superior (Estilo Privalia) */
    .nav-bar {
        background-color: white;
        padding: 10px;
        border-bottom: 1px solid #eee;
        text-align: center;
        margin-bottom: 20px;
    }
    .nav-item {
        display: inline-block;
        margin: 0 15px;
        font-weight: bold;
        color: #000;
        text-decoration: none;
        text-transform: uppercase;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU SUPERIOR
st.markdown("""
    <div class="nav-bar">
        <span class="nav-item">Início</span>
        <span class="nav-item">Estudos Bíblicos</span>
        <span class="nav-item">Ministério</span>
        <span class="nav-item">Contato</span>
    </div>
    """, unsafe_allow_html=True)

# 3. CONTEÚDO PRINCIPAL (VITRINE)
st.title("✨ Coleções de Fé")
st.write("Explore as pastas e mergulhe na palavra.")

# Criando colunas como se fossem categorias de marcas
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=500", caption="PASTA: JEREMIAS 29")
    if st.button("Abrir Estudo", key="j29"):
        st.info("Plano de Deus: Paz e Futuro.")

with col2:
    st.image("https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=500", caption="PASTA: SALMOS")
    if st.button("Abrir Estudo", key="salmos"):
        st.info("O Senhor é meu Pastor.")

with col3:
    st.image("https://images.unsplash.com/photo-1490730141103-6ca3d7d6cf4b?w=500", caption="PASTA: ATOS")
    if st.button("Abrir Estudo", key="atos"):
        st.info("O Poder do Espírito Santo.")

# 4. LOGIN ADMIN DISCRETO (ESTILO 'ENTRAR' NO TOPO DIREITO)
with st.sidebar:
    st.title("🔒 Login Admin")
    user = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Acessar Painel"):
        st.success("Logado!")
