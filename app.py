import streamlit as st

# Título da página baseado no seu PDF original
st.set_page_config(page_title="Viva o Propósito", page_icon="🙏")

st.title("VIVA O PRÓPOSITO EM ORAÇÃO")
st.subheader("Acesso ao conteúdo da pregação")

# Sistema de Login (As credenciais do seu projeto)
with st.form(key='login_form'):
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    botao_entrar = st.form_submit_button(label='ENTRAR')
    
    if botao_entrar:
        if usuario == "admin" and senha == "1234":
            st.success("BUSCAR-ME-EIS E ME ACHAREIS!")
            st.balloons()
            st.write("---")
            st.markdown("""
            ### Resumo do Estudo - Jeremias 29
            * **1. O Contexto**: O exílio de 70 anos e a promessa de retorno.
            * **2. A Dor**: As lutas fazem parte do propósito (Jó, Elias e Jesus).
            * **3. A Direção**: Orar e prosperar durante o processo.
            * **4. A Libertação**: O decreto de Ciro e a mudança de sorte.
            """)
        else:
            st.error("Acesso negado. Busque de todo o coração.")
