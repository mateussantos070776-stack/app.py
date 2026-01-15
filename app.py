# ... (mantenha as configurações iniciais, CSS e sidebar como estão)

elif st.session_state.tela == "membro":
    st.markdown("<h1 style='color:#E50914; text-align:center;'>EXCLUSIVO MÍDIA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888; margin-bottom:40px;'>CENTRAL DE ACESSO KERIGMA</p>", unsafe_allow_html=True)
    
    # Grid 3x3 para os tipos de conteúdos
    # Aqui você pode personalizar cada "janela" para uma função específica
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card-galeria">', unsafe_allow_html=True)
        st.markdown("### 📸 GALERIA GERAL")
        st.write("Fotos coletivas da comunidade.")
        if st.button("ABRIR GALERIA", key="btn_galeria"):
            st.session_state.sub_view = "galeria_fotos"
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card-galeria">', unsafe_allow_html=True)
        st.markdown("### 🎥 VÍDEOS / REELS")
        st.write("Brutos e editados para redes.")
        if st.button("VER VÍDEOS", key="btn_videos"):
            st.info("Módulo de vídeos em breve.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card-galeria">', unsafe_allow_html=True)
        st.markdown("### 🎨 IDENTIDADE")
        st.write("Logos, fontes e assets visuais.")
        if st.button("ACESSAR ASSETS", key="btn_assets"):
            pass
        st.markdown('</div>', unsafe_allow_html=True)

    # Segunda Linha do Grid
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown('<div class="card-galeria">', unsafe_allow_html=True)
        st.markdown("### 📂 DOCUMENTOS")
        st.write("Roteiros e planejamentos.")
        st.button("ABRIR PASTA", key="btn_docs")
        st.markdown('</div>', unsafe_allow_html=True)

    with col5:
        st.markdown('<div class="card-galeria">', unsafe_allow_html=True)
        st.markdown("### 🎵 ÁUDIOS")
        st.write("Trilhas e locuções.")
        st.button("OUVIR", key="btn_audio")
        st.markdown('</div>', unsafe_allow_html=True)

    with col6:
        st.markdown('<div class="card-galeria">', unsafe_allow_html=True)
        st.markdown("### 🗓️ CRONOGRAMA")
        st.write("Datas de postagens e eventos.")
        st.button("VER CALENDÁRIO", key="btn_cal")
        st.markdown('</div>', unsafe_allow_html=True)

    # Logica para exibir a Galeria de Fotos se selecionada
    if 'sub_view' in st.session_state and st.session_state.sub_view == "galeria_fotos":
        st.write("---")
        st.subheader("📸 Galeria Coletiva de Fotos")
        
        # Upload dentro da sub-view
        with st.expander("➕ ENVIAR NOVA FOTO"):
            upload = st.file_uploader("Selecione a imagem", type=["jpg", "png", "jpeg"])
            if upload:
                caminho_destino = os.path.join(PASTA_GALERIA, upload.name)
                with open(caminho_destino, "wb") as f:
                    f.write(upload.getbuffer())
                st.success("Imagem adicionada!")
                st.rerun()

        # Listagem das fotos
        arquivos = os.listdir(PASTA_GALERIA)
        if arquivos:
            img_cols = st.columns(3)
            for i, nome_arquivo in enumerate(arquivos):
                caminho_completo = os.path.join(PASTA_GALERIA, nome_arquivo)
                with img_cols[i % 3]:
                    st.image(caminho_completo, use_container_width=True)
                    d1080 = preparar_download(caminho_completo, 1920)
                    st.download_button(f"Baixar {nome_arquivo}", d1080, nome_arquivo, "image/png", key=f"dl_{i}")
