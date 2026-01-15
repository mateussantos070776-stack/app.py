import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA E REMOÇÃO DE MARCA D'ÁGUA
st.set_page_config(page_title="Portal Viva o Propósito", page_icon="🙏", layout="wide")

# CSS para esconder o menu, o rodapé e a marca d'água do Streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 2. INICIALIZAÇÃO DO BANCO DE DADOS (MEMÓRIA DA SESSÃO)
if 'estudos' not in st.session_state:
    st.session_state.estudos = {
        "Jeremias 29": "Deus tem planos de paz e não de mal para dar o fim que desejais. Busque-o de todo o coração.",
        "O Propósito na Dor": "As lutas de Jó e Jesus mostram que a dor é um processo de moldagem para o destino profético.",
        "Direção no Exílio": "Edificai casas e plantai pomares. Prosperar onde você está é uma ordem divina."
    }

# 3. BARRA LATERAL (LOGIN ADMIN NO CANTO SUPERIOR ESQUERDO)
with st.sidebar:
    st.title("🔐 Administração")
    
    if 'admin_ativo' not in st.session_state:
        st.session_state.admin_ativo = False

    # Área de Login
    if not st.session_state.admin_ativo:
        with st.expander("LOGIN ADMIN"):
            user = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            if st.button("Acessar Editor"):
                if user == "admin" and password == "1234":
                    st.session_state.admin_ativo = True
                    st.success("Modo Editor Ativo!")
                    st.rerun()
                else:
                    st.error("Credenciais inválidas.")
    else:
        st.write("✅ Você está logado como Admin")
        if st.button("Sair do Sistema"):
            st.session_state.admin_ativo = False
            st.rerun()

    st.write("---")
    st.title("📂 PASTAS PÚBLICAS")
    pasta = st.selectbox("Selecione uma Pregação:", list(st.session_state.estudos.keys()))

# 4. ÁREA DE EXIBIÇÃO E EDIÇÃO
st.title(f"📖 Pregação: {pasta}")
st.write("---")

if st.session_state.admin_ativo:
    st.warning("MODO DE EDIÇÃO: Altere o texto abaixo e clique em salvar.")
    # Campo de edição para o Admin
    texto_editado = st.text_area("Conteúdo da Pregação:", st.session_state.estudos[pasta], height=400)
    if st.button("💾 Salvar Alterações"):
        st.session_state.estudos[pasta] = texto_editado
        st.success("Conteúdo atualizado com sucesso!")
else:
    # Exibição limpa para o público
    st.markdown(f"### {pasta}")
    st.write(st.session_state.estudos[pasta])

st.write("---")
st.caption("Plataforma de Pregações - Viva o Propósito")
