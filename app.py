import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# App title and emoji
st.set_page_config(page_title="LaymanLens", page_icon="⌛")  # Hourglass emoji used as favicon

st.markdown("""
    <h1 style='text-align: center;'>🔍 LaymanLens</h1>
    <h4 style='text-align: center;'>✍️ Simplifying complex technical sentences into layman terms</h4>
    <br>
""", unsafe_allow_html=True)

# Load model & tokenizer
@st.cache_resource(show_spinner="Loading the model...")
def load_model():
    model_name = "Swethaa02/laymanlens-v1"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# Input
user_input = st.text_area("Paste any technical sentence below to simplify:", height=150)

# Simplify function
if user_input:
    with st.spinner("Simplifying..."):
        input_ids = tokenizer.encode("simplify: " + user_input, return_tensors="pt")
        output_ids = model.generate(input_ids, max_length=256, num_beams=4, early_stopping=True)
        simplified_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        # Output
        st.markdown("""
            <h4 style='margin-top: 30px;'>✅ <u>Simplified Output</u>:</h4>
        """, unsafe_allow_html=True)
        st.success(simplified_text)

# Footer
st.markdown("""
    <br><hr>
    <center>⌛ <i>LaymanLens by Swethaa02</i> ✍️</center>
""", unsafe_allow_html=True)
