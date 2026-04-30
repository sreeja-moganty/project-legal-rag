import streamlit as st
from retriever import build_retriever, retrieve
from rag_pipeline import generate_answer, expand_query


st.set_page_config(page_title="Legal RAG System", layout="wide")

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1 {
    color: #1f4e79;
}
.stButton>button {
    background-color: #1f4e79;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.title("⚖️ Agentic Legal RAG System")
st.markdown("### Explainable Legal Case Analysis using AI")

st.markdown("---")

@st.cache_resource
def load_system():
    return build_retriever()

index, texts = load_system()

col1, col2 = st.columns([3,1])

with col1:
    query = st.text_input("🔍 Enter your legal query")

with col2:
    run = st.button("Run Analysis")

st.markdown("**Example queries:**")
st.write("- What are fraud-related legal cases?")
st.write("- Explain judgement reasoning in fraud cases")
st.write("- What types of legal disputes occur in financial fraud?")

st.markdown("---")

if run:

    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        with st.spinner("🔄 Analyzing legal documents..."):

            queries = expand_query(query)

            all_docs = []
            for q in queries:
                docs = retrieve(q, index, texts)
                all_docs.extend(docs)

            unique_docs = list(set(all_docs))

            if len(unique_docs) == 0:
                st.error("No relevant documents found.")
            else:
                st.subheader("🔍 Retrieved Sources")

                for i, doc in enumerate(unique_docs[:3]):
                    with st.expander(f"Source {i+1}"):
                        st.write(doc)

                answer = generate_answer(query, unique_docs)

                st.subheader("🧠 Final AI Answer")
                st.success(answer)

st.markdown("---")
st.caption("Built with RAG + FAISS + LLM + Agentic Architecture")
