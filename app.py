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
if 'sorteados' not in st.session_state:
    st.session_state.sorteados = []

# LISTA DE MEMBROS CADASTRADOS (Exemplo)
membros_equipe = ["Lucas Silva", "Ana Souza", "Mateus Oliveira", "Bárbara Reis", "João Pedro", "Clara Mendes", "Rafael Vaz"]

# 2. CSS MASTER
st.markdown("""
    <style>
    [data-testid="sidebar-button"], 
    button[title="Collapse sidebar"], 
    button[title="Expand sidebar"] {
        display: none !important;
    }

    [data-testid="stSidebar"] {
        background-color: #111111 !important;
        border-right: 2px solid #E50914 !important;
        min-width: 260px !important;
        margin-left: 0 !important;
        transform: none !important;
        transition: none !important;
    }

    .stApp { background-color: #050505; }

    /* ESTILO DOS BOTÕES */
    .stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100% !important;
    }

    /* INPUTS */
    .stTextInput input, .stTextArea textarea {
        background-color: white !important;
        color: #000000 !important;
        font-weight: 600 !important;
    }

    h1, h2, h3, p { font-family: 'Montserrat', sans-serif; color: white; }
    
    /* ESTILO NOMES SORTEADOS */
    .nome-sorteado {
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL
with st.sidebar:
    st.markdown("<br><h2 style='color:#E50914; text-align:center; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🏠 HOME"): st.session_state.tela = "home"; st.rerun()
    if st.button("🔴 MEMBROS MÍDIA"): st.session_state.tela = "login_membro"; st.rerun()
    if st.button("💬 CHAT"): st.session_state.tela = "chat"; st.rerun()
    if st.button("⚙️ KERIGMA ADM"): st.session_state.tela = "login_admin"; st.rerun()
    st.write("---")

# 4. LÓGICA DE TELAS
if st.session_state.tela == "home":
    st.markdown('<h1 style="font-size:3.5rem; color:#E50914; text-align:center; margin-top:80px; font-weight:900;">EQUIPE MIDIA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align:center; margin-top:30px; padding:30px; border:2px solid #E50914; border-radius:15px;"><p style="color:#E50914; font-weight:bold; letter-spacing:3px;">MURAL DE AVISOS</p><h2 style="color:white; font-weight:300;">{st.session_state.texto_mural}</h2></div>', unsafe_allow_html=True)

elif st.session_state.tela == "login_admin":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ACESSO LIDERANÇA</h1>", unsafe_allow_html=True)
    _, col_adm, _ = st.columns([1, 1.2, 1])
    with col_adm:
        senha = st.text_input("Senha Master", type="password")
        if st.button("ACESSAR SALA ADM"):
            if senha == "55420": st.session_state.tela = "master"; st.rerun()

elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CENTRAL MÍDIA</h1>", unsafe_allow_html=True)
    st.write("---")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("<p style='color:#E50914; font-weight:bold;'>🔑 GERADOR</p>", unsafe_allow_html=True)
        st.code(st.session_state.chave_gerada if st.session_state.chave_gerada else "---")
        if st.button("NOVA CHAVE"):
            st.session_state.chave_gerada = str(random.randint(100000, 999999))
            st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        # BOTÃO QUE LEVA PARA A TELA DE SORTEIO
        if st.button("🎲 SORTEIO DE MÍDIA"):
            st.session_state.tela = "sorteio"
            st.rerun()
        if st.button("📸 FOTOS"): pass
        if st.button("🎬 VÍDEOS"): pass

    with c2:
        st.markdown("<p style='color:#E50914; font-weight:bold;'>📢 MURAL</p>", unsafe_allow_html=True)
        novo_aviso = st.text_area("Novo aviso...", height=68, label_visibility="collapsed")
        if st.button("PUBLICAR"):
            st.session_state.texto_mural = novo_aviso
            st.rerun()

    with c3:
        st.markdown("<p style='color:#E50914; font-weight:bold;'>🔔 NOTIF.</p>", unsafe_allow_html=True)
        st.text_input("Assunto", key="notif_input", label_visibility="collapsed")
        st.button("ENVIAR")

# --- NOVA TELA: SORTEIO ---
elif st.session_state.tela == "sorteio":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>SORTEIO DE ESCALA</h1>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("REALIZAR SORTEIO"):
            # Sorteia 2 pessoas diferentes da lista de membros
            st.session_state.sorteados = random.sample(membros_equipe, 2)
        
        st.write("<br>", unsafe_allow_html=True)
        
        if st.session_state.sorteados:
            st.markdown("<p style='color:#888; text-align:center;'>Pessoas selecionadas para a escala:</p>", unsafe_allow_html=True)
            for pessoa in st.session_state.sorteados:
                st.markdown(f"""
                    <div class="nome-sorteado">
                        <span style="color:white; font-size:18px; font-weight:600;">{pessoa}</span>
                        <span style="color:#28a745; font-size:20px;">● Online/Escalado ✅</span>
                    </div>
                """, unsafe_allow_html=True)
        
        st.write("<br>")
        if st.button("VOLTAR PARA CENTRAL"):
            st.session_state.tela = "master"
            st.rerun()

# --- OUTRAS TELAS (LOGIN MEMBRO / CHAT) ---
elif st.session_state.tela == "login_membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>ÁREA DE MEMBROS</h1>", unsafe_allow_html=True)
    if st.button("VOLTAR"): st.session_state.tela = "home"; st.rerun()

elif st.session_state.tela == "chat":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>CHAT</h1>", unsafe_allow_html=True)
    if st.button("VOLTAR"): st.session_state.tela = "home"; st.rerun()
