import streamlit as st

# 1. CONFIGURAÇÃO INICIAL
st.set_page_config(page_title="Viva o Propósito", layout="wide", initial_sidebar_state="collapsed")

# Inicialização de Estados com Trava de Segurança
if 'view' not in st.session_state: st.session_state.view = "home"
if 'admin_logado' not in st.session_state: st.session_state.admin_logado = False
if 'usuarios' not in st.session_state: st.session_state.usuarios = []
if 'pastas' not in st.session_state:
    st.session_state.pastas = {
        "Jeremias 29": {"texto": "Planos de paz e futuro.", "img": "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=400"},
        "Salmos 23": {"texto": "O Senhor é meu pastor.", "img": "https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=400"}
    }
if 'ordem' not in st.session_state: st.session_state.ordem = list(st.session_state.pastas.keys())

# 2. BARRA DE NAVEGAÇÃO SUPERIOR (ESTILO PRIVALIA)
cols_nav = st.columns([1, 1, 1, 1])
if cols_nav[0].button("🔒 ACESSO"):
    st.session_state.view = "admin_area" if st.session_state.admin_logado else "login_admin"
    st.rerun()
if cols_nav[1].button("🏠 INÍCIO"): st.session_state.view = "home"; st.rerun()
if cols_nav[2].button("📝 CADASTROS"): st.session_state.view = "tela_cadastro"; st.rerun()
if cols_nav[3].button("📖 ESTUDOS"): st.session_state.view = "home"; st.rerun()

st.write("---")

# 3. LÓGICA DE NAVEGAÇÃO

# TELA DE CADASTRO
if st.session_state.view == "tela_cadastro":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.title("📝 Cadastro de Membros")
    with st.form("form_cad"):
        n = st.text_input("Nome")
        s = st.text_input("Senha", type="password")
        if st.form_submit_button("Cadastrar"):
            st.session_state.usuarios.append({"nome": n, "senha": s})
            st.success("Cadastrado com sucesso!")

# TELA DE LOGIN ADMIN (admin / 1234)
elif st.session_state.view == "login_admin":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.subheader("🔑 Login Administrativo")
    with st.form("login_admin_form"):
        u = st.text_input("Usuário")
        p = st.text_input("Senha", type="password")
        if st.form_submit_button("Entrar"):
            if u == "admin" and p == "1234":
                st.session_state.admin_logado = True
                st.session_state.view = "admin_area"
                st.rerun()
            else: st.error("Incorreto.")

# ÁREA ADMIN
elif st.session_state.view == "admin_area":
    if st.button("⬅️ SAIR DO ADMIN"): 
        st.session_state.admin_logado = False
        st.session_state.view = "home"; st.rerun()
    st.title("🛡️ Painel de Gestão")
    t1, t2 = st.tabs(["🔄 Ordem", "👥 Usuários"])
    with t1:
        nova = st.multiselect("Ordem:", options=list(st.session_state.pastas.keys()), default=st.session_state.ordem)
        if st.button("Salvar"): st.session_state.ordem = nova; st.success("Ok!")
    with t2:
        for user in st.session_state.usuarios: st.write(f"👤 {user['nome']}")

# VITRINE HOME (COM CORREÇÃO DO ERRO)
else:
    st.title("✨ Vitrine de Estudos")
    qtd_pastas = len(st.session_state.ordem)
    
    if qtd_pastas > 0:
        cols = st.columns(qtd_pastas) # Aqui o erro foi corrigido
        for i, nome in enumerate(st.session_state.ordem):
            with cols[i]:
                st.image(st.session_state.pastas[nome]["img"])
                st.subheader(nome)
                if st.button(f"Abrir {nome}", key=nome):
                    st.info(st.session_state.pastas[nome]["texto"])
    else:
        st.warning("Nenhuma pregação disponível no momento.")
