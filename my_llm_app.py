import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

# Input field for OpenAI API key
openai_api_key = st.sidebar.text_input('OpenAI API Key')

# Function to generate LLM response
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm.invoke(input_text))

# User input form
with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')

    # Check if API key is valid
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')

    # Generate response when form is submitted
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)