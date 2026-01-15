import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="KERIGMA | Master Portal", layout="wide")

# 2. BANCO DE DADOS (TEXTO)
ARQUIVO_ATIVAS = "chaves_ativas.txt"
ARQUIVO_USADOS = "chaves_usadas.txt"

for arq in [ARQUIVO_ATIVAS, ARQUIVO_USADOS]:
    if not os.path.exists(arq):
        with open(arq, "w") as f: f.write("")

def listar_chaves(arquivo):
    with open(arquivo, "r") as f: return f.read().splitlines()

def salvar_chave(chave, arquivo):
    with open(arquivo, "a") as f: f.write(chave + "\n")

# 3. CSS PARA UI CINEMATOGRÁFICA
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');
    header {visibility: hidden !important;}
    .block-container {padding-top: 0rem !important;}
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: #0a0a0a !important; border-right: 2px solid #E50914 !important; }
    .main-title { font-weight: 900; font-size: 5rem; color: #E50914; text-align: center; margin-top: 10vh; letter-spacing: -2px; }
    div.stButton > button { background-color: #E50914 !important; color: white !important; font-weight: 700 !important; border-radius: 8px !important; border: none; height: 50px;}
    .master-card { background: rgba(229, 9, 20, 0.05); padding: 40px; border-radius: 15px; border: 1px solid #E50914; text-align: center; }
    .key-list { background: rgba(255, 255, 255, 0.05); padding: 10px; border-radius: 5px; margin: 5px 0; display: flex; justify-content: space-between; align-items: center; }
    </style>
    """, unsafe_allow_html=True)

# 4. CONTROLE DE ESTADO
if 'tela' not in st.session_state: st.session_state.tela = "home"

# 5. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#E50914;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # ACESSO ADMIN GERAL
    st.markdown("### 👑 MASTER ACCESS")
    senha_mestre = st.text_input("Senha Mestre", type="password")
    if st.button("ENTRAR COMO ADMIN"):
        if senha_mestre == "1234":  # SENHA ATUALIZADA
            st.session_state.tela = "master"
            st.rerun()
        else:
            st.error("Senha Mestre Inválida")

    st.write("---")

    # ACESSO INTEGRANTE
    st.markdown("### 🔒 ACESSO MEMBRO")
    chave_membro = st.text_input("Chave de 10 dígitos", type="password")
    if st.button("VALIDAR MEMBRO"):
        ativas = listar_chaves(ARQUIVO_ATIVAS)
        usadas = listar_chaves(ARQUIVO_USADOS)
        if chave_membro in ativas and chave_membro not in usadas:
            salvar_chave(chave_membro, ARQUIVO_USADOS)
            novas_ativas = [c for c in ativas if c != chave_membro]
            with open(ARQUIVO_ATIVAS, "w") as f:
                for c in novas_ativas: f.write(c + "\n")
            st.session_state.tela = "membro"
            st.rerun()
        else:
            st.error("Chave inválida ou já utilizada.")

    st.write("---")
    if st.button("VOLTAR AO INÍCIO"):
        st.session_state.tela = "home"
        st.rerun()

# 6. TELAS

# TELA HOME
if st.session_state.tela == "home":
    st.markdown('<h1 class="main-title">KERIGMA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing:15px; color:#444;'>DIGITAL MEDIA HUB</p>", unsafe_allow_html=True)

# TELA MASTER (GERADOR)
elif st.session_state.tela == "master":
    st.markdown('<h1 style="color:#E50914; text-align:center;">PAINEL MASTER GERAL</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="master-card">', unsafe_allow_html=True)
        st.subheader("Gerador de Acessos")
        if st.button("✨ GERAR NOVA CHAVE ALEATÓRIA"):
            nova = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova, ARQUIVO_ATIVAS)
            st.success("Nova chave gerada!")
            st.code(nova, language="text")
        
        st.write("---")
        st.markdown("### Gestão de Chaves Ativas")
        ativas = listar_chaves(ARQUIVO_ATIVAS)
        
        if not ativas:
            st.info("Nenhuma chave disponível.")
        else:
            for c in ativas:
                col_key, col_del = st.columns([3, 1])
                col_key.code(c)
                if col_del.button("Apagar", key=c):
                    ativas.remove(c)
                    with open(ARQUIVO_ATIVAS, "w") as f:
                        for rest in ativas: f.write(rest + "\n")
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# TELA MEMBRO
elif st.session_state.tela == "membro":
    st.markdown('<h1 style="color:#E50914;">ÁREA DO INTEGRANTE</h1>', unsafe_allow_html=True)
    st.write("---")
    st.success("Bem-vindo à área de produção.")
    st.file_uploader("Enviar arquivos de mídia", type=["mp4", "mov", "png", "jpg"])
