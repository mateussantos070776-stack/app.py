import streamlit as st

# 1. CONFIGURAÇÃO E REMOÇÃO DE MARCA D'ÁGUA REFORÇADA
st.set_page_config(page_title="Portal Viva o Propósito", page_icon="🙏", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display:none;}
            #stDecoration {display:none;}
            [data-testid="stHeader"] {display:none;}
            [data-testid="stFooter"] {display:none;}
            /* Garante que o seletor de pastas fique bem visível no topo no mobile */
            .stSelectbox {margin-bottom: 20px;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 2. BANCO DE DADOS (MEMÓRIA)
if 'estudos' not in st.session_state:
    st.session_state.estudos = {
        "Jeremias 29": "Deus tem planos de paz e não de mal para dar o fim que desejais. Busque-o de todo o coração.",
        "O Propósito na Dor": "As lutas de Jó e Jesus mostram que a dor é um processo de moldagem para o destino profético.",
        "Direção no Exílio": "Edificai casas e plantai pomares. Prosperar onde você está é uma ordem divina."
    }

# 3. ÁREA DE LOGIN (ADMIN) - CONTINUA NA LATERAL
with st.sidebar:
    st.title("🔐 Administração")
    if 'admin_ativo' not in st.session_state:
        st.session_state.admin_ativo = False

    if not st.session_state.admin_ativo:
        with st.expander("LOGIN ADMIN"):
            user = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            if st.button("Acessar Editor"):
                if user == "admin" and password == "1234":
                    st.session_state.admin_ativo = True
                    st.rerun()
                else:
                    st.error("Erro!")
    else:
        if st.button("Sair do Sistema"):
            st.session_state.admin_ativo = False
            st.rerun()

# 4. ÁREA PRINCIPAL (PASTAS ACESSÍVEIS NO TELEFONE)
st.title("📂 MINHAS PREGAÇÕES")

# Colocamos o seletor de pastas no corpo principal para não sumir no celular
pasta = st.selectbox("Escolha uma pasta para abrir:", list(st.session_state.estudos.keys()))

st.write("---")

if st.session_state.admin_ativo:
    st.warning("MODO EDIÇÃO ATIVO")
    texto_editado = st.text_area("Editar conteúdo:", st.session_state.estudos[pasta], height=300)
    if st.button("💾 Salvar Alterações"):
        st.session_state.estudos[pasta] = texto_editado
        st.success("Salvo!")
else:
    st.header(f"📍 {pasta}")
    st.write(st.session_state.estudos[pasta])

st.write("---")
st.caption("Viva o Propósito - Acesso Público")
