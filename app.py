import streamlit as st
from transformers import pipeline

# ✅ Cache the model so it's only loaded once
@st.cache_resource
def load_model():
    return pipeline("text-classification", model="Swethaa02/laymanlens-v1")

# Load model from cache
model = load_model()

# Streamlit app UI
st.set_page_config(page_title="LaymanLens", layout="centered")
st.title("🔍 LaymanLens")
st.subheader("Simplifying Complex Technical Sentences")

# User input
text = st.text_area("Enter a complex technical sentence:")

if st.button("Simplify"):
    if text.strip():
        with st.spinner("Simplifying..."):
            output = model(text)[0]["label"]
        st.success("✅ Simplified Output:")
        st.write(output)
    else:
        st.warning("Please enter a sentence to simplify.")
