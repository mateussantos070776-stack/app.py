import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Gestão de Pregações", page_icon="📝", layout="wide")

# --- INICIALIZAÇÃO DA MEMÓRIA (BANCO DE DADOS TEMPORÁRIO) ---
if 'pregacoes' not in st.session_state:
    st.session_state.pregacoes = {
        "Jeremias 29": "Conteúdo sobre viver o propósito no exílio...",
        "Fé e Coragem": "Estudo sobre Davi e Golias...",
        "Oração": "A importância de buscar de todo o coração."
    }

# --- BARRA LATERAL (LOGIN ADMIN NO CANTO SUPERIOR ESQUERDO) ---
with st.sidebar:
    st.title("🛡️ Área Restrita")
    if 'admin_logado' not in st.session_state:
        st.session_state.admin_logado = False

    if not st.session_state.admin_logado:
        with st.expander("LOGIN ADMIN"):
            usuario = st.text_input("Usuário")
            senha = st.text_input("Senha", type="password")
            if st.button("Acessar Painel"):
                if usuario == "admin" and senha == "1234":
                    st.session_state.admin_logado = True
                    st.success("Acesso liberado!")
                    st.rerun()
                else:
                    st.error("Dados incorretos.")
    else:
        st.write("✅ Você está no modo Editor")
        if st.button("Sair do Painel"):
            st.session_state.admin_logado = False
            st.rerun()

    st.write("---")
    st.title("📂 PASTAS PÚBLICAS")
    pasta_selecionada = st.selectbox("Escolha uma pregação para ler:", list(st.session_state.pregacoes.keys()))

# --- CONTEÚDO PRINCIPAL ---
st.title(f"📖 Pregação: {pasta_selecionada}")

if st.session_state.admin_logado:
    st.info("MODO EDIÇÃO ATIVADO: Você pode alterar o texto abaixo e clicar em 'Salvar Alterações'.")
    # Editor de Texto para o Admin
    novo_texto = st.text_area("Editar conteúdo:", st.session_state.pregacoes[pasta_selecionada], height=300)
    if st.button("💾 Salvar Alterações"):
        st.session_state.pregacoes[pasta_selecionada] = novo_texto
        st.success("Alteração salva com sucesso para esta sessão!")
else:
    # Visualização para o Público
    st.write(st.session_state.pregacoes[pasta_selecionada])

st.write("---")
st.caption("Site gerenciável via Streamlit Cloud e GitHub.")
