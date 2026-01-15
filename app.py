import streamlit as st

# 1. CONFIGURAÇÃO E ESTILO (ESTILO PRIVALIA)
st.set_page_config(page_title="Viva o Propósito", layout="wide", initial_sidebar_state="collapsed")

# Inicialização de Estados para evitar erros de navegação
if 'view' not in st.session_state: st.session_state.view = "home"
if 'admin_logado' not in st.session_state: st.session_state.admin_logado = False
if 'usuarios' not in st.session_state: st.session_state.usuarios = []
if 'pastas' not in st.session_state:
    st.session_state.pastas = {
        "Jeremias 29": {"texto": "Planos de paz e futuro.", "img": "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=400"},
        "Salmos 23": {"texto": "O Senhor é meu pastor.", "img": "https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=400"}
    }
if 'ordem' not in st.session_state: st.session_state.ordem = list(st.session_state.pastas.keys())

# CSS para Menu Superior Limpo
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .nav-bar { display: flex; justify-content: center; background: white; padding: 15px; border-bottom: 2px solid #eee; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BARRA DE NAVEGAÇÃO SUPERIOR (ESTILO MARCAS)
col_cad, col_ini, col_reg, col_est = st.columns([1, 1, 1, 1])

# Botão de Acesso (Cadeado com Ação)
if col_cad.button("🔒 ACESSO"):
    st.session_state.view = "admin_area" if st.session_state.admin_logado else "login_admin"
    st.rerun()

if col_ini.button("🏠 INÍCIO"): st.session_state.view = "home"; st.rerun()
if col_reg.button("📝 CADASTROS"): st.session_state.view = "tela_cadastro"; st.rerun()
if col_est.button("📖 ESTUDOS"): st.session_state.view = "home"; st.rerun()

st.write("---")

# 3. LÓGICA DE TELAS E NAVEGAÇÃO

# TELA DE CADASTRO PÚBLICO
if st.session_state.view == "tela_cadastro":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.title("📝 Cadastro de Membros")
    with st.form("cad_user"):
        nome = st.text_input("Nome Completo")
        senha_u = st.text_input("Criar Senha", type="password")
        if st.form_submit_button("Cadastrar"):
            if nome and senha_u:
                st.session_state.usuarios.append({"nome": nome, "senha": senha_u})
                st.success(f"Bem-vindo(a), {nome}!")
            else: st.error("Preencha todos os campos.")

# TELA DE LOGIN ADMIN (LOGIN: admin / SENHA: 1234)
elif st.session_state.view == "login_admin":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.subheader("🔑 Login do Administrador")
    with st.form("login_form"):
        u = st.text_input("Usuário")
        s = st.text_input("Senha", type="password")
        if st.form_submit_button("Entrar"):
            # Credenciais Exatas: admin e 1234
            if u == "admin" and s == "1234":
                st.session_state.admin_logado = True
                st.session_state.view = "admin_area"
                st.rerun()
            else:
                st.error("Usuário ou Senha incorretos.")

# ÁREA ADMIN (ONDE FICA A PASTA USUÁRIOS)
elif st.session_state.view == "admin_area":
    if st.button("⬅️ SAIR DO ADMIN"): 
        st.session_state.admin_logado = False
        st.session_state.view = "home"; st.rerun()
    
    st.title("🛡️ Painel de Gestão")
    tab_ordem, tab_users = st.tabs(["🔄 Reordenar Vitrine", "👥 Pasta: Usuários"])
    
    with tab_ordem:
        ordem_nova = st.multiselect("Ordem de exibição:", options=list(st.session_state.pastas.keys()), default=st.session_state.ordem)
        if st.button("Salvar Ordem"):
            st.session_state.ordem = ordem_nova
            st.success("Vitrine atualizada!")

    with tab_users:
        st.subheader("Pessoas que se cadastraram")
        if st.session_state.usuarios:
            for user in st.session_state.usuarios:
                st.write(f"👤 **{user['nome']}**")
        else:
            st.info("Nenhum cadastro realizado ainda.")

# HOME (VITRINE)
else:
    st.title("✨ Nossas Coleções")
    cols = st.columns(len(st.session_state.ordem))
    for i, nome in enumerate(st.session_state.ordem):
        with cols[i]:
            st.image(st.session_state.pastas[nome]["img"])
            st.subheader(nome)
            if st.button(f"Abrir {nome}", key=nome):
                st.info(st.session_state.pastas[nome]["texto"])
