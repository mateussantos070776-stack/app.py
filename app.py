import streamlit as st
import os
import random
from PIL import Image
import io

# 1. CONFIGURAÇÃO E CRIAÇÃO DE PASTAS
st.set_page_config(page_title="KERIGMA | Galeria Coletiva", layout="wide")

PASTA_GALERIA = "galeria_kerigma"
ARQUIVO_ATIVAS = "chaves_ativas.txt"
ARQUIVO_USADOS = "chaves_usadas.txt"

# Cria as pastas e arquivos necessários se não existirem
if not os.path.exists(PASTA_GALERIA):
    os.makedirs(PASTA_GALERIA)

for arq in [ARQUIVO_ATIVAS, ARQUIVO_USADOS]:
    if not os.path.exists(arq):
        with open(arq, "w") as f: f.write("")

# 2. FUNÇÕES DE SUPORTE
def listar_chaves(arquivo):
    with open(arquivo, "r") as f: return f.read().splitlines()

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

# 3. CSS PREMIUM
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');
    header {visibility: hidden !important;}
    .block-container {padding-top: 0rem !important;}
    .stApp { background-color: #050505; color: white; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: #0a0a0a !important; border-right: 2px solid #E50914 !important; }
    .main-title { font-weight: 900; font-size: 5rem; color: #E50914; text-align: center; margin-top: 10vh; letter-spacing: -2px; }
    div.stButton > button { background-color: #E50914 !important; color: white !important; font-weight: 700 !important; border-radius: 8px !important; height: 50px;}
    .card-galeria { background: rgba(255, 255, 255, 0.03); border: 1px solid #333; border-radius: 10px; padding: 15px; margin-bottom: 20px; transition: 0.3s; }
    .card-galeria:hover { border-color: #E50914; background: rgba(229, 9, 20, 0.05); }
    </style>
    """, unsafe_allow_html=True)

if 'tela' not in st.session_state: st.session_state.tela = "home"

# 4. BARRA LATERAL
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#E50914;'>SISTEMA KERIGMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # ADMIN
    senha_mestre = st.text_input("Senha Mestre", type="password")
    if st.button("ENTRAR COMO ADMIN"):
        if senha_mestre == "1234":
            st.session_state.tela = "master"
            st.rerun()
    
    st.write("---")
    
    # MEMBRO
    chave_membro = st.text_input("Chave de Integrante", type="password")
    if st.button("ACESSAR GALERIA"):
        ativas = listar_chaves(ARQUIVO_ATIVAS)
        if chave_membro in ativas:
            salvar_chave(chave_membro, ARQUIVO_USADOS)
            novas_ativas = [c for c in ativas if c != chave_membro]
            with open(ARQUIVO_ATIVAS, "w") as f:
                for c in novas_ativas: f.write(c + "\n")
            st.session_state.tela = "membro"
            st.rerun()
    
    st.write("---")
    if st.button("SAIR / INÍCIO"):
        st.session_state.tela = "home"
        st.rerun()

# 5. TELAS

if st.session_state.tela == "home":
    st.markdown('<h1 class="main-title">KERIGMA MAANAIM</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing:15px; color:#444;'>DIGITAL MEDIA HUB</p>", unsafe_allow_html=True)

elif st.session_state.tela == "master":
    st.markdown("<h2 style='color:#E50914;'>PAINEL MASTER</h2>", unsafe_allow_html=True)
    if st.button("✨ GERAR NOVA CHAVE PARA MEMBRO"):
        nova = "".join([str(random.randint(0, 9)) for _ in range(10)])
        salvar_chave(nova, ARQUIVO_ATIVAS)
        st.success(f"Chave Gerada: {nova}")
    
    st.write("---")
    st.subheader("Chaves Ativas")
    st.write(listar_chaves(ARQUIVO_ATIVAS))

elif st.session_state.tela == "membro":
    st.markdown("<h1 style='color:#E50914;'>GALERIA COLETIVA KERIGMA</h1>", unsafe_allow_html=True)
    
    # Upload de novo arquivo
    with st.expander("➕ ADICIONAR NOVA FOTO À GALERIA"):
        upload = st.file_uploader("Selecione a imagem", type=["jpg", "png", "jpeg"])
        if upload:
            caminho_destino = os.path.join(PASTA_GALERIA, upload.name)
            with open(caminho_destino, "wb") as f:
                f.write(upload.getbuffer())
            st.success("Imagem adicionada à galeria de todos os membros!")
            st.rerun()

    st.write("---")
    
    # Exibição da Galeria
    arquivos = os.listdir(PASTA_GALERIA)
    if not arquivos:
        st.info("A galeria está vazia. Adicione a primeira foto acima!")
    else:
        # Cria um grid de 3 colunas
        cols = st.columns(3)
        for i, nome_arquivo in enumerate(arquivos):
            caminho_completo = os.path.join(PASTA_GALERIA, nome_arquivo)
            with cols[i % 3]:
                st.markdown('<div class="card-galeria">', unsafe_allow_html=True)
                st.image(caminho_completo, use_container_width=True)
                st.write(f"📁 {nome_arquivo}")
                
                # Opções de Download
                d1080 = preparar_download(caminho_completo, 1920)
                st.download_button("Download 1080p", d1080, f"1080p_{nome_arquivo}", "image/png", key=f"d10{i}")
                
                d720 = preparar_download(caminho_completo, 1280)
                st.download_button("Download 720p", d720, f"720p_{nome_arquivo}", "image/png", key=f"d72{i}")
                st.markdown('</div>', unsafe_allow_html=True)
