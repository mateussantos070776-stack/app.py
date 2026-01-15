import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Viva o Propósito", layout="wide", initial_sidebar_state="collapsed")

# 2. INICIALIZAÇÃO DE ESTADOS (O 'CÉREBRO' DO SITE)
if 'admin_ativo' not in st.session_state:
    st.session_state.admin_ativo = False
if 'view' not in st.session_state:
    st.session_state.view = "home"
if 'pastas' not in st.session_state:
    st.session_state.pastas = {
        "Jeremias 29": {"texto": "Planos de paz e futuro.", "img": "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=400"},
        "Salmos 23": {"texto": "O Senhor é meu pastor.", "img": "https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=400"}
    }
if 'ordem' not in st.session_state:
    st.session_state.ordem = list(st.session_state.pastas.keys())

# 3. ESTILO VISUAL E BARRA SUPERIOR (ESTILO PRIVALIA)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .top-bar {
        display: flex; align-items: center; justify-content: space-between;
        padding: 10px 40px; background: white; border-bottom: 1px solid #eee;
        position: fixed; top: 0; left: 0; right: 0; z-index: 999;
    }
    .main-content { margin-top: 100px; }
    </style>
    """, unsafe_allow_html=True)

# CRIANDO A BARRA SUPERIOR COM O BOTÃO DE CADEADO REAL
with st.container():
    col_cad, col_tit, col_vazio = st.columns([1, 4, 1])
    with col_cad:
        # Este botão agora substitui o ícone parado e abre o painel lateral
        if st.button("🔒 ACESSO"):
            st.toast("Abrindo Painel de Login...")
            # No Streamlit, botões podem disparar mudanças de estado
            st.session_state.view = "login"
    with col_tit:
        st.markdown("<h2 style='text-align: center;'>VIVA O PROPÓSITO</h2>", unsafe_allow_html=True)

st.markdown("<div class='main-content'></div>", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGAÇÃO (AS JANELAS)

# JANELA DE LOGIN (DISPARADA PELO CADEADO)
if st.session_state.view == "login":
    if st.button("⬅️ VOLTAR PARA O INÍCIO"):
        st.session_state.view = "home"
        st.rerun()
    
    st.subheader("🔐 Área Administrativa")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Confirmar Login"):
        if usuario == "admin" and senha == "suasenha": # Altere sua senha aqui
            st.session_state.admin_ativo = True
            st.success("Logado com sucesso!")
            st.session_state.view = "admin_panel"
            st.rerun()
        else:
            st.error("Dados inválidos.")

# JANELA DE ADMINISTRAÇÃO (ONDE VOCÊ TROCA TUDO DE LUGAR)
elif st.session_state.view == "admin_panel":
    if st.button("⬅️ VOLTAR PARA O INÍCIO"):
        st.session_state.view = "home"
        st.rerun()
    
    st.title("🔄 Gerenciar Vitrine")
    nova_ordem = st.multiselect("Defina a ordem das pregações:", 
                                options=list(st.session_state.pastas.keys()), 
                                default=st.session_state.ordem)
    if st.button("Salvar Nova Ordem"):
        st.session_state.ordem = nova_ordem
        st.success("Ordem atualizada!")
    
    if st.button("Sair (Logout)"):
        st.session_state.admin_ativo = False
        st.session_state.view = "home"
        st.rerun()

# JANELA DE LEITURA DE ESTUDO
elif st.session_state.view in st.session_state.pastas:
    if st.button("⬅️ VOLTAR PARA A VITRINE"):
        st.session_state.view = "home"
        st.rerun()
    
    nome_estudo = st.session_state.view
    st.header(nome_estudo)
    st.image(st.session_state.pastas[nome_estudo]["img"], width=400)
    st.write(st.session_state.pastas[nome_estudo]["texto"])

# VITRINE PRINCIPAL (HOME)
else:
    st.title("✨ Vitrine de Estudos")
    cols = st.columns(3)
    for i, nome in enumerate(st.session_state.ordem):
        dados = st.session_state.pastas[nome]
        with cols[i % 3]:
            st.image(dados['img'], use_container_width=True)
            st.subheader(nome)
            if st.button(f"Ler: {nome}", key=f"btn_{nome}"):
                st.session_state.view = nome
                st.rerun()
