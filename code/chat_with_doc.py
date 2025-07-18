import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import json
import time
import uuid
import datetime
from PIL import Image

def chat_with_doc():
    start_time = time.time()
    
    # Loading the required image to display
    image = Image.open('assets\\qa.png')
    # Display image using Streamlit
    st.image(image, caption='', width=200)

    st.header("Chat With Doc 🌐🔁")
    
    if 'application_id' not in st.session_state:
        st.warning("Please enter your application id in authentication page to proceed.")
        return
    
    application_id = st.session_state.application_id
    st.text(f"Application ID: {application_id}")
    # Placeholder for displaying the response
    response_placeholder = st.empty()

    # Ensure the embeddings and vectorstore are in the session state
    embeddings = st.session_state.get("openai_embeddings")
    vectorstore = st.session_state.get("vectorstore")

    if embeddings is None or vectorstore is None:
        st.error("OpenAI embeddings or vectorstore not found in session state.")
        return
    
    # Initialize the question-response history in session state if not already done
    if 'qa_history' not in st.session_state:
        st.session_state.qa_history = []

    user_question = st.text_input("👨‍💼 Ask anything to the chat", key="user_question")

    if user_question:
        llm = ChatOpenAI(model="gpt-4o")
        docs = vectorstore.similarity_search(query=user_question, k=3)
        
        chain = load_qa_chain(llm=llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_question)
        
        st.session_state.qa_history.append((user_question, response))

        # Display the question-response history
        response_text = ""
        for question, response in st.session_state.qa_history:
            response_text += f"❔ **Question:** {question}\n\n🤖 **Response:** {response}\n\n"

        response_placeholder.markdown(response_text)
        # Clear the text input value after the response is displayed
        # st.session_state.user_question = ""

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    chat_with_doc()
