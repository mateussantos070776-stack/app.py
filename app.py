import streamlit as st
import os
import random
from PIL import Image
import io

# 1. CONFIGURAÇÃO INICIAL E SESSION STATE
st.set_page_config(page_title="KERIGMA | Exclusivo Mídia", layout="wide")

if 'tela' not in st.session_state:
    st.session_state.tela = "home"
if 'sub_view' not in st.session_state:
    st.session_state.sub_view = None

PASTA_GALERIA = "galeria_kerigma"
ARQUIVO_ATIVAS = "chaves_ativas.txt"
ARQUIVO_USADOS = "chaves_usadas.txt"

if not os.path.exists(PASTA_GALERIA):
    os.makedirs(PASTA_GALERIA)

for arq in [ARQUIVO_ATIVAS, ARQUIVO_USADOS]:
    if not os.path.exists(arq):
        with open(arq, "w") as f: f.write("")

# 2. FUNÇÕES DE SUPORTE
def listar_chaves(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f: return f.read().splitlines()
    return []

def salvar_chave(chave, arquivo):
    with open(arquivo, "a") as f: f.write(chave + "\n")

# 3. CSS PREMIUM (ESTÉTICA, GRADIENTES E CARDS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300;400;700;900&display=swap');
    
    header {visibility: hidden !important;}
    
    .stApp { 
        background: radial-gradient(circle at center, #0f0f0f 0%, #050505 100%);
        color: white; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    .main-title { 
        font-family: 'Great Vibes', cursive; 
        font-weight: 400; 
        font-size: 6.5rem; 
        color: #E50914; 
        text-align: center; 
        text-shadow: 2px 2px 15px rgba(229, 9, 20, 0.3);
        margin-top: 5vh;
        margin-bottom: -10px;
    }

    .sub-title {
        text-align: center; 
        letter-spacing: 15px; 
        color: #555; 
        font-weight: 300;
        margin-bottom: 40px;
        font-size: 0.8rem;
        text-transform: uppercase;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #E50914 0%, #9e070e 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(229, 9, 20, 0.2);
        transition: all 0.4s ease;
        display: block;
        margin: 0 auto;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(229, 9, 20, 0.4);
    }

    div[data-testid="stTextInput"] input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 10px !important;
        text-align: center;
    }

    .card-janela {
        background: linear-gradient(145deg, rgba(30, 30, 30, 0.6) 0%, rgba(10, 10, 10, 0.8) 100%);
        border: 1px solid rgba(229, 9, 20, 0.1);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 10px;
    }
    
    .card-janela:hover { 
        border-color: #E50914; 
        background: linear-gradient(145deg, rgba(40, 40, 40, 0.8) 0%, rgba(20, 20, 20, 0.9) 100%);
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(229, 9, 20, 0.15);
    }

    .card-janela h3 { color: #E50914; font-weight: 900; letter-spacing: 2px; margin-bottom: 10px; }
    .card-janela p { color: #aaa; font-size: 0.9rem; font-weight: 300; }

    [data-testid="stSidebar"] { 
        background-color: #080808 !important; 
        border-right: 1px solid rgba(229, 9, 20, 0.2) !important; 
    }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#E50914; font-weight:900;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("SAIR / INÍCIO"):
        st.session_state.tela = "home"
        st.session_state.sub_view = None
        st.rerun()

# 5. LÓGICA DE TELAS

# TELA: HOME
if st.session_state.tela == "home":
    st.markdown('<div style="height: 12vh;"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Digital Media Hub</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        chave_membro = st.text_input("", placeholder="INSIRA SUA CHAVE SAGRADA", type="password")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("ENTRAR NO MAANAIM"):
            ativas = listar_chaves(ARQUIVO_ATIVAS)
            if chave_membro == "admin123":
                st.session_state.tela = "master"
                st.rerun()
            elif chave_membro in ativas:
                st.session_state.tela = "membro"
                st.rerun()
            else:
                st.error("Chave não reconhecida.")

# TELA: PAINEL MASTER
elif st.session_state.tela == "master":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900;'>PAINEL MASTER</h1>", unsafe_allow_html=True)
    st.write("---")
    col_adm1, col_adm2 = st.columns(2)
    with col_adm1:
        st.markdown('<div class="card-janela">', unsafe_allow_html=True)
        if st.button("✨ GERAR NOVA CHAVE"):
            nova = "".join([str(random.randint(0, 9)) for _ in range(10)])
            salvar_chave(nova, ARQUIVO_ATIVAS)
            st.success(f"CHAVE: {nova}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_adm2:
        st.subheader("CHAVES ATIVAS")
        chaves = listar_chaves(ARQUIVO_ATIVAS)
        for c in chaves: st.code(c)

# TELA: EXCLUSIVO MÍDIA
elif st.session_state.tela == "membro":
    st.markdown("<h1 style='color:#E50914; text-align:center; font-weight:900; letter-spacing:5px;'>EXCLUSIVO MÍDIA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#555; margin-bottom:50px; font-weight:700;'>ADMINISTRAÇÃO DE CONTEÚDO SANTO</p>", unsafe_allow_html=True)
    
    # Listas de dados para o Grid
    titulos = ["📸 FOTOS", "🎥 VÍDEOS", "🎨 ARTES", "📝 ROTEIROS", "🎵 ÁUDIOS", "🗓️ AGENDA"]
    descricoes = ["Galeria Coletiva", "Arquivos Brutos", "Identidade Visual", "Scripts e Ideias", "Trilhas Kerigma", "Escala de Mídia"]
    chaves_btn = ["btn_f", "btn_v", "btn_a", "btn_r", "btn_au", "btn_ag"]

    # Grid 3x3 (2 linhas x 3 colunas)
    for i in range(2):
        cols = st.columns(3)
        for j in range(3):
            idx = (i * 3) + j
            with cols[j]:
                st.markdown(f"""
                    <div class="card-janela">
                        <h3>{titulos[idx]}</h3>
                        <p>{descricoes[idx]}</p>
                    </div>
                """, unsafe_allow_html=True)
                if st.button("ACESSAR", key=chaves_btn[idx]):
                    if titulos[idx] == "📸 FOTOS":
                        st.session_state.sub_view = "fotos"

    # Sub-view da Galeria
    if st.session_state.get('sub_view') == "fotos":
        st.write("---")
        st.subheader("📸 Galeria de Imagens")
        with st.expander("➕ ADICIONAR FOTO"):
            upload = st.file_uploader("Upload", type=["jpg", "png", "jpeg"])
            if upload:
                with open(os.path.join(PASTA_GALERIA, upload.name), "wb") as f:
                    f.write(upload.getbuffer())
                st.rerun()

        arquivos = os.listdir(PASTA_GALERIA)
        if arquivos:
            cols_img = st.columns(4)
            for i, img in enumerate(arquivos):
                with cols_img[i % 4]:
                    st.image(os.path.join(PASTA_GALERIA, img), use_container_width=True)
