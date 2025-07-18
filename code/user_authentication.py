import streamlit as st
from PIL import Image
import os
from doc_generator_page import load_embeddings, text_embeddings
import json
import datetime

# Function to authenticate the user
def authenticate_user(application_id):
    # Check if the application ID contains any alphanumeric character
    if any(char.isalnum() for char in application_id):
        return True
    else:
        return False

# Function to check if embeddings exist for the given application ID
def check_embeddings(application_id, text_embeddings):
    embeddings_file = f"{application_id}_embeddings.pkl"
    if os.path.exists(embeddings_file):
        return load_embeddings(application_id, text_embeddings)
    else:
        return None

# Function to create the user authentication page
def main():
    # Loading the required image to display
    image = Image.open('assets\\user_authentication.jpg')
    # Display image using Streamlit
    st.image(image, caption='', width=225)
    st.header("User Authentication 🔐")

    #Opening database json file
    with open("constant\\database.json", "r") as f:
            database = json.load(f)

    # Check if the application ID is already in session state
    if 'application_id' in st.session_state and st.session_state.application_id:
        application_id = st.session_state.application_id
        st.text_input("Enter Application ID", value=application_id, disabled=True)
    
        st.success("Authenticated successfully!")
        # Check if embeddings exist for the given application ID
        user_embeddings = check_embeddings(application_id, text_embeddings)
        if user_embeddings is not None:
            st.session_state.openai_embeddings = text_embeddings
            st.session_state.vectorstore = user_embeddings
            st.write("Embeddings found for the user ID")
        else:
            st.write("No embeddings found for the user ID")
    else:
        application_id = st.text_input("Enter Application ID")
        
        if st.button("Authenticate"):
            if authenticate_user(application_id):
                st.session_state.application_id = application_id
                st.success("Authenticated successfully!")
                # Check if embeddings exist for the given application ID
                user_embeddings = check_embeddings(application_id, text_embeddings)
                if user_embeddings is not None:
                    st.session_state.openai_embeddings = text_embeddings
                    st.session_state.vectorstore = user_embeddings
                    st.write("Embeddings found for the Application ID")
                else:
                    st.write("No embeddings found for the Application ID")

                if application_id in database.keys():
                    st.write("Application ID found in database")
                else:
                    database[application_id] = {
                        "doc_list": [
                            
                        ]
                    }
                    # Debugging statement to check the database update
                    #st.write("Updated database entry: ", database[application_id])
                    new_database = json.dumps(database, indent=4)
                    with open("constant\\database.json", "w") as f:
                        f.write(new_database)
                    st.write("Application ID added to the database")
            else:
                st.error("Authentication failed. Please enter a valid Application ID.")

    if st.button("Reset Session"):
        # Clear session state
        st.session_state.clear()
        st.success("Session has been reset.")

if __name__ == "__main__":
    main()
