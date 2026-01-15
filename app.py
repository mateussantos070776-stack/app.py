import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="KERIGMA | Master Portal", layout="wide")

# 2. BANCO DE DADOS (TEXTO)
ARQUIVO_ATIVAS = "chaves_ativas.txt"
ARQUIVO_USADAS = "chaves_usadas.txt"

for arq in [ARQUIVO_ATIVAS, ARQUIVO_USADAS]:
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
    </style>
    """, unsafe_allow_html=True)

# 4. CONTROLE DE ESTADO (NAVEGAÇÃO)
if 'tela' not in st.session_state: st.session_state.tela = "home"

# 5. BARRA LATERAL (ENTRADAS)
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#E50914;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # ACESSO ADMIN GERAL
    st.markdown("### 👑 MASTER ACCESS")
    senha_mestre = st.text_input("Senha Mestre", type="password")
    if st.button("ENTRAR COMO ADMIN"):
        if senha_mestre == "ADMIN123": # Altere aqui sua senha
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
        usadas = listar_chaves(ARQUIVO_USADAS)
        if chave_membro in ativas and chave_membro not in usadas:
            # Move para usadas
            salvar_chave(chave_membro, ARQUIVO_USADAS)
            # Remove das ativas
            novas_ativas = [c for c in ativas if c != chave_membro]
            with open(ARQUIVO_ATIVAS, "w") as f:
                for c in novas_ativas: f.write(c + "\n")
            
            st.session_state.tela = "membro"
            st.rerun()
        else:
            st.error("Chave inválida ou já utilizada.")

    if st.button("VOLTAR AO INÍCIO"):
        st.session_state.tela = "home"
        st.rerun()

# 6. TELAS (CONTEÚDO PRINCIPAL)

# TELA HOME (PÚBLICA)
if st.session_state.tela == "home":
    st.markdown('<h1 class="main-title">KERIGMA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing:15px; color:#444;'>DIGITAL MEDIA HUB</p>", unsafe_allow_html=True)

# TELA MASTER (GERADOR DE CHAVES)
elif st.session_state.tela == "master":
    st.markdown('<h1 style="color:#E50914; text-align:center;">PAINEL MASTER GERAL</h1>', unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="master-card">', unsafe_allow_html=True)
        st.subheader("Gerador de Acessos")
        if st.button("✨ GERAR NOVA CHAVE ALEATÓRIA"):
            nova = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova, ARQUIVO_ATIVAS)
            st.success("Chave gerada e salva com sucesso!")
            st.code(nova, language="text")
        
        st.write("---")
        st.markdown("### Chaves Ativas no Sistema")
        ativas = listar_chaves(ARQUIVO_ATIVAS)
        if ativas:
            for c in ativas:
                st.text(f"• {c}")
        else:
            st.write("Nenhuma chave ativa.")
        st.markdown('</div>', unsafe_allow_html=True)

# TELA MEMBRO (ÁREA DE PRODUÇÃO)
elif st.session_state.tela == "membro":
    st.markdown('<h1 style="color:#E50914;">ÁREA DO INTEGRANTE</h1>', unsafe_allow_html=True)
    st.write("---")
    st.success("Bem-vindo à área de produção. Sua chave foi descartada pelo sistema para sua segurança.")
    
    # Exemplo de conteúdo de mídia
    cols = st.columns(3)
    cols[0].metric("Arquivos Hoje", "12")
    cols[1].metric("Usuários Online", "1")
    cols[2].metric("Status do Servidor", "100%")
    
    st.file_uploader("Enviar arquivos de mídia", type=["mp4", "mov", "png", "jpg"])
