import streamlit as st

# 1. CONFIGURAÇÃO E DESIGN (ESTILO VITRINE)
st.set_page_config(page_title="Viva o Propósito", layout="wide", initial_sidebar_state="collapsed")

# CSS para criar a barra superior e o botão de cadeado no canto esquerdo
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
    /* Barra Superior Estilo Privalia */
    .top-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 40px;
        background-color: white;
        border-bottom: 1px solid #eee;
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 999;
    }
    .nav-items { font-weight: bold; text-transform: uppercase; font-size: 13px; color: #000; }
    .nav-items span { margin: 0 15px; cursor: pointer; }
    
    /* Ajuste para o conteúdo não ficar embaixo da barra fixa */
    .main-content { margin-top: 80px; }
    </style>
    
    <div class="top-bar">
        <div style="font-size: 24px;">🔒</div> <div class="nav-items">
            <span>INÍCIO</span>
            <span>ESTUDOS</span>
            <span>MINISTÉRIO</span>
            <span>SOBRE</span>
        </div>
        <div style="width: 24px;"></div> </div>
    <div class="main-content"></div>
    """, unsafe_allow_html=True)

# 2. BANCO DE DADOS (MEMÓRIA)
if 'pastas' not in st.session_state:
    st.session_state.pastas = {
        "Jeremias 29": {"texto": "Planos de paz e futuro.", "img": "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=400"},
        "Salmos 23": {"texto": "O Senhor é meu pastor.", "img": "https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=400"},
        "Atos 2": {"texto": "O mover do Espírito.", "img": "https://images.unsplash.com/photo-1490730141103-6ca3d7d6cf4b?w=400"}
    }
    st.session_state.ordem = list(st.session_state.pastas.keys())

# 3. ABA ADMIN (LATERAL - ACESSADA PELO CADEADO)
with st.sidebar:
    st.title("🔐 Login Admin")
    with st.expander("Acessar Painel"):
        user = st.text_input("Usuário")
        passw = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if user == "admin" and passw == "suasenha": # Altere para sua senha segura
                st.session_state.admin = True
                st.success("Bem-vindo, Pastor!")
    
    if st.session_state.get('admin'):
        st.write("---")
        st.subheader("🔄 Trocar tudo de lugar")
        # Função para reordenar
        nova_ordem = st.multiselect(
            "Selecione as pastas na ordem desejada:",
            options=list(st.session_state.pastas.keys()),
            default=st.session_state.ordem
        )
        if st.button("Aplicar Nova Ordem"):
            st.session_state.ordem = nova_ordem
            st.rerun()
        
        if st.button("Sair"):
            st.session_state.admin = False
            st.rerun()

# 4. EXIBIÇÃO DA VITRINE
st.title("✨ Vitrine Viva o Propósito")
st.write("Explore nossas coleções de estudos bíblicos.")

cols = st.columns(3)
for i, nome in enumerate(st.session_state.ordem):
    dados = st.session_state.pastas[nome]
    with cols[i % 3]:
        st.image(dados['img'], use_container_width=True)
        st.subheader(nome)
        if st.button(f"Abrir {nome}", key=nome):
            st.write(dados['texto'])
