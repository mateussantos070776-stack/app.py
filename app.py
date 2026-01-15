import streamlit as st

# 1. CONFIGURAÇÃO E DESIGN (ESTILO PRIVALIA)
st.set_page_config(page_title="Viva o Propósito", layout="wide", initial_sidebar_state="collapsed")

# 2. INICIALIZAÇÃO DE ESTADOS
if 'view' not in st.session_state: st.session_state.view = "home"
if 'admin_logado' not in st.session_state: st.session_state.admin_logado = False
if 'usuarios' not in st.session_state: st.session_state.usuarios = []
if 'manutencao' not in st.session_state: st.session_state.manutencao = False # Estado do aviso
if 'pastas' not in st.session_state:
    st.session_state.pastas = {
        "Jeremias 29": {"texto": "Planos de paz e futuro.", "img": "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?w=400"},
        "Salmos 23": {"texto": "O Senhor é meu pastor.", "img": "https://images.unsplash.com/photo-1507434965515-61970f2bd7c6?w=400"}
    }
if 'ordem' not in st.session_state: st.session_state.ordem = list(st.session_state.pastas.keys())

# 3. CSS PARA ESMAECER E AVISO "ESTAMOS TRABALHANDO"
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .stApp { animation: fadeIn 0.8s ease-in-out; }

    /* Estilo da mensagem grande de manutenção */
    .banner-trabalho {
        background-color: #FF4B4B;
        color: white;
        text-align: center;
        padding: 20px;
        font-size: 30px;
        font-weight: bold;
        border-radius: 10px;
        margin-bottom: 20px;
        border: 2px solid white;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. EXIBIÇÃO DO AVISO GLOBAL (Se ativado no Admin)
if st.session_state.manutencao:
    st.markdown('<div class="banner-trabalho">⚠️ ESTAMOS TRABALHANDO</div>', unsafe_allow_html=True)

# 5. NAVEGAÇÃO SUPERIOR
col_cad, col_ini, col_reg, col_est = st.columns([1, 1, 1, 1])
if col_cad.button("🔒 ACESSO"):
    st.session_state.view = "admin_area" if st.session_state.admin_logado else "login_admin"
    st.rerun()
if col_ini.button("🏠 INÍCIO"): st.session_state.view = "home"; st.rerun()
if col_reg.button("📝 CADASTROS"): st.session_state.view = "tela_cadastro"; st.rerun()
if col_est.button("📖 ESTUDOS"): st.session_state.view = "home"; st.rerun()

st.write("---")

# 6. LÓGICA DE TELAS

# TELA DE CADASTRO
if st.session_state.view == "tela_cadastro":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.title("📝 Cadastro de Membros")
    with st.form("cad"):
        n = st.text_input("Nome")
        if st.form_submit_button("Cadastrar"):
            st.session_state.usuarios.append({"nome": n})
            st.success("Cadastrado!")

# TELA DE LOGIN ADMIN (admin / 1234)
elif st.session_state.view == "login_admin":
    if st.button("⬅️ VOLTAR"): st.session_state.view = "home"; st.rerun()
    st.subheader("🔑 Login do Administrador")
    with st.form("login"):
        u = st.text_input("Usuário")
        s = st.text_input("Senha", type="password")
        if st.form_submit_button("Entrar"):
            if u == "admin" and s == "1234":
                st.session_state.admin_logado = True
                st.session_state.view = "admin_area"
                st.rerun()
            else: st.error("Incorreto.")

# ÁREA ADMIN (NOVA OPÇÃO DE MANUTENÇÃO AQUI)
elif st.session_state.view == "admin_area":
    if st.button("⬅️ SAIR DO ADMIN"): 
        st.session_state.admin_logado = False
        st.session_state.view = "home"; st.rerun()
    
    st.title("🛡️ Painel de Gestão")
    t1, t2, t3 = st.tabs(["🔄 Ordem", "👥 Usuários", "🛠️ Avisos"])
    
    with t1:
        nova = st.multiselect("Vitrine:", options=list(st.session_state.pastas.keys()), default=st.session_state.ordem)
        if st.button("Salvar Ordem"): st.session_state.ordem = nova; st.success("Salvo!")
            
    with t2:
        for user in st.session_state.usuarios: st.write(f"👤 {user['nome']}")
        
    with t3:
        st.subheader("Controle de Avisos do Site")
        # Chave para ligar/desligar a mensagem "ESTAMOS TRABALHANDO"
        st.session_state.manutencao = st.toggle("Ativar aviso: ESTAMOS TRABALHANDO", value=st.session_state.manutencao)
        if st.session_state.manutencao:
            st.warning("O aviso está visível para todos os visitantes agora.")
        else:
            st.info("O site está em modo normal.")

# VITRINE HOME
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
