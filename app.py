import streamlit as st
from transformers import pipeline

# Title
st.set_page_config(page_title="LaymanLens", layout="centered")
st.title("📚 LaymanLens – Complex to Simple Explanation")

# Input Text
user_input = st.text_area("Enter a technical or complex sentence:")

# Load summarization pipeline (you can switch to your custom model if hosted)
@st.cache_resource
def load_model():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_model()

# Summarize on button click
if st.button("Simplify"):
    if user_input.strip() != "":
        with st.spinner("Simplifying..."):
            summary = summarizer(user_input, max_length=60, min_length=15, do_sample=False)
            st.subheader("Layman's Explanation:")
            st.success(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text.")
