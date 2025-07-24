"""
LaymanLens: A Streamlit App to Simplify Academic Research Abstracts into Layman-Friendly Summaries

This app uses Hugging Face's `google/pegasus-xsum` model to convert complex academic research abstracts 
into simplified English summaries for general understanding.

Dependencies:
- streamlit
- transformers
- torch
- sentencepiece
"""

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Set Streamlit page configuration
st.set_page_config(page_title="LaymanLens", layout="centered")

# App Title
st.title("🔬 LaymanLens")
st.markdown("**Convert complex academic abstracts into simple, understandable summaries.**")

# Text input area
user_input = st.text_area("📄 Paste your academic abstract below:", height=200)

# Load model and tokenizer (cached)
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-xsum")
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    return summarizer

summarizer = load_model()

# Button to summarize
if st.button("🔁 Convert to Layman Summary"):
    if user_input.strip() == "":
        st.warning("Please paste an academic abstract first.")
    else:
        with st.spinner("Generating simplified summary..."):
            summary = summarizer(user_input, max_length=80, min_length=30, do_sample=False)[0]['summary_text']
            st.success("✅ Here's the layman summary:")
            st.markdown(f"**📝 Summary:**\n\n{summary}")

        # Optional Q&A Style
        with st.expander("💡 What does this mean? (Q&A Style Explanation)"):
            st.write("**Q: What is the main idea of this research?**")
            st.write(summary)
            st.write("**Q: Why is this important?**")
            st.write("This research might be complex, but the simplified summary helps non-experts understand the core message.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using [Hugging Face Transformers](https://huggingface.co/google/pegasus-xsum) and [Streamlit](https://streamlit.io)")
