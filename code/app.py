import streamlit as st
from user_authentication import main as user_authentication
from doc_generator_page import doc_generator_page
from chat_with_doc import chat_with_doc
from faq_handler import faqs_page
from history_page import history_page
from quiz_page import quiz_page
from training_page import training_page
from document_comparison_page import document_comparison_page
from generate_procedure_manual_page import generate_procedure_manual_page
from document_comparison_with_reference import document_comparison_with_reference

def welcome_page():
    st.markdown("<h1 style='text-align: center; font-family: Arial; color: #4CAF50;'>Operational AI Assistant</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="text-align: center; font-size: 18px; line-height: 1.6; font-family: Arial; margin-top: 20px;">
        Welcome to the Operational AI Assistant for Bank of Muscat!  
        Your trusted partner in navigating operational challenges with precision and intelligence.  
        </div>
        
        <div style="text-align: left; margin-top: 30px; font-family: Arial;">
        <ul style="font-size: 18px; color: #333;">
            <li>🚀 <strong>Operational Advice:</strong> Get tailored, AI-powered recommendations for enhanced decision-making.</li>
            <li>💡 <strong>FAQs Section:</strong> Quickly find answers to common queries, designed to keep you informed and efficient.</li>
            <li>🎯 <strong>Interactive Quizzes:</strong> Test your knowledge and sharpen your skills in a fun and engaging way.</li>
        </ul>
        </div>
        
        <div style="text-align: center; margin-top: 20px; font-size: 18px; font-family: Arial; color: #555;">
        Empower yourself with cutting-edge AI solutions and transform the way you handle operations.  
        Let’s embark on this journey of innovation and excellence together!
        </div>
        """,
        unsafe_allow_html=True,
    )

# Sidebar Navigation
st.sidebar.title('App Navigation')

icons = {
    'Welcome': '🏠',
    'OA Generator': '🚀',
    'History': '📜',
    'User Authentication': '🔐',
    'Doc Generator': '📄',
    'Chat With Doc': '🌐',
    'FAQs': '💡',
    'Quiz': '🎓',
    'Training': '🏋️‍♂️',
    'Document Comparison Page': '📝',
    'Generate Procedure Manual': '📝',
    'Doc Comparison With Reference Doc': '📝',
}

# Main Navigation
selection = st.sidebar.radio("Navigate to:", 
    ['Welcome', 'OA Generator', 'History'], 
    format_func=lambda x: f"{icons[x]} {x}")

# Conditional Pages
if selection == 'Welcome':
    welcome_page()
elif selection == 'OA Generator':
    sub_selection = st.sidebar.radio(
        "Subpage Options:",
        ['User Authentication', 'Doc Generator', 'Chat With Doc', 'FAQs', 'Quiz', 'Training', 'Document Comparison Page','Generate Procedure Manual','Doc Comparison With Reference Doc'],
        format_func=lambda x: f"{icons[x]} {x}"
    )
    if sub_selection == 'User Authentication':
        user_authentication()
    elif sub_selection == 'Doc Generator':
        doc_generator_page()
    elif sub_selection == 'Chat With Doc':
        chat_with_doc()
    elif sub_selection == 'FAQs':
        faqs_page()
    elif sub_selection== 'Quiz':
        quiz_page()
    elif sub_selection== 'Training':
        training_page()
    elif sub_selection== 'Document Comparison Page':
        document_comparison_page()
    elif sub_selection== 'Generate Procedure Manual':
        generate_procedure_manual_page()
    elif sub_selection== 'Doc Comparison With Reference Doc':
        document_comparison_with_reference()

elif selection == 'History':
    history_page()
