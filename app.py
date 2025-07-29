import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Title and description
st.set_page_config(page_title="LaymanLens", page_icon="⏳")
st.title("LaymanLens ⏳")
st.write("### Simplify complex technical text into layman's terms using AI.")

# Load model and tokenizer (no sentencepiece!)
@st.cache_resource
def load_model():
    model_name = "mrm8488/t5-base-finetuned-summarize-news"  # Light model for Streamlit
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return pipeline("summarization", model=model, tokenizer=tokenizer)

simplifier = load_model()

# User input
user_input = st.text_area("Enter complex technical sentence:")

# Simplify button
if st.button("Simplify"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Simplifying..."):
            result = simplifier(user_input[:1024])[0]['summary_text']
        st.success("Here's the simplified version:")
        st.write(f"🪄 **{result}**")
