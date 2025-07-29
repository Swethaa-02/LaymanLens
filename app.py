import streamlit as st
from transformers import pipeline

# ------------------- App Configuration -------------------
st.set_page_config(page_title="LaymanLens", page_icon="⏳", layout="centered")

# ------------------- App Header -------------------
st.markdown("<h1 style='text-align: center;'>LaymanLens ⏳</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Simplify Complex Technical Text Instantly</h4>", unsafe_allow_html=True)

# ------------------- Load Model -----------------
