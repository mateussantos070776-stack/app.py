import streamlit as st

# 1. CONFIGURAÇÃO INICIAL
st.set_page_config(page_title="Viva o Propósito", layout="wide", initial_sidebar_state="collapsed")

# 2. INICIALIZAÇÃO SEGURA (Evita o AttributeError)
if 'pastas' not in st.session_state:
    st.session_state.pastas = {
        "Jeremias 29": {"texto": "Planos de paz e futuro.", "img": "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=400"},
        "Salmos 23": {"texto": "O Senhor é meu pastor.", "img": "https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=400"},
        "Atos 2": {"texto": "O mover do Espírito.", "img": "https://images.unsplash.com/photo-1490730141103-6ca3d7d6cf4b?w=400"}
    }
if 'ordem' not in st.session_state:
    st.session_state.ordem = list(st.session_state.pastas.keys())
if 'admin_ativo' not in st.session_state:
    st.session_state.admin_ativo = False

# 3. ESTILO VISUAL (BARRA SUPERIOR COM CADEADO 2x2)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .top-bar {
        display: flex; align-items: center; justify-content: space-between;
        padding: 15px 40px; background: white; border-bottom: 1px solid #eee;
        position: fixed; top: 0; left: 0; right: 0; z-index: 999;
    }
    .admin-icon {
        width: 35px; height: 35px; background: #f4f4f4;
        display: flex; align-items: center; justify-content: center;
        border-radius: 4px; border: 1px solid #ddd; cursor: pointer;
    }
    .main-content { margin-top: 100px; }
    </style>
    <div class="top-bar">
        <div class="admin-icon">🔒</div>
        <div style="font-weight: bold; letter-spacing: 2px;">VIVA O PROPÓSITO</div>
        <div style="width: 35px;"></div>
    </div>
    <div class="main-content"></div>
    """, unsafe_allow_html=True)

# 4. PAINEL ADMIN (SIDEBAR REVELADA PELO CADEADO)
with st.sidebar:
    st.title("🔐 Área do Pastor")
    if not st.session_state.admin_ativo:
        user = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if user == "admin" and senha == "suasenha": # ALTERE SUA SENHA AQUI
                st.session_state.admin_ativo = True
                st.rerun()
    else:
        st.success("Modo Edição Ativo")
        st.subheader("🔄 Reordenar Pastas")
        nova_ordem = st.multiselect("Defina a nova ordem:", 
                                    options=list(st.session_state.pastas.keys()), 
                                    default=st.session_state.ordem)
        if st.button("Salvar Nova Ordem"):
            st.session_state.ordem = nova_ordem
            st.rerun()
        if st.button("Sair"):
            st.session_state.admin_ativo = False
            st.rerun()

# 5. VITRINE DE ESTUDOS
st.title("✨ Nossas Pregações")
cols = st.columns(3)
for i, nome in enumerate(st.session_state.ordem):
    dados = st.session_state.pastas[nome]
    with cols[i % 3]:
        st.image(dados['img'], use_container_width=True)
        st.subheader(nome)
        with st.expander("Ler Estudo"):
            st.write(dados['texto'])
