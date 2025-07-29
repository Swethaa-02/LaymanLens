import streamlit as st
from transformers import pipeline

# ------------------- App Configuration -------------------
st.set_page_config(page_title="LaymanLens", page_icon="⏳", layout="centered")

# ------------------- App Header -------------------
st.markdown("<h1 style='text-align: center;'>LaymanLens ⏳</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Simplify Complex Technical Text Instantly</h4>", unsafe_allow_html=True)

# ------------------- Load Model -------------------
@st.cache_resource(show_spinner=True)
def load_model():
    return pipeline("text2text-generation", model="Swethaa02/laymanlens-v1")

simplifier = load_model()

# ------------------- Input Box -------------------
st.markdown("### 📝 Enter Technical Text")
user_input = st.text_area("Paste your complex text below:", height=200, placeholder="e.g. The quantum entanglement in photonic systems enables secure communication channels...")

# ------------------- Simplify Button -------------------
if st.button("🔍 Simplify"):
    if not user_input.strip():
        st.warning("Please enter some text to simplify.")
    else:
        with st.spinner("⏳ Simplifying... please wait..."):
            try:
                output = simplifier(user_input, max_length=150, clean_up_tokenization_spaces=True)[0]['generated_text']
                st.success("✅ Simplified Text")
                st.markdown(f"```{output.strip()}```")
            except Exception as e:
                st.error(f"🚨 Error: {e}")

# ------------------- Footer -------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 12px;'>Made with ❤️ by Swethaa02 | Hugging Face Model: <code>Swethaa02/laymanlens-v1</code></p>",
    unsafe_allow_html=True
)
