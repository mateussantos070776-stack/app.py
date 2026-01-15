import streamlit as st

# 1. ESTILO VITRINE (PRIVALIA)
st.set_page_config(page_title="Viva o Propósito", layout="wide")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .nav-bar {background-color: white; padding: 15px; border-bottom: 2px solid #f4f4f4; text-align: center; margin-bottom: 30px;}
    .nav-item {display: inline-block; margin: 0 20px; font-weight: 700; color: #111; text-transform: uppercase; font-size: 13px; cursor: pointer;}
    .card {border: 1px solid #eee; padding: 10px; border-radius: 5px; text-align: center;}
    </style>
    <div class="nav-bar">
        <span class="nav-item">Lançamentos</span>
        <span class="nav-item">Mais Lidas</span>
        <span class="nav-item">Séries</span>
        <span class="nav-item">Sobre</span>
    </div>
    """, unsafe_allow_html=True)

# 2. INICIALIZAÇÃO DE DADOS (ORDEM E CONTEÚDO)
if 'ordem_pastas' not in st.session_state:
    st.session_state.pastas = {
        "Jeremias 29": {"texto": "Planos de paz e futuro.", "img": "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=400"},
        "Salmos 23": {"texto": "O Senhor é meu pastor.", "img": "https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=400"},
        "Atos 2": {"texto": "O mover do Espírito.", "img": "https://images.unsplash.com/photo-1490730141103-6ca3d7d6cf4b?w=400"}
    }
    st.session_state.ordem_pastas = list(st.session_state.pastas.keys())

# 3. PAINEL ADMIN (NA LATERAL)
with st.sidebar:
    st.title("🛡️ Gestão do Portal")
    with st.expander("LOGIN ADMIN"):
        user = st.text_input("Usuário")
        passw = st.text_input("Senha", type="password")
        if st.button("Acessar"):
            if user == "admin" and passw == "1234": # Lembre-se de trocar por sua senha forte!
                st.session_state.admin_logado = True
                st.rerun()

    if st.session_state.get('admin_logado'):
        st.subheader("🔄 Reordenar Pastas")
        nova_ordem = st.multiselect(
            "Arraste ou selecione na ordem desejada:",
            options=list(st.session_state.pastas.keys()),
            default=st.session_state.ordem_pastas
        )
        if st.button("Aplicar Nova Ordem"):
            st.session_state.ordem_pastas = nova_ordem
            st.success("Ordem atualizada!")
            st.rerun()
        
        if st.button("Sair do Admin"):
            st.session_state.admin_logado = False
            st.rerun()

# 4. EXIBIÇÃO DA VITRINE (PÚBLICO)
st.title("✨ Vitrine Viva o Propósito")
cols = st.columns(len(st.session_state.ordem_pastas))

for i, nome_pasta in enumerate(st.session_state.ordem_pastas):
    dados = st.session_state.pastas[nome_pasta]
    with cols[i]:
        st.image(dados['img'], use_container_width=True)
        st.subheader(nome_pasta)
        if st.button(f"Ver {nome_pasta}", key=f"btn_{i}"):
            st.write(dados['texto'])
