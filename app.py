import streamlit as st
import google.generativeai as genai

# Configuração da chave
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="BrainBuilder AI", layout="wide")

st.title("🧠 BrainBuilder AI - Painel de Controle")

# Barra lateral
with st.sidebar:
    st.header("📂 Configuração")
    nicho_escolhido = st.selectbox(
        "Selecione o Nicho:", 
        ["Saúde & Estética", "Imobiliário", "Jurídico", "Gastronomia"]
    )

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Entrada de Dados")
    entrada = st.text_area("Cole o texto bagunçado aqui:", height=300)

with col2:
    st.subheader("✨ Manual Estruturado")
    if st.button("🚀 Organizar com IA"):
        if entrada:
            with st.spinner("IA trabalhando..."):
                try:
                    # Linha corrigida e alinhada
                    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
                    prompt = f"Como consultor especialista em {nicho_escolhido}, organize este texto em um manual de processos: {entrada}"
                    response = model.generate_content(prompt)
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Erro: {e}")
        else:
            st.warning("Escreva algo primeiro!")
            
                       
