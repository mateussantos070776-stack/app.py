import streamlit as st
import os
import random
from PIL import Image
import io

# 1. CONFIGURAÇÃO INICIAL E SESSION STATE
st.set_page_config(page_title="KERIGMA | Exclusivo Mídia", layout="wide")

# Inicialização para evitar NameError
if 'tela' not in st.session_state:
    st.session_state.tela = "home"
if 'sub_view' not in st.session_state:
    st.session_state.sub_view = None

PASTA_GALERIA = "galeria_kerigma"
ARQUIVO_ATIVAS = "chaves_ativas.txt"
ARQUIVO_USADOS = "chaves_usadas.txt"

# Criação de pastas e arquivos base
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

def preparar_download(caminho_img, largura_alvo):
    img = Image.open(caminho_img)
    proporcao = largura_alvo / float(img.size[0])
    altura_alvo = int((float(img.size[1]) * float(proporcao)))
    img_redimensionada = img.resize((largura_alvo, altura_alvo), Image.LANCZOS)
    buf = io.BytesIO()
    img_redimensionada.save(buf, format="PNG")
    return buf.getvalue()

# 3. CSS PREMIUM (DESIGN CENTRALIZADO E FONTE ELEGANTE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@400;700;900&display=swap');
    
    header {visibility: hidden !important;}
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    
    /* Título com Rabisco Elegante */
    .main-title { 
        font-family: 'Great Vibes', cursive; 
        font-weight: 400; 
        font-size: 6rem; 
        color: #E50914; 
        text-align: center; 
        margin-top: 5vh;
        margin-bottom: -10px;
    }

    /* Subtítulo Hub */
    .sub-title {
        text-align: center; 
        letter-spacing: 12px; 
        color: #444; 
        font-weight: 700;
        margin-bottom: 40px;
        font-size: 0.9rem;
    }

    /* Botão Vermelho Centralizado */
    div.stButton > button {
        background-color: #E50914 !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        height: 50px;
        width: 100%;
        max-width: 300px;
        display: block;
        margin: 0 auto;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #b20710 !important;
        transform: scale(1.02);
    }

    /* Centralização de Inputs */
    div[data-testid="stTextInput"] {
        max-width: 400px;
        margin: 0 auto;
    }

    /* Janelas 3x3 do Exclusivo Mídia */
    .card-janela {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid #333;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        transition: 0.3s;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin-bottom: 15px;
    }
    .card-janela:hover { 
        border-color: #E50914; 
        background: rgba(229, 9, 20, 0.05); 
    }

    [data-testid="stSidebar"] { background-color: #0a0a0a !important; border-right: 1px solid #222 !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#E50914;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("SAIR / INÍCIO"):
        st.session_state.tela = "home"
        st.session_state.sub_view = None
        st.rerun()

# 5. LÓGICA DE TELAS

# TELA: HOME
if st.session_state.tela == "home":
    st.markdown('<div style="height: 15vh;"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">Kerigma Maanaim</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">DIGITAL MEDIA HUB</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        chave_membro = st.text_input("", placeholder="Chave de Integrante", type="password")
        if st.button("ACESSAR EXCLUSIVO MÍDIA"):
            ativas = listar_chaves(ARQUIVO_ATIVAS)
            if chave_membro in ativas:
                # Opcional: remover chave após uso ou registrar
                st.session_state.tela = "membro"
                st.rerun()
            elif chave_membro == "admin123": # Senha mestra temporária
                st.session_state.tela = "master"
                st.rerun()
            else:
                st.error("Chave inválida ou já utilizada.")

# TELA: PAINEL MASTER (ADMIN)
elif st.session_state.tela == "master":
    st.markdown("<h2 style='color:#E50914;'>PAINEL MASTER</h2>", unsafe_allow_html=True)
    if st.button("✨ GERAR NOVA CHAVE PARA MEMBRO"):
        nova = "".join([str(random.randint(0, 9)) for _ in range(10)])
        salvar_chave(nova, ARQUIVO_ATIVAS)
        st.success(f"Chave Gerada: {nova}")
    
    st.write("---")
    st.subheader("Chaves Disponíveis")
    st.write(listar_chaves(ARQUIVO_ATIVAS))

# TELA: EXCLUSIVO MÍDIA (MEMBRO)
elif st.session_state.tela == "membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>EXCLUSIVO MÍDIA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; margin-bottom:50px;'>SELECIONE A CATEGORIA DE CONTEÚDO</p>", unsafe_allow_html=True)
    
    # Grid 3x3
    row1_1, row1_2, row1_3 = st.columns(3)
    with row1_1:
        st.markdown('<div class="card-janela"><h3>📸 FOTOS</h3><p>Galeria Coletiva</p></div>', unsafe_allow_html=True)
        if st.button("ABRIR", key="btn_fotos"): st.session_state.sub_view = "fotos"
        
    with row1_2:
        st.markdown('<div class="card-janela"><h3>🎥 VÍDEOS</h3><p>Arquivos Brutos</p></div>', unsafe_allow_html=True)
        st.button("ABRIR", key="btn_videos")
        
    with row1_3:
        st.markdown('<div class="card-janela"><h3>🎨 ARTES</h3><p>Identidade Visual</p></div>', unsafe_allow_html=True)
        st.button("ABRIR", key="btn_artes")

    row2_1, row2_2, row2_3 = st.columns(3)
    with row2_1:
        st.markdown('<div class="card-janela"><h3>📝 ROTEIROS</h3><p>Scripts e Ideias</p></div>', unsafe_allow_html=True)
        st.button("ABRIR", key="btn_roteiros")
        
    with row2_2:
        st.markdown('<div class="card-janela"><h3>🎵 ÁUDIOS</h3><p>Trilhas Kerigma</p></div>', unsafe_allow_html=True)
        st.button("ABRIR", key="btn_audios")
        
    with row2_3:
        st.markdown('<div class="card-janela"><h3>🗓️ AGENDA</h3><p>Escala de Mídia</p></div>', unsafe_allow_html=True)
        st.button("ABRIR", key="btn_agenda")

    # Área de Conteúdo da Galeria de Fotos
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
                    st.caption(img)
