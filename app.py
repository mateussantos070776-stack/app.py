import streamlit as st
import os
import random

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="KERIGMA MAANAIM | Admin", layout="wide")

# 2. ARQUIVOS DE BANCO DE DADOS (TEXTO)
ARQUIVO_ATIVAS = "chaves_ativas.txt" # Chaves que você gerou e podem ser usadas
ARQUIVO_USADAS = "chaves_usadas.txt" # Chaves que já foram descartadas

# Inicializa os arquivos se não existirem
for arq in [ARQUIVO_ATIVAS, ARQUIVO_USADAS]:
    if not os.path.exists(arq):
        with open(arq, "w") as f: f.write("")

# Funções de Gerenciamento
def listar_chaves(arquivo):
    with open(arquivo, "r") as f: return f.read().splitlines()

def salvar_chave(chave, arquivo):
    with open(arquivo, "a") as f: f.write(chave + "\n")

def remover_chave_ativa(chave):
    ativas = listar_chaves(ARQUIVO_ATIVAS)
    if chave in ativas:
        ativas.remove(chave)
        with open(ARQUIVO_ATIVAS, "w") as f:
            for c in ativas: f.write(c + "\n")

# 3. CSS PARA REMOVER O TOPO BRANCO E ESTILIZAR
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');
    header {visibility: hidden !important;}
    .block-container {padding-top: 1rem !important;}
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: #0a0a0a !important; border-right: 2px solid #E50914 !important; }
    .main-title { font-weight: 900; font-size: 5rem; color: #E50914; text-align: center; margin-top: 5vh; letter-spacing: -2px; }
    div.stButton > button { background-color: #E50914 !important; color: white !important; font-weight: 700 !important; width: 100%; border-radius: 8px !important; border: none; }
    .admin-box { background: rgba(229, 9, 20, 0.1); padding: 20px; border-radius: 10px; border: 1px dashed #E50914; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - DOIS NÍVEIS DE ACESSO
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#E50914;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    
    # --- ÁREA DO ADMINISTRADOR (VOCÊ) ---
    with st.expander("🔑 PAINEL DO ADMIN GERAL"):
        master_pass = st.text_input("Senha Mestre", type="password")
        if master_pass == "ADMIN123": # <--- ALTERE SUA SENHA MESTRE AQUI
            st.markdown('<div class="admin-box">', unsafe_allow_html=True)
            if st.button("✨ GERAR NOVA CHAVE"):
                nova_chave = "".join([str(random.randint(0, 9)) for _ in range(10)])
                salvar_chave(nova_chave, ARQUIVO_ATIVAS)
                st.success(f"Chave Gerada: {nova_chave}")
                st.code(nova_chave) # Facilita copiar e colar
            
            st.write("Chaves Ativas:", len(listar_chaves(ARQUIVO_ATIVAS)))
            st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")

    # --- ÁREA DO INTEGRANTE (MEMBROS) ---
    if 'logado' not in st.session_state: st.session_state.logado = False

    if not st.session_state.logado:
        st.markdown("### 🔒 Acesso Membro")
        chave_input = st.text_input("Chave de 10 dígitos", type="password")
        
        if st.button("VALIDAR ACESSO"):
            ativas = listar_chaves(ARQUIVO_ATIVAS)
            usadas = listar_chaves(ARQUIVO_USADAS)
            
            if chave_input in usadas:
                st.error("Chave expirada/usada.")
            elif chave_input in ativas:
                registrar_chave_usada(chave_input) # Grava como usada
                remover_chave_ativa(chave_input)   # Tira das disponíveis
                salvar_chave(chave_input, ARQUIVO_USADAS) # Garante o bloqueio permanente
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Chave inválida.")
    else:
        st.success("SESSÃO ATIVA")
        if st.button("SAIR"):
            st.session_state.logado = False
            st.rerun()

# 5. CONTEÚDO PRINCIPAL
if not st.session_state.logado:
    st.markdown('<h1 class="main-title">KERIGMA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#444;'>DIGITAL MEDIA HUB | ACESSO RESTRITO</p>", unsafe_allow_html=True)
else:
    st.markdown('<h1 style="color:#E50914; font-weight:900;">PAINEL DE PRODUÇÃO</h1>', unsafe_allow_html=True)
    st.write("Bem-vindo integrante. Esta chave foi inutilizada.")
