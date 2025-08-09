# LaymanLens

LaymanLens is a web application that uses **NLP (Natural Language Processing)** and **Transformers** to simplify complex academic and technical sentences into plain, easy-to-understand language.  
The app is built with **Python** and **Streamlit**, and uses Hugging Face’s transformer models for text simplification 

---

## Table of Contents
- [Overview](#overview)
- [Workflow](#workflow)
- [Features](#features)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Testing](#testing)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview
LaymanLens is an AI-powered text simplification tool that converts complex technical text into easy-to-understand language.  
It uses a pre-trained transformer model hosted on Hugging Face to ensure accurate, context-aware simplifications.  
This tool is built with **Streamlit** for the UI and can be deployed locally or online.

---

## Workflow
Follow these steps to configure, run, and maintain the project:

1. **Clone the repository**
    ```bash
    git clone https://github.com/Swethaa-02/LaymanLens.git
    cd LaymanLens
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**
    ```bash
    streamlit run app.py
    ```

4. **Access the application**
    - Local: `http://localhost:8501`
    - If using ngrok: use the forwarding link shown in your terminal.

---

## Features
- Converts complex sentences into simplified plain language.
- Uses transformer-based NLP models.
- Web interface via Streamlit.
- Hugging Face model integration.
- Supports both local and cloud deployment.

---

## Dataset
The project uses a pre-trained model from Hugging Face (`Swethaa02/laymanlens-v1`) trained on custom technical text and simplified text pairs.

---

## Model Architecture
- **Tokenizer:** AutoTokenizer from Hugging Face Transformers.
- **Model:** AutoModelForSeq2SeqLM for sequence-to-sequence simplification.
- **Framework:** PyTorch backend.

---

## Getting Started
Make sure you have **Python 3.8+** installed.  
Install all requirements using:
```bash
pip install -r requirements.txt

---

## Usage
1. Enter complex text in the input box.  
2. Click **"Simplify"**.  
3. View simplified output instantly.

Example:
```bash
Input: "The acceleration due to gravity on Earth is approximately 9.81 meters per second squared."
Output: "Gravity on Earth pulls things down at about 9.81 m/s²."
