import streamlit as st
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain_community.llms import Ollama
from langchain.chat_models import ChatOpenAI
import json

# Helper function to load frequently asked questions from a JSON file
def load_faqs():
    with open("constant//faqs.json", "r") as f:
        return json.load(f)

# Function to process a question and fetch an answer using the vector store
def process_faq(question, vectorstore, llm):
    docs = vectorstore.similarity_search(query=question, k=3)  # Find similar chunks
    chain = load_qa_chain(llm=llm, chain_type="stuff")  # Load QA chain
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=question)  # Generate response
    return response

# FAQs Page
def faqs_page():
    st.header("Frequently Asked Questions (FAQs) 🤔")

    # Check if vector store and embeddings are in session state
    if "vectorstore" not in st.session_state or "openai_embeddings" not in st.session_state:
        st.warning("Please upload documents in the 'Document Generator' page before accessing FAQs.")
        return

    # Model selection (reusing the model choice for consistency)
    model_choice = st.selectbox("Select a Model", ["GPT-4o", "LLAMA3"])
    llm = ChatOpenAI() if model_choice == "GPT-4o" else Ollama(model="llama3")

    # Load FAQs from JSON
    faqs = load_faqs()
    vectorstore = st.session_state.vectorstore  # Load vector store from session state

    # Display and answer each FAQ
    st.subheader("Here are some FAQs based on your uploaded documents:")
    for faq in faqs["questions"]:
        question = faq.get("question", "No question provided")
        st.markdown(f"**Q: {question}**")

        # Generate an answer
        answer = process_faq(question, vectorstore, llm)
        st.write(f"**A:** {answer}")

if __name__ == "__main__":
    faqs_page()
