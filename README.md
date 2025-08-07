📘 LaymanLens - Research Simplified with AI
LaymanLens is an AI-powered web application that simplifies complex academic or technical text into easy-to-understand layman language using state-of-the-art transformer models. It's designed to help students, researchers, and curious learners grasp complicated content effortlessly.

🔍 Table of Contents
📘 Project Overview

💡 Features

📷 Demo Screenshot / Video

🛠 Tech Stack

🧠 How It Works

📦 Installation

🚀 Running the App Locally

🌍 Deployment Options

📂 Project Structure

❓ FAQs

🤝 Contributions

📄 License

📘 Project Overview
LaymanLens was built with the vision to break the barrier between complex academic knowledge and general understanding. With the help of Natural Language Processing (NLP) and the PEGASUS transformer model, users can paste any research abstract or technical description and instantly get a simpler version.



💡 Features

📷 Demo Screenshot / Video

🛠 Tech Stack

🧠 How It Works

📦 Installation

🚀 Running the App Locally

🌍 Deployment Options

📂 Project Structure

❓ FAQs

🤝 Contributions

📄 License


📘 Project Overview

💡 Features
✅ Summarizes and simplifies technical text

✅ Powered by the Hugging Face transformers library

✅ Easy-to-use interface built with Streamlit

✅ Responsive and minimal UI

✅ Hosted via Hugging Face Spaces / ngrok / Replit

🛠 Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	Python
NLP Model	PEGASUS (from Hugging Face)
Hosting	Hugging Face Spaces / Replit / ngrok
Source Code	GitHub

🧠 How It Works
User inputs a technical sentence or academic abstract.

The AutoTokenizer and AutoModelForSeq2SeqLM from Hugging Face load the PEGASUS model.

The model generates a simplified version of the input.

Output is displayed instantly in a user-friendly interface.

📦 Installation
Make sure Python 3.10+ is installed.

Step 1: Clone the repo
git clone https://github.com/Swethaa-02/LaymanLens.git
cd LaymanLens
Step 2: Install dependencies
pip install -r requirements.txt

🚀 Running the App Locally
streamlit run app.py
Then open http://localhost:8501 in your browser.

🌍 Deployment Options
📌 Option 1: Hugging Face Spaces
Fork this repo and go to https://huggingface.co/spaces

Click New Space

Choose Streamlit, link your GitHub, and select this repo

Done!

📌 Option 2: Replit
Create a new Replit project (Python)

Upload all files (app.py, requirements.txt)

Add a replit.nix if needed for Streamlit

Set the run command to:
streamlit run app.py --server.port=3000 --server.address=0.0.0.0

📂 Project Structure
LaymanLens/
│
├── app.py                 # Streamlit app logic
├── requirements.txt       # All Python dependencies
├── index.html             # (optional) Homepage template
└── README.md              # Project documentation

❓ FAQs
Q1. Why does my app not load on Hugging Face?
Make sure your app.py is in root, and requirements.txt has transformers, torch, and streamlit.

Q2. Which model are you using?
google/pegasus-xsum from Hugging Face.

Q3. Does it work offline?
No, the model loads from Hugging Face and requires internet.



🤝 Contributions
Contributions are welcome!

Fork the repo

Create a branch

Push your changes

Submit a PR



📄 License
MIT License
Feel free to use, modify, and share.


