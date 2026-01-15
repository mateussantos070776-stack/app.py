import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA (Define como a barra lateral se comporta)
st.set_page_config(
    page_title="Viva o Propósito", 
    page_icon="🙏", 
    layout="wide",
    initial_sidebar_state="expanded"  # Pode ser "collapsed" para começar fechada
)

# 2. LIMPEZA VISUAL (CSS)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {display:none !important;}
    </style>
    """, unsafe_allow_html=True)

# 3. COLUNA LATERAL REDUZÍVEL (Sidebar)
with st.sidebar:
    st.title("🛡️ Painel Admin")
    st.write("Clique na seta acima ( < ) para recolher esta barra.")
    
    # Sistema de Login dentro da barra
    with st.expander("🔑 Login Admin"):
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.button("Acessar"):
            if usuario == "seu_usuario" and senha == "sua_senha":
                st.session_state.logado = True
                st.success("Acesso liberado!")
            else:
                st.error("Incorreto")

    st.write("---")
    st.caption("Versão 2.0 - 2026")

# 4. CONTEÚDO PRINCIPAL (Fica centralizado quando a barra fecha)
st.title("📖 Portal Viva o Propósito")
st.info("No celular, a seta para abrir a barra lateral fica no canto superior esquerdo.")

# Simulando as pastas de pregação na área principal para melhor uso no telefone
aba1, aba2 = st.tabs(["Estudos", "Sobre"])
with aba1:
    st.subheader("Pasta: Jeremias 29")
    st.write("Conteúdo da pregação aqui...")
