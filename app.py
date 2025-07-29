import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

st.set_page_config(
    page_title="LaymanLens",
    page_icon="🔍",
    layout="centered"
)

st.markdown("<h1 style='text-align: center;'>🔍 LaymanLens</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Simplify complex text into plain English</p>", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model_name = "knkarthick/MEETING_SUMMARY"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return pipeline("summarization", model=model, tokenizer=tokenizer)

simplifier = load_model()

user_input = st.text_area("✍️ Paste your technical or complex text below:")

if st.button("Simplify"):
    if user_input.strip() == "":
        st.warning("Please enter some text to simplify.")
    else:
        with st.spinner("Simplifying..."):
            result = simplifier(user_input, max_length=100, min_length=30, do_sample=False)
            st.success("Here's the simplified version:")
            st.write(result[0]['summary_text'])

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 0.8em;'>Made with ❤️ by LaymanLens Team</p>", unsafe_allow_html=True)
