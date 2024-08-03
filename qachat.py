# from dotenv import load_dotenv
# load_dotenv() #loading the environment variables
# from PIL import Image

# import streamlit as st
# import os
# import google.generativeai as genai


# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # function to load Gemini Pro Model and get response

# model = genai.GenerativeModel("gemini-pro")
# chat = model.start_chat(history=[])

# def get_gemini_response(question):
#     response = chat.send_message(question, stream=True)
#     return response

# # initialize our streamlit

# st.set_page_config(page_title='Q&A Demo')
# st.header('Gemini LLM Application')

# # Initialize session state chat history if it doesnt exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# input = st.text_input("Input: ", key='input')
# submit = st.button("Ask the Question")

# if submit  and input:
#     response = get_gemini_response(input)

#     # Add user query and respond to session chat
#     st.session_state['chat_history'].append(('You', input))
#     st.subheader("The Response is:")
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(('Bot', input))
# st.subheader("The chat history is")

# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")

import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()  # Load environment variables

# Function to initialize the Gemini Pro model and start a chat
def initialize_model():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-pro")
    return model.start_chat(history=[])

# Function to get Gemini response
def get_gemini_response(chat, question):
    return chat.send_message(question, stream=True)

# Streamlit app
def main():
    st.set_page_config(page_title="Q&A Demo")
    st.header("Gemini LLM Chat Application")

    # Initialize chat history and model
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
        st.session_state['chat'] = initialize_model()

    # User input and submit button
    user_input = st.text_input("Input:")
    if st.button("Ask the Question") and user_input:
        response = get_gemini_response(st.session_state['chat'], user_input)
        st.session_state['chat_history'].append(('You', user_input))
        st.subheader("The Response is:")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(('Bot', chunk.text))

    # Display chat history
    st.subheader("Chat History")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")

if __name__ == "__main__":
    main()
