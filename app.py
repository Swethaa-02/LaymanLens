import streamlit as st
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

st.set_page_config(page_title="LaymenLens", page_icon="⏳", layout="centered")

# Title & Description
st.markdown("<h1 style='text-align: center;'>⏳ LaymenLens</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 18px;'>Breaking down complex research into simple English.</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Load model and tokenizer
@st.cache_resource
def load_model():
    model_name = "Swethaa02/laymanlens-v1"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return pipeline("text2text-generation", model=model, tokenizer=tokenizer)

simplifier = load_model()

# Text Input
st.markdown("### ✍️ Paste your research sentence below:")
input_text = st.text_area(" ", height=200, placeholder="E.g. The convolutional neural network uses backpropagation to update weights...")

# Simplify Button
if st.button("Simplify"):
    if input_text.strip() == "":
        st.warning("Please enter some text to simplify.")
    else:
        with st.spinner("Simplifying..."):
            result = simplifier(input_text, max_length=256, do_sample=False)[0]["generated_text"]
        st.success("✅ Simplified Text:")
        st.markdown(f"**{result}**")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Made with ❤️ by <strong>Team LaymenLens</strong></p>",
    unsafe_allow_html=True
)
