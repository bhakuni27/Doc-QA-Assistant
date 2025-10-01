import streamlit as st
from src.app import DocQAAssistant

st.set_page_config(page_title="Doc QA Assistant", page_icon="📄", layout="wide")

st.title("📄 Document Question Answering Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    assistant = DocQAAssistant(uploaded_file)

    st.success("✅ Document processed. Ask me questions!")
    question = st.text_input("Enter your question:")

    if question:
        answer, retrieved_chunks = assistant.answer_question(question)

        st.subheader("Answer")
        st.write(answer)

        with st.expander("📌 Retrieved Context"):
            for idx, chunk in enumerate(retrieved_chunks, 1):
                st.markdown(f"**Chunk {idx}:** {chunk}")
