import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="KERIGMA MAANAIM | Hub Oficial",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. INICIALIZAÇÃO SECRETA DAS CHAVES (ESTADO DO SERVIDOR)
# Estas chaves são de uso único. Uma vez usadas, são removidas da lista.
if 'chaves_disponiveis' not in st.session_state:
    st.session_state.chaves_disponiveis = [
        "5294017386", "1084739522", "8472016493", "3950284716", "6621049385",
        "2173958404", "9048217362", "4539102877", "7816402931", "1394857209"
    ]

if 'membro_logado' not in st.session_state:
    st.session_state.membro_logado = False

# 3. CSS PREMIUM (UI CINEMATOGRÁFICA)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;900&display=swap');
    .stApp { background: radial-gradient(circle at 50% -20%, #1a1a1a 0%, #000000 100%); color: #f5f5f5; font-family: 'Montserrat', sans-serif; }
    [data-testid="stSidebar"] { background-color: rgba(10, 10, 10, 0.98); border-right: 1px solid #E50914; }
    .main-title { font-weight: 900; font-size: 4rem; color: #E50914; text-transform: uppercase; text-align: center; margin-top: 50px; 
                  background: linear-gradient(180deg, #ff1e1e 0%, #a80000 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    div.stButton > button { background: #E50914 !important; color: white !important; font-weight: 700 !important; width: 100%; border: none !important; border-radius: 8px !important; height: 45px; }
    div.stButton > button:hover { background: #ff1e2d !important; box-shadow: 0 0 20px rgba(229,9,20,0.5) !important; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL: VALIDAÇÃO SECRETA E DESCARTÁVEL
with st.sidebar:
    st.markdown("<h3 style='text-align:center; color:#E50914;'>SISTEMA KERIGMA</h3>", unsafe_allow_html=True)
    st.write("---")
    
    if not st.session_state.membro_logado:
        st.markdown("### 🔒 Área Restrita")
        chave_input = st.text_input("Credencial de 10 dígitos", type="password", placeholder="0000000000")
        
        if st.button("VERIFICAR ACESSO"):
            if chave_input in st.session_state.chaves_disponiveis:
                # LÓGICA DE USO ÚNICO: Remove a chave da lista secreta
                st.session_state.chaves_disponiveis.remove(chave_input)
                st.session_state.membro_logado = True
                st.success("Credencial Validada! Esta chave foi inutilizada para novos acessos.")
                st.rerun()
            else:
                st.error("Acesso Negado: Chave inexistente ou já utilizada.")
    else:
        st.success("✅ DISPOSITIVO AUTORIZADO")
        st.info(f"Chaves restantes no lote: {len(st.session_state.chaves_disponiveis)}")
        if st.button("ENCERRAR SESSÃO"):
            st.session_state.membro_logado = False
            st.rerun()

# 5. CONTEÚDO PRINCIPAL (DINÂMICO)
if not st.session_state.membro_logado:
    # Interface Pública / Home
    st.markdown('<h1 class="main-title">MIDIA KERIGMA</h1>', unsafe_allow_html=True)
    st.image("https://lh3.googleusercontent.com/d/1B8LjYZmHsjpyZPC96FaYAODskWrwOVJC", width=300) # Imagem proporcional
    st.markdown("<p style='text-align:center; letter-spacing:10px; color:#555;'>MAANAIM DIGITAL EXPERIENCE</p>", unsafe_allow_html=True)
    st.write("##")
    st.info("Aguardando validação de credencial na barra lateral esquerda...")
else:
    # Interface Profissional para Integrantes (Área Restrita)
    st.markdown('<h1 style="color:#E50914; font-weight:900;">DASHBOARD DE MÍDIA</h1>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.subheader("🎬 Repositório de Vídeos")
        st.file_uploader("Upload de Master (4K/HD)", type=["mp4", "mkv", "mov"])
    
    with col_b:
        st.subheader("📢 Avisos da Equipe")
        st.code("Reunião de pauta às 19h.\nVerificar áudio do Salmo 23.", language="text")

    st.write("---")
    st.subheader("📂 Arquivos Recentes")
    st.table([{"Arquivo": "Abertura_Evento.mp4", "Tamanho": "1.2GB", "Autor": "Admin"},
              {"Arquivo": "Estudo_Biblico_01.mp4", "Tamanho": "850MB", "Autor": "Mídia"}])
