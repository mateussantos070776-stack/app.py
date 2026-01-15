# ... (mantenha o início do código igual até a parte das TELAS)

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
    st.markdown("<h1 style='color:#E50914; text-align:center;'>EXCLUSIVO MÍDIA</h1>", unsafe_allow_html=True)
    
    # Criando o Layout 3x3 de Janelas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card-galeria">### 📸 FOTOS<br>Galeria Coletiva</div>', unsafe_allow_html=True)
        if st.button("ACESSAR FOTOS"): st.session_state.sub_view = "fotos"

    with col2:
        st.markdown('<div class="card-galeria">### 🎥 VÍDEOS<br>Arquivos Brutos</div>', unsafe_allow_html=True)
        st.button("VER VÍDEOS", key="v1")

    with col3:
        st.markdown('<div class="card-galeria">### 🎨 ARTES<br>Identidade Visual</div>', unsafe_allow_html=True)
        st.button("BAIXAR ASSETS", key="v2")

    # Segunda Linha
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown('<div class="card-galeria">### 📝 ROTEIROS<br>Scripts e Ideias</div>', unsafe_allow_html=True)
        st.button("LER AGORA", key="v3")
    
    with col5:
        st.markdown('<div class="card-galeria">### 🎵 ÁUDIOS<br>Trilhas Kerigma</div>', unsafe_allow_html=True)
        st.button("OUVIR", key="v4")

    with col6:
        st.markdown('<div class="card-galeria">### 🗓️ AGENDA<br>Cronograma Mídia</div>', unsafe_allow_html=True)
        st.button("VER DATAS", key="v5")

    # Exibição da Galeria (Só aparece se clicar no botão de fotos)
    if st.session_state.get('sub_view') == "fotos":
        st.write("---")
        # Coloque aqui o código de listagem de arquivos da galeria que você já tinha
        arquivos = os.listdir(PASTA_GALERIA)
        st.subheader("Galeria de Imagens")
        if arquivos:
            cols_img = st.columns(4)
            for idx, img in enumerate(arquivos):
                with cols_img[idx % 4]:
                    st.image(os.path.join(PASTA_GALERIA, img))
