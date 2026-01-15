import streamlit as st

# 1. ESTÉTICA E LIMPEZA (SEM MARCA D'ÁGUA)
st.set_page_config(page_title="Viva o Propósito", page_icon="🙏", layout="centered")

# CSS para esconder tudo o que é desnecessário e focar na Palavra
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none;}
    [data-testid="stHeader"] {display:none !important;}
    [data-testid="stFooter"] {display:none !important;}
    /* Melhora a fonte e o espaçamento */
    .main .block-container {padding-top: 2rem;}
    h1 {color: #1E3A8A; font-family: 'Georgia', serif;}
    </style>
    """, unsafe_allow_html=True)

# 2. CONTEÚDO (PASTAS)
if 'estudos' not in st.session_state:
    st.session_state.estudos = {
        "📖 Jeremias 29:11": "Porque eu bem sei os pensamentos que tenho a vosso respeito, diz o Senhor; pensamentos de paz, e não de mal, para vos dar o fim que esperais.",
        "🔥 O Propósito na Dor": "A dor não é o fim, é o processo. Jó perdeu tudo para conhecer a Deus face a face.",
        "🏘️ Edificando no Exílio": "Não espere a tempestade passar para ser feliz. Edifique sua casa hoje, onde você está.",
        "🙏 Oração de Todo Coração": "Buscar-me-eis e me achareis, quando me buscardes de todo o vosso coração."
    }

# 3. INTERFACE PRINCIPAL
st.title("PROJETO: VIVA O PROPÓSITO")
st.write("---")

# Seletor de Pastas Centralizado
escolha = st.selectbox("📂 Escolha uma pregação para ler:", list(st.session_state.estudos.keys()))

st.write("---")

# Exibição do Texto
st.markdown(f"### {escolha}")
st.write(st.session_state.estudos[escolha])

# 4. BOTÃO DE COMPARTILHAR (MELHORIA)
texto_compartilhar = f"Olha esse estudo bíblico: {escolha}. Leia aqui: {st.query_params.get('url', 'SeuSite')}"
st.link_button("📢 Compartilhar no WhatsApp", f"https://wa.me/?text={texto_compartilhar}")

# 5. LOGIN ADMIN DISCRETO NO RODAPÉ
st.write("---")
with st.expander("🔐 Acesso Restrito"):
    user = st.text_input("Usuário")
    passw = st.text_input("Senha", type="password")
    if st.button("Entrar no Modo Editor"):
        if user == "admin" and passw == "1234":
            st.session_state.admin = True
            st.success("Modo Edição Ativo!")
        else:
            st.error("Acesso negado.")

if st.session_state.get('admin'):
    novo_texto = st.text_area("Editar conteúdo desta pasta:", st.session_state.estudos[escolha], height=200)
    if st.button("💾 Salvar Alterações"):
        st.session_state.estudos[escolha] = novo_texto
        st.success("Alterado com sucesso!")
