from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# ✅ FIRST Streamlit command
st.set_page_config(page_title="Q&A Demo")

# Configure API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found in .env file.")
else:
    genai.configure(api_key=api_key)

# Debug: List available models
with st.expander("Available Models"):
    try:
        models = genai.list_models()
        for m in models:
            if "generateContent" in m.supported_generation_methods:
                st.write(f"✅ {m.name}")
            else:
                st.write(f"⚠️ {m.name} (No generateContent)")
    except Exception as e:
        st.error(f"Could not list models: {e}")

# Load Gemini model
try:
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None

# Get response from Gemini
def get_gemini_response(question):
    if model:
        response = model.generate_content(question)
        return response.text
    else:
        return "Model not loaded properly."

# Streamlit UI
st.header("Gemini Application")

user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and user_input:
    try:
        response = get_gemini_response(user_input)
        st.subheader("The Response is")
        st.write(response)
    except Exception as e:
        st.error(f"Error generating content: {e}")
