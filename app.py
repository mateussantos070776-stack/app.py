import streamlit as st

# 1. CONFIGURAÇÃO E DESIGN
st.set_page_config(page_title="Viva o Propósito", layout="wide", initial_sidebar_state="collapsed")

# Inicialização de Estados
if 'view' not in st.session_state: st.session_state.view = "home"
if 'usuarios_cadastrados' not in st.session_state: st.session_state.usuarios_cadastrados = []
if 'pastas' not in st.session_state:
    st.session_state.pastas = {
        "Jeremias 29": {"texto": "Planos de paz.", "img": "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=400"},
        "Salmos 23": {"texto": "O Senhor é meu pastor.", "img": "https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=400"}
    }
if 'ordem' not in st.session_state: st.session_state.ordem = list(st.session_state.pastas.keys())

# CSS para Menu Superior
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .nav-bar { display: flex; justify-content: center; background: white; padding: 10px; border-bottom: 1px solid #eee; margin-bottom: 30px; }
    .nav-item { margin: 0 20px; font-weight: bold; cursor: pointer; text-transform: uppercase; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU SUPERIOR E BOTÃO CADEADO
col_cad, col_menu, col_vazio = st.columns([1, 4, 1])
with col_cad:
    if st.button("🔒 ACESSO"):
        st.session_state.view = "login_admin"
        st.rerun()

with col_menu:
    # Simulando abas clicáveis com botões lado a lado
    c1, c2, c3 = st.columns(3)
    if c1.button("🏠 INÍCIO"): st.session_state.view = "home"; st.rerun()
    if c2.button("📝 CADASTROS"): st.session_state.view = "tela_cadastro"; st.rerun()
    if c3.button("📖 ESTUDOS"): st.session_state.view = "home"; st.rerun()

st.write("---")

# 3. LÓGICA DE NAVEGAÇÃO

# TELA DE CADASTRO (PARA O PÚBLICO)
if st.session_state.view == "tela_cadastro":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.title("📝 Cadastro de Novos Membros")
    with st.form("novo_user"):
        nome_novo = st.text_input("Nome Completo")
        senha_nova = st.text_input("Crie uma Senha", type="password")
        if st.form_submit_button("Finalizar Cadastro"):
            st.session_state.usuarios_cadastrados.append({"nome": nome_novo, "senha": senha_nova})
            st.success(f"Bem-vindo, {nome_novo}! Cadastro realizado.")

# TELA LOGIN ADMIN
elif st.session_state.view == "login_admin":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.subheader("🔑 Login do Administrador")
    u = st.text_input("Usuário Admin")
    s = st.text_input("Senha Admin", type="password")
    if st.button("Entrar"):
        if u == "admin" and s == "1234":
            st.session_state.view = "admin_area"
            st.rerun()

# ÁREA ADMIN (ONDE APARECEM OS USUÁRIOS)
elif st.session_state.view == "admin_area":
    if st.button("⬅️ VOLTAR PARA O SITE"): st.session_state.view = "home"; st.rerun()
    st.title("🛡️ Painel de Controle")
    
    aba_reordenar, aba_usuarios = st.tabs(["🔄 Reordenar Pastas", "👥 Usuários Cadastrados"])
    
    with aba_reordenar:
        nova_ordem = st.multiselect("Ordem da Vitrine:", options=list(st.session_state.pastas.keys()), default=st.session_state.ordem)
        if st.button("Salvar Ordem"):
            st.session_state.ordem = nova_ordem
            st.success("Ordem salva!")
            
    with aba_usuarios:
        st.subheader("Lista de Pessoas Cadastradas")
        if st.session_state.usuarios_cadastrados:
            for user in st.session_state.usuarios_cadastrados:
                st.write(f"👤 **Nome:** {user['nome']}")
        else:
            st.info("Nenhum usuário cadastrado ainda.")

# HOME (VITRINE)
elif st.session_state.view == "home":
    st.title("✨ Vitrine de Propósito")
    cols = st.columns(len(st.session_state.ordem))
    for i, nome in enumerate(st.session_state.ordem):
        with cols[i]:
            st.image(st.session_state.pastas[nome]["img"])
            st.subheader(nome)
            if st.button(f"Ver {nome}", key=nome):
                st.info(st.session_state.pastas[nome]["texto"])
