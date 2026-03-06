import streamlit as st

# Configuração da Página
st.set_page_config(page_title="BrainBuilder AI", layout="wide")

# Barra Lateral com Nichos
with st.sidebar:
    st.title("📂 Nichos")
    nicho = st.selectbox("Selecione o Nicho:", ["Saúde", "Imobiliário", "Jurídico", "Gastronomia", "Indústria"])

# Dashboard Principal
st.title(f"🧠 BrainBuilder - {nicho}")

# Área de Upload
c1, c2 = st.columns(2)
with c1:
    st.subheader("📥 Entrada de Dados")
    entrada = st.text_area("Cole a bagunça aqui:", height=300)
    
with c2:
    st.subheader("✨ Saída Estruturada")
    if st.button("🚀 Organizar com IA"):
        st.write("Conecte sua API Key para processar.")

st.divider()
st.button("📄 Gerar PDF de Consultoria")
