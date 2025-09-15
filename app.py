import google.generativeai as genai
import streamlit as st
import os

# get api from local env
key=os.getenv('GOOGLE_API_KEY')

# Configure the model
genai.configure(api_key=key)
model=genai.GenerativeModel('gemini-2.5-flash-lite')

# Create a frontend UI
st.title('Simple Text Generation')
st.header('This is to test the gemini model as application')
prompt=st.text_input('Write your prompt here',max_chars=10000)
if prompt:
    response=model.generate_content(prompt)
    st.write(response.text)

