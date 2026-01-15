import streamlit as st

# 1. CONFIGURAÇÃO INICIAL
st.set_page_config(page_title="Viva o Propósito", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS PARA EFEITO DE ESMAECER (FADE-IN)
st.markdown("""
    <style>
    /* Remove menus padrão */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
    /* Animação de Esmaecer */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Aplica o esmaecer em todo o conteúdo principal */
    .stApp {
        animation: fadeIn 0.8s ease-in-out;
    }
    
    /* Estilo do Menu Superior */
    .nav-bar { display: flex; justify-content: center; background: white; padding: 10px; border-bottom: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

# 3. INICIALIZAÇÃO DE ESTADOS
if 'view' not in st.session_state: st.session_state.view = "home"
if 'admin_logado' not in st.session_state: st.session_state.admin_logado = False
if 'usuarios' not in st.session_state: st.session_state.usuarios = []
if 'pastas' not in st.session_state:
    st.session_state.pastas = {
        "Jeremias 29": {"texto": "Planos de paz e futuro.", "img": "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=400"},
        "Salmos 23": {"texto": "O Senhor é meu pastor.", "img": "https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=400"},
        "Atos 2": {"texto": "O mover do Espírito.", "img": "https://images.unsplash.com/photo-1490730141103-6ca3d7d6cf4b?w=400"}
    }
if 'ordem' not in st.session_state: st.session_state.ordem = list(st.session_state.pastas.keys())

# 4. NAVEGAÇÃO SUPERIOR
cols_nav = st.columns([1, 1, 1, 1])
if cols_nav[0].button("🔒 ACESSO"):
    st.session_state.view = "admin_area" if st.session_state.admin_logado else "login_admin"
    st.rerun()
if cols_nav[1].button("🏠 INÍCIO"): st.session_state.view = "home"; st.rerun()
if cols_nav[2].button("📝 CADASTROS"): st.session_state.view = "tela_cadastro"; st.rerun()
if cols_nav[3].button("📖 ESTUDOS"): st.session_state.view = "home"; st.rerun()

st.write("---")

# 5. LÓGICA DE TELAS (NAVEGAÇÃO)

# TELA DE CADASTRO
if st.session_state.view == "tela_cadastro":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.title("📝 Cadastro de Membros")
    with st.form("form_cad"):
        n = st.text_input("Nome")
        s = st.text_input("Senha", type="password")
        if st.form_submit_button("Finalizar Cadastro"):
            st.session_state.usuarios.append({"nome": n, "senha": s})
            st.success("Cadastro realizado com sucesso!")

# TELA DE LOGIN ADMIN (admin / 1234)
elif st.session_state.view == "login_admin":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.subheader("🔑 Login do Administrador")
    with st.form("login_admin_form"):
        u = st.text_input("Usuário")
        p = st.text_input("Senha", type="password")
        if st.form_submit_button("Entrar"):
            if u == "admin" and p == "1234":
                st.session_state.admin_logado = True
                st.session_state.view = "admin_area"
                st.rerun()
            else: st.error("Acesso negado.")

# ÁREA ADMIN (COM PASTA USUÁRIOS)
elif st.session_state.view == "admin_area":
    if st.button("⬅️ SAIR DO ADMIN"): 
        st.session_state.admin_logado = False
        st.session_state.view = "home"; st.rerun()
    st.title("🛡️ Painel de Gestão")
    t1, t2 = st.tabs(["🔄 Reordenar", "👥 Pasta: Usuários"])
    with t1:
        nova = st.multiselect("Ordem da Vitrine:", options=list(st.session_state.pastas.keys()), default=st.session_state.ordem)
        if st.button("Salvar Ordem"):
            st.session_state.ordem = nova
            st.success("Ordem atualizada!")
    with t2:
        st.subheader("Usuários Registrados")
        for user in st.session_state.usuarios:
            st.write(f"👤 {user['nome']}")

# VITRINE HOME (COM EFEITO DE ESMAECER)
else:
    st.title("✨ Vitrine Viva o Propósito")
    if len(st.session_state.ordem) > 0:
        cols = st.columns(len(st.session_state.ordem))
        for i, nome in enumerate(st.session_state.ordem):
            with cols[i]:
                st.image(st.session_state.pastas[nome]["img"])
                st.subheader(nome)
                if st.button(f"Abrir {nome}", key=nome):
                    st.info(st.session_state.pastas[nome]["texto"])
    else:
        st.info("Nenhum conteúdo disponível.")
