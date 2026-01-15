import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA E REMOÇÃO TOTAL DE MARCAS (PC E CELULAR)
st.set_page_config(page_title="Portal Viva o Propósito", page_icon="🙏", layout="wide")

# CSS Reforçado para esconder marca d'água, rodapé, menu e botão de deploy
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployButton {display:none;}
            #stDecoration {display:none;}
            [data-testid="stHeader"] {display:none !important;}
            [data-testid="stFooter"] {display:none !important;}
            div[data-testid="stStatusWidget"] {display:none !important;}
            /* Remove o preenchimento excessivo no topo no celular */
            .block-container {padding-top: 1rem !important;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 2. BANCO DE DADOS (MEMÓRIA DA SESSÃO)
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

    if not st.session_state.admin_ativo:
        with st.expander("LOGIN ADMIN"):
            user = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            if st.button("Acessar Editor"):
                if user == "admin" and password == "1234":
                    st.session_state.admin_ativo = True
                    st.rerun()
                else:
                    st.error("Dados incorretos.")
    else:
        st.write("✅ Modo Admin Ativado")
        if st.button("Sair do Sistema"):
            st.session_state.admin_ativo = False
            st.rerun()

# 4. ÁREA PRINCIPAL (PASTAS ACESSÍVEIS NO TELEFONE)
st.title("📂 MINHAS PREGAÇÕES")
st.write("Selecione abaixo a pasta que deseja ler:")

# Seletor de pastas no corpo da página para funcionar bem no mobile
pasta = st.selectbox("", list(st.session_state.estudos.keys()))

st.write("---")

if st.session_state.admin_ativo:
    st.info("MODO EDIÇÃO: Altere o texto abaixo e clique em salvar.")
    # Campo de edição para o Admin
    texto_editado = st.text_area("Editar conteúdo:", st.session_state.estudos[pasta], height=400)
    if st.button("💾 Salvar Alterações"):
        st.session_state.estudos[pasta] = texto_editated
        st.success("Conteúdo atualizado com sucesso!")
else:
    # Exibição limpa para o público
    st.header(f"📍 {pasta}")
    st.markdown(st.session_state.estudos[pasta])

st.write("---")
st.caption("Site gerenciável - Viva o Propósito")
