import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DE TELA
st.set_page_config(
    page_title="KERIGMA | Sistema", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE ESTADOS ---
if 'tela' not in st.session_state: 
    st.session_state.tela = "home"
if 'chave_gerada' not in st.session_state: 
    st.session_state.chave_gerada = ""
if 'texto_mural' not in st.session_state:
    st.session_state.texto_mural = "Bem-vindo à Equipe Mídia Maanaim"

# 2. CSS MASTER
st.markdown("""
    <style>
    header, [data-testid="stHeader"] { display: none !important; }
    
    .stApp {
        margin-top: -50px !important;
        background-color: #050505;
    }

    button[title="Collapse sidebar"], [data-testid="sidebar-button"] { display: none !important; }

    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 2px solid #E50914 !important;
        min-width: 260px !important;
    }

    /* BOTÕES DA SIDEBAR (VERMELHOS) */
    .stSidebar .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        height: 48px !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100% !important;
        margin-bottom: 5px !important;
    }

    /* BOTÕES CENTRAIS (VERMELHOS) */
    div[data-testid="stVerticalBlock"] div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: #FFFFFF !important;
        font-weight: 800 !important;
        border: none !important;
        width: 100% !important;
        height: 45px !important;
        border-radius: 8px !important;
    }

    /* INPUTS BRANCOS */
    .stTextInput input, .stTextArea textarea {
        background-color: white !important;
        color: #000000 !important;
        font-weight: 600 !important;
        border-radius: 5px !important;
    }
    
    /* COR DA LETRA AO CLICAR (FOCO) */
    .stTextInput input:focus, .stTextArea textarea:focus {
        color: #E50914 !important;
    }

    /* COR DA LETRA ANTES DE DIGITAR (PLACEHOLDER) */
    .stTextInput input::placeholder, .stTextArea textarea::placeholder {
        color: #000000 !important;
        opacity: 0.6;
    }

    h1, h2, h3, p { font-family: 'Montserrat', sans-serif; color: white; }
    .block-container { padding-top: 2rem !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='color:#E50914; text-align:center; font-weight:900; margin-bottom:20px;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 ÁREA DE MEMBROS"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("💬 CHAT"): st.session_state.tela = "chat"; st.rerun()
    if st.button("⚙️ ACESSO ADMIN"): st.session_state.tela = "login_admin"; st.rerun()
    st.write("---")

# 4. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:3.5rem; color:#E50914; text-align:center; margin-top:100px; font-weight:900;">EQUIPE MIDIA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown(f"""
        <div style="text-align:center; margin-top:30px; padding:20px; border:1px solid #E50914; border-radius:10px;">
            <p style="color:#E50914; font-weight:bold; letter-spacing:2px;">MURAL DE AVISOS</p>
            <h2 style="color:white; font-weight:300;">{st.session_state.texto_mural}</h2>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        st.text_input("Nome Completo")
        st.text_input("Chave de Acesso", type="password")
        if st.button("ENTRAR"): st.session_state.tela = "painel_membro"; st.rerun()

elif st.session_state.tela == "chat":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>💬 CHAT AO VIVO</h1>", unsafe_allow_html=True)
    st.text_area("Mensagens", value="Sistema pronto.", height=300, label_visibility="collapsed")
    c_msg, c_send = st.columns([4, 1])
    with c_msg: st.text_input("Sua mensagem...", label_visibility="collapsed")
    with c_send: st.button("ENVIAR")

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1.2, 1])
    with col_adm:
        senha = st.text_input("Senha Master", type="password")
        if st.button("ACESSAR COMANDO"):
            if senha == "55420": st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL DE COMANDO MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<p style='color:#E50914; font-weight:bold;'>🔑 GERADOR</p>", unsafe_allow_html=True)
        
        # EXIBIÇÃO DO NÚMERO EM CAIXA BRANCA COM LETRA VERMELHA (RESOLVE O VERDE)
        chave = st.session_state.chave_gerada if st.session_state.chave_gerada else "---"
        st.markdown(f"""
            <div style="background-color: white; color: #E50914; padding: 10px; 
                        border-radius: 5px; text-align: center; font-size: 25px; 
                        font-weight: 800; border: 1px solid #E50914; margin-bottom: 10px;">
                {chave}
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("NOVA CHAVE"):
            st.session_state.chave_gerada = str(random.randint(100000, 999999))
            st.rerun()
    with c2:
        st.markdown("<p style='color:#E50914; font-weight:bold;'>📢 MURAL</p>", unsafe_allow_html=True)
        novo_aviso = st.text_area("Escreva aqui o aviso para a Home", height=68, label_visibility="collapsed")
        if st.button("PUBLICAR"):
            st.session_state.texto_mural = novo_aviso
            st.rerun()
    with c3:
        st.markdown("<p style='color:#E50914; font-weight:bold;'>🔔 NOTIF.</p>", unsafe_allow_html=True)
        st.text_input("Assunto", label_visibility="collapsed")
        st.button("ENVIAR")
