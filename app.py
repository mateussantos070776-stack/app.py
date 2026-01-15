import streamlit as st

# 1. CONFIGURAÇÃO INICIAL
st.set_page_config(page_title="Viva o Propósito", layout="wide", initial_sidebar_state="collapsed")

# 2. INICIALIZAÇÃO DE ESTADOS (SEGURANÇA)
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

# 3. ESTILO VISUAL (BARRA SUPERIOR)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .top-bar {
        display: flex; align-items: center; justify-content: space-between;
        padding: 10px 40px; background: white; border-bottom: 1px solid #eee;
        position: fixed; top: 0; left: 0; right: 0; z-index: 999;
    }
    .main-content { margin-top: 80px; }
    </style>
    <div class="top-bar">
        <div style="font-size: 20px;">🔒 Portal Admin</div>
        <div style="font-weight: bold; letter-spacing: 2px;">VIVA O PROPÓSITO</div>
        <div></div>
    </div>
    <div class="main-content"></div>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL (ONDE O CADEADO "ABRE" O LOGIN)
# Para o cadeado ter ação, o Streamlit usa a barra lateral (sidebar) como o painel que desliza.
with st.sidebar:
    # BOTÃO VOLTAR (Sempre no topo da barra)
    if st.button("⬅️ Voltar"):
        st.session_state.view = "home"
        st.rerun()
        
    st.title("🔐 Acesso Restrito")
    if not st.session_state.admin_ativo:
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if usuario == "admin" and senha == "suasenha": # Altere aqui
                st.session_state.admin_ativo = True
                st.success("Logado!")
                st.rerun()
    else:
        st.write("✅ Você está no modo Editor")
        st.subheader("Configurações")
        nova_ordem = st.multiselect("Reordenar Vitrine:", options=list(st.session_state.pastas.keys()), default=st.session_state.ordem)
        if st.button("Salvar Ordem"):
            st.session_state.ordem = nova_ordem
            st.rerun()
        if st.button("Logoff"):
            st.session_state.admin_ativo = False
            st.rerun()

# 5. CONTEÚDO PRINCIPAL
if st.session_state.view == "home":
    st.title("✨ Vitrine de Estudos")
    cols = st.columns(len(st.session_state.ordem))
    for i, nome in enumerate(st.session_state.ordem):
        dados = st.session_state.pastas[nome]
        with cols[i]:
            st.image(dados['img'])
            if st.button(f"Abrir {nome}", key=nome):
                st.session_state.view = nome
                st.rerun()

else:
    # TELA DE LEITURA (COM SETA VOLTAR)
    if st.button("⬅️ Voltar para a Vitrine"):
        st.session_state.view = "home"
        st.rerun()
    
    nome_estudo = st.session_state.view
    st.header(nome_estudo)
    st.write(st.session_state.pastas[nome_estudo]["texto"])
