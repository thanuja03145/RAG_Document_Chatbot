# 📚 RAG Document Chatbot (Gemini + FAISS)

A Retrieval-Augmented Generation (RAG) chatbot that lets you upload PDF documents and ask questions about them in plain English. The chatbot answers **only** using information found inside your uploaded PDFs, and clearly says so when it can't find an answer, instead of making things up.

Built as an AI Internship Week 4 assignment project.

---

## 📖 Project Overview

This project is a browser-based chatbot built with **Streamlit**. You upload one or more PDF files, the app reads them, breaks the text into small chunks, converts those chunks into embeddings, and stores them in a **FAISS** vector database. When you ask a question, the app finds the most relevant chunks from your PDFs and sends them to **Google's Gemini API** (`gemini-1.5-flash` / `gemini-2.0-flash`) to generate an accurate, grounded answer — along with the exact PDF file and page number the answer came from.

---

## ✨ Features

* 📥 **Upload one or multiple PDF files at once**
* 📄 **Automatic text extraction**, page by page
* ✂️ **Smart text chunking** using LangChain's `RecursiveCharacterTextSplitter`
* 🧠 **Embeddings generation** using HuggingFace `sentence-transformers` / Google Gemini Embeddings
* 🔍 **Fast similarity search** using FAISS
* 🤖 **Answer generation** using Google Gemini API (`gemini-1.5-flash` / `gemini-2.0-flash`)
* 📌 **Shows which PDF and page number** each answer came from
* 💬 **Chat history maintained** during the session
* ♾️ **Ask unlimited questions** until you close the browser
* 🧹 **Clear Chat button**
* 🔄 **Process PDFs / Rebuild Database button** (after uploading new PDFs)
* ⏳ **Loading spinners** while processing
* ✅ **Success messages** after indexing
* ⚠️ **Friendly error messages** for invalid files, empty PDFs, missing API keys, network issues, and API quota errors
* 🚫 **No hallucination** — replies with *"I could not find this information in the uploaded document."* when the answer isn't in the PDFs

---

## 🛠️ Technologies Used

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **Frontend** | Streamlit |
| **LLM** | Google Gemini API (`gemini-1.5-flash` / `gemini-2.0-flash`) |
| **Orchestration** | LangChain |
| **Embeddings** | HuggingFace `sentence-transformers` (`all-MiniLM-L6-v2`) / Gemini Embeddings |
| **Vector Database** | FAISS |
| **PDF Reading** | PyPDF / PyPDF2 |
| **Environment Config** | `python-dotenv` |

---

## 📁 Folder Structure

```text
RAG_Document_Chatbot/
│
├── app.py # Main Streamlit UI application
├── pdf_loader.py # Reads and extracts text from PDFs page by page
├── text_splitter.py # Splits text into manageable semantic chunks
├── embeddings.py # Loads embedding models
├── vector_store.py # Builds and queries FAISS vector database
├── rag_chatbot.py # RAG pipeline implementation using Gemini
├── utils.py # Helper functions & API key handling
├── requirements.txt # Python package dependencies
├── README.md # Project documentation
├── .gitignore # Git ignore rules
├── .env.example # Environment variables template
├── assets/ # Branding assets & images
├── sample_pdfs/ # Sample PDF files for testing
└── screenshots/ # Application screenshots

⚙️ Installation
1. Clone or extract the project
git clone [https://github.com/RakhiPB/RAG_Document_Chatbot.git](https://github.com/RakhiPB/RAG_Document_Chatbot.git)
cd RAG_Document_Chatbot

2. Create a virtual environment
python -m venv venv

Activate it:
 * Windows:
   venv\Scripts\activate

 * macOS / Linux:
   source venv/bin/activate

3. Install requirements
pip install -r requirements.txt

🔑 Environment Variables
 * Copy .env.example to a new file named .env:
   cp .env.example .env

 * Open .env and add your Google Gemini API key:
   GOOGLE_API_KEY=your_actual_gemini_api_key_here

   You can get a free Gemini API key from Google AI Studio.
▶️ How to Run
Once dependencies are installed and your .env file is set up, run:
streamlit run app.py

The app will automatically open in your default browser at http://localhost:8501.
Usage steps:
 * Upload one or more PDF files using the sidebar.
 * Click Process PDFs / Build Database and wait for the success message.
 * Type your question in the chat box at the bottom of the page.
 * View the answer along with the source PDF and page number.
 * Use Clear Chat to reset the conversation, or Process PDFs after uploading new documents.
---

📋 Requirements
 * Python 3.10 or higher
 * A valid Google Gemini API key
 * Internet connection (for downloading embedding models and calling the Gemini API)
---

❓ Sample Questions
Once you've built the database, try asking:
 * "What is the main topic of the document?"
 * "Summarize the uploaded document."
 * "What are the candidate's core technical skills and tools?"
 * "Explain the key projects mentioned in the PDF."
 * "What are the main conclusions or findings?"
---

🖼️ Screenshots
Add your application screenshots to the screenshots/ folder and reference them here:
screenshots/
├── upload_page.png
├── chat_interface.png
└── source_display.png
---

🚀 Future Improvements
 * Support for other document formats (.docx, .txt, .pptx)
 * Persistent chat history across sessions (saved to a database)
 * Multi-user support with separate document collections
 * Highlighting the exact text passage used to generate the answer
 * Option to choose between multiple Gemini models from the UI
 * Downloadable chat transcript
 * Dark mode UI toggle
---

📌 Notes
 * The FAISS index is saved locally in a faiss_index/ folder so you don't need to rebuild it every time you restart the app (as long as you don't delete that folder).
 * This project is intended for educational purposes as part of an AI internship assignment.

---



