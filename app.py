import streamlit as st

# 1. CONFIGURAÇÃO E DESIGN (ESTILO PRIVALIA)
st.set_page_config(page_title="Viva o Propósito", layout="wide", initial_sidebar_state="collapsed")

# Inicialização de Estados (O "Cérebro" do Site)
if 'view' not in st.session_state: st.session_state.view = "home"
if 'admin_logado' not in st.session_state: st.session_state.admin_logado = False
if 'usuarios' not in st.session_state: st.session_state.usuarios = []
if 'pastas' not in st.session_state:
    st.session_state.pastas = {
        "Jeremias 29": {"texto": "Planos de paz e futuro.", "img": "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=400"},
        "Salmos 23": {"texto": "O Senhor é meu pastor.", "img": "https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=400"}
    }
if 'ordem' not in st.session_state: st.session_state.ordem = list(st.session_state.pastas.keys())

# CSS para Menu Superior e Estilo
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .nav-bar { display: flex; justify-content: center; background: white; padding: 15px; border-bottom: 2px solid #eee; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BARRA DE NAVEGAÇÃO SUPERIOR
col_cad, col_menu, col_vazio = st.columns([1, 4, 1])
with col_cad:
    # O CADEADO AGORA LEVA DIRETO PARA O LOGIN OU PARA A AREA ADMIN SE JÁ LOGADO
    if st.button("🔒 ACESSO"):
        st.session_state.view = "admin_area" if st.session_state.admin_logado else "login_admin"
        st.rerun()

with col_menu:
    c1, c2, c3 = st.columns(3)
    if c1.button("🏠 INÍCIO"): st.session_state.view = "home"; st.rerun()
    if c2.button("📝 CADASTROS"): st.session_state.view = "tela_cadastro"; st.rerun()
    if c3.button("📖 ESTUDOS"): st.session_state.view = "home"; st.rerun()

st.write("---")

# 3. LÓGICA DE TELAS (NAVEGAÇÃO COM SETA VOLTAR)

# TELA DE CADASTRO PÚBLICO
if st.session_state.view == "tela_cadastro":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.title("📝 Cadastro de Novos Membros")
    with st.container(border=True):
        nome = st.text_input("Nome Completo")
        senha_c = st.text_input("Crie uma Senha", type="password")
        if st.button("Finalizar Cadastro"):
            if nome and senha_c:
                st.session_state.usuarios.append({"nome": nome, "senha": senha_c})
                st.success(f"Glória a Deus! {nome} cadastrado.")
            else: st.error("Preencha tudo!")

# TELA DE LOGIN ADMIN (RESOLUÇÃO DO ERRO DO BOTÃO)
elif st.session_state.view == "login_admin":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.subheader("🔑 Autenticação do Administrador")
    
    # Usamos um formulário para garantir que o botão 'Entrar' funcione no primeiro clique
    with st.form("form_login"):
        u_admin = st.text_input("Usuário")
        s_admin = st.text_input("Senha", type="password")
        botao_entrar = st.form_submit_button("Entrar na Área Admin")
        
        if botao_entrar:
            if u_admin == "admin" and s_admin == "1234":
                st.session_state.admin_logado = True
                st.session_state.view = "admin_area"
                st.rerun()
            else:
                st.error("Usuário ou Senha incorretos.")

# ÁREA ADMIN (ONDE ESTÁ A PASTA USUÁRIOS)
elif st.session_state.view == "admin_area":
    if not st.session_state.admin_logado: 
        st.session_state.view = "login_admin"; st.rerun()
        
    if st.button("⬅️ SAIR DO PAINEL"): 
        st.session_state.admin_logado = False
        st.session_state.view = "home"; st.rerun()
        
    st.title("🛡️ Painel Administrativo")
    aba_ordem, aba_users = st.tabs(["🔄 Reordenar Vitrine", "👥 Pasta: Usuários"])
    
    with aba_ordem:
        nova_ordem = st.multiselect("Arraste para mudar a ordem:", options=list(st.session_state.pastas.keys()), default=st.session_state.ordem)
        if st.button("Salvar Nova Ordem"):
            st.session_state.ordem = nova_ordem
            st.success("Ordem atualizada na vitrine!")

    with aba_users:
        st.subheader("Membros Cadastrados")
        if st.session_state.usuarios:
            for i, u in enumerate(st.session_state.usuarios):
                st.write(f"{i+1}. 👤 **{u['nome']}**")
        else:
            st.info("Nenhum usuário cadastrado ainda.")

# HOME / VITRINE
else:
    st.title("✨ Vitrine Viva o Propósito")
    cols = st.columns(len(st.session_state.ordem))
    for i, nome in enumerate(st.session_state.ordem):
        with cols[i]:
            st.image(st.session_state.pastas[nome]["img"])
            st.subheader(nome)
            if st.button(f"Abrir {nome}", key=nome):
                st.info(st.session_state.pastas[nome]["texto"])
