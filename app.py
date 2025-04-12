import os
import streamlit as st
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Use OpenAI-compatible ChatOpenAI with OpenRouter endpoint
llm = ChatOpenAI(
    openai_api_key=openrouter_api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="mistralai/mixtral-8x7b",
    temperature=0.3,
)

# Load or create FAISS index
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
if not os.path.exists("embeddings/faiss_index"):
    loader = TextLoader("data/admissions.txt")
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    vectorstore = FAISS.from_documents(chunks, embedding=embedding_model)
    vectorstore.save_local("embeddings/faiss_index")
else:
    vectorstore = FAISS.load_local("embeddings/faiss_index", embedding_model, allow_dangerous_deserialization=True)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# QA chain
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

# UI
st.set_page_config(page_title="🤖 JSOM Chatbot – Ask Me Anything")
st.title("🤖 JSOM Chatbot – Ask Me Anything")
query = st.text_input("What would you like to know about JSOM?")

if query:
    with st.spinner("Thinking..."):
        result = qa.invoke(query)
        st.markdown(f"**Answer:** {result['result']}")
        with st.expander("📄 Context Chunks Used"):
            for i, doc in enumerate(result["source_documents"]):
                st.markdown(f"**Chunk {i+1}:** {doc.page_content.strip()}")
