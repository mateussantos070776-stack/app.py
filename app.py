import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Arquivo de Pregações", page_icon="📖")

st.title("📂 MINHAS PREGAÇÕES")
st.write("---")

# 1. Menu de Pastas (Categorias)
# Isso funciona como pastas organizadas para o público
pasta_selecionada = st.sidebar.selectbox(
    "Selecione a Pasta de Estudos:",
    ["Jeremias 29 (Viva o Propósito)", "Personagens Bíblicos", "Promessas de Deus"]
)

# 2. Conteúdo da Pasta: Jeremias 29
if pasta_selecionada == "Jeremias 29 (Viva o Propósito)":
    st.header("📍 Série: Viva o Propósito")
    
    with st.expander("Estudo 1: O Contexto do Exílio"):
        st.write("Conteúdo sobre os 70 anos de cativeiro e a soberania de Deus.")
        
    with st.expander("Estudo 2: O Propósito na Dor"):
        st.write("Reflexão sobre as dores de Jó, Elias e Jesus.")
        
    with st.expander("Estudo 3: O Que Fazer no Processo?"):
        st.write("Instruções bíblicas: Edificar, plantar e orar pela paz.")

# 3. Conteúdo da Pasta: Personagens Bíblicos
elif pasta_selecionada == "Personagens Bíblicos":
    st.header("👥 Estudos sobre Personagens")
    
    with st.expander("A Fé de Abraão"):
        st.write("Como a obediência gera frutos permanentes.")
        
    with st.expander("A Coragem de Davi"):
        st.write("Vencendo gigantes através da confiança em Deus.")

# 4. Conteúdo da Pasta: Promessas de Deus
elif pasta_selecionada == "Promessas de Deus":
    st.header("✨ As Promessas Inabaláveis")
    st.info("Buscar-me-eis e me achareis quando me buscardes de todo o vosso coração.")

# Rodapé Público
st.write("---")
st.caption("Site atualizado via GitHub e Streamlit Cloud.")
