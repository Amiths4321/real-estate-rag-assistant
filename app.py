import streamlit as st
from rag import ask_question, load_vectorstore

st.set_page_config(
    page_title="Real Estate AI Assistant",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Real Estate AI Assistant")
st.caption("Powered by IBM Granite on GPU + RERA & MahaRERA documents")

@st.cache_resource
def get_vectorstore():
    return load_vectorstore()

vectorstore = get_vectorstore()

st.markdown("**Try asking:**")
suggestions = [
    "What are RERA registration requirements for a developer?",
    "What is the penalty for project delay under RERA?",
    "What documents does a buyer need for due diligence?",
    "What is the carpet area definition under RERA?"
]

cols = st.columns(2)
for i, q in enumerate(suggestions):
    if cols[i % 2].button(q, key=f"sug_{i}", use_container_width=True):
        st.session_state["question"] = q

question = st.text_input(
    "Ask your question:",
    value=st.session_state.get("question", ""),
    placeholder="e.g. What are RERA penalties for delayed possession?"
)

if st.button("Ask", type="primary") and question:
    with st.spinner("Searching documents and thinking..."):
        result = ask_question(question, vectorstore)

    st.markdown("### Answer")
    st.markdown(result["answer"])

    with st.expander(f"Sources used ({len(result['sources'])} documents)"):
        for src in result["sources"]:
            st.markdown(f"- 📄 `{src}`")

    st.caption(f"Based on {result['chunks_used']} relevant passages")