import streamlit as st
import google.generativeai as genai

# Conecta com a chave que guardaste no Streamlit
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="BrainBuilder AI", layout="wide")

# Título do App
st.title("🧠 BrainBuilder AI - Painel de Controle")

# Menu de Escolha de Nicho
with st.sidebar:
    st.header("📂 Configuração")
    nicho_escolhido = st.selectbox(
        "Selecione o Nicho do Cliente:", 
        ["Saúde & Estética", "Imobiliário", "Jurídico", "Gastronomia", "Indústria Local"]
    )
    st.info(f"Nicho Ativo: {nicho_escolhido}")

# Área de Trabalho
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Entrada de Dados")
    entrada = st.text_area("Cole o texto bagunçado aqui:", height=300)

with col2:
    st.subheader("✨ Manual Estruturado")
    if st.button("🚀 Organizar com IA"):
        if entrada:
            with st.spinner("A processar..."):
                try:
           model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')
                    prompt = f"Como consultor especialista em {nicho_escolhido}, organiza este texto num manual de processos: {entrada}"
                    response = model.generate_content(prompt)
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Erro: {e}")
        else:
            st.warning("Escreve algo primeiro!")
                       
