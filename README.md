<<<<<<< HEAD
# 🤖 JSOM Chatbot – Ask Me Anything

A local AI-powered chatbot designed to answer questions about the Naveen Jindal School of Management (JSOM) at The University of Texas at Dallas. Built using LangChain, FAISS, Streamlit, and Mistral (via Ollama).

---

## 🚀 Features

- 🔍 Vector search using FAISS
- 📄 Local embeddings via HuggingFace transformers
- 💬 Natural language QA with Mistral LLM via Ollama
- 🌐 Streamlit-powered web app
- 🧠 Context-aware document querying

---

## 📁 Project Structure

jsom_chatbot/
│
├── app.py                  # Streamlit frontend
├── scripts/
│   └── build_vectorstore.py  # Script to embed docs + build FAISS index
├── data/
│   └── admissions.txt       # Raw scraped JSOM content
├── embeddings/
│   └── faiss_index          # Vector store (auto-generated)
├── .env                    # Your environment variables (e.g., API keys)
└── requirements.txt        # Dependencies

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/ashleshakadam/utd-jsom-chatbot.git
cd jsom-chatbot

2. Create & Activate a Virtual Environment

python3 -m venv venv
source venv/bin/activate

3. Install Requirements

pip install -r requirements.txt

4. Setup Ollama (Mistral)

Install Ollama:

brew install ollama
ollama serve

Then pull the model:

ollama run mistral

5. Build the Vectorstore

python scripts/build_vectorstore.py

6. Run the Chatbot

streamlit run app.py

Then visit 👉 http://localhost:8501

⸻

⚙️ Environment Variables

Create a .env file in your project root with the following:

# Not needed with Ollama but helpful for optional OpenAI fallback
OPENAI_API_KEY=sk-xxxxx...



⸻

📚 Acknowledgments
	•	LangChain
	•	FAISS
	•	Sentence Transformers
	•	Ollama
	•	Streamlit

⸻

💬 Questions or Contributions?

Feel free to open an issue or submit a PR. Let’s make academic info more accessible!

⸻

🧠 Author

Built with ❤️ by Ashlesha Kadam

---
=======
# Trial_bot
>>>>>>> b928c05b6d8293b6baad04b439caf5d2f8f2b12d
