import streamlit as st
import os, random, json, string

# 1. CONFIGURAÇÃO E PERSISTÊNCIA
st.set_page_config(page_title="KERIGMA", layout="wide", initial_sidebar_state="expanded")

def gerenciar_dados(acao, id_u=None, chave=None):
    caminho = "usuarios_kerigma.json"
    dados = json.load(open(caminho, "r")) if os.path.exists(caminho) else {}
    if acao == "salvar": dados[id_u] = chave
    elif acao == "deletar": dados.pop(id_u, None)
    if acao in ["salvar", "deletar"]: json.dump(dados, open(caminho, "w"))
    return dados

# --- ESTADOS ---
for k, v in {"tela": "home", "autenticado": False, "id_g": "", "ch_g": "", "mural": "Bem-vindo à Mídia Maanaim"}.items():
    if k not in st.session_state: st.session_state[k] = v

# 2. CSS MASTER COMPACTO
st.markdown("""
    <style>
    header {visibility: hidden;}
    .block-container { padding: 1rem 2rem !important; }
    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 2px solid #E50914 !important;
        min-width: 260px !important; position: fixed !important; 
        height: 100vh !important; transform: none !important; z-index: 999;
    }
    [data-testid="sidebar-button"], button[title*="sidebar"] { display: none !important; }
    .stApp { background-color: #050505; }
    .stButton>button {
        background: linear-gradient(135deg, #E50914, #9e070e) !important;
        color: white !important; font-weight: 700 !important; width: 100% !important; border: none !important;
    }
    .stTextInput input { background: white !important; color: black !important; }
    h1, h2, h3, p, label { color: white !important; font-family: 'Montserrat', sans-serif; }
    .card { border: 1px dashed #E50914; padding: 15px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center;'>KERIGMA</h2>", unsafe_allow_html=True)
    if st.button("🏠 HOME"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 MEMBROS"): st.session_state.tela = "painel_membro" if st.session_state.autenticado else "login_membro"; st.rerun()
    if st.button("⚙️ ADM"): st.session_state.tela = "master" if st.session_state.autenticado else "login_admin"; st.rerun()
    if st.session_state.autenticado and st.button("🚪 SAIR"):
        st.session_state.autenticado = False; st.session_state.tela = "home"; st.rerun()

# 4. TELAS
if st.session_state.tela == "home":
    st.markdown(f'<div style="text-align:center; margin-top:50px; border:1px solid #E50914; padding:30px; border-radius:10px;"><h1>MÍDIA MAANAIM</h1><h3>{st.session_state.mural}</h3></div>', unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        u = st.text_input("ID").strip().upper()
        c = st.text_input("CHAVE", type="password")
        if st.button("ENTRAR"):
            db = gerenciar_dados("carregar")
            if u in db and db[u] == c:
                st.session_state.autenticado, st.session_state.tela = True, "painel_membro"; st.rerun()
            else: st.error("Incorreto.")

elif st.session_state.tela == "master":
    if not st.session_state.autenticado: st.rerun()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<div class="card"><p>NOVO ACESSO</p><h2>ID: {st.session_state.id_g or "---"}</h2><h2>CH: {st.session_state.ch_g or "---"}</h2></div>', unsafe_allow_html=True)
        if st.button("GERAR"):
            st.session_state.id_g = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            st.session_state.ch_g = ''.join(random.choices(string.digits, k=6))
            gerenciar_dados("salvar", st.session_state.id_g, st.session_state.ch_g); st.rerun()
    with c2:
        db = gerenciar_dados("carregar")
        for u, ch in db.items():
            col_t, col_d = st.columns([0.8, 0.2])
            col_t.write(f"ID: {u} | CH: {ch}")
            if col_d.button("🗑️", key=u): gerenciar_dados("deletar", u); st.rerun()

elif st.session_state.tela == "painel_membro":
    st.markdown('<h1 style="text-align:center; color:#E50914; margin-top:100px;">ACESSO CONFIRMADO</h1>', unsafe_allow_html=True)

elif st.session_state.tela == "login_admin":
    _, col, _ = st.columns([1, 1, 1])
    with col:
        if st.text_input("Master", type="password") == "55420" and st.button("ACESSAR"):
            st.session_state.autenticado, st.session_state.tela = True, "master"; st.rerun()
