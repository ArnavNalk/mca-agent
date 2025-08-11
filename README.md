# MCA Agentic AI — Semantic Search & Analytics for MCA Annual Reports (2007–2025)

## Overview
This project builds an **Agentic AI** system that can summarize, answer questions, and extract statistical insights from the **Ministry of Corporate Affairs (MCA) Annual Reports** spanning **2007–2025**.

MCA Annual Reports are rich in corporate governance, compliance, and policy data, but they exist only as long, static PDF documents.  
Our system transforms them into an **interactive, searchable knowledge base** powered by **Retrieval-Augmented Generation (RAG)** and **statistical analysis**.

---

## Key Features
- **Semantic Q&A:** Ask natural language questions and get precise answers from MCA reports.
- **Summarization:** Generate concise summaries of long sections.
- **Statistics Extraction:** Pull numeric data from tables and integrate into visualizations.
- **Trend Analysis:** Analyze multi-year patterns such as company registrations, LLP growth, and SFIO cases.
- **Deployable Prototype:** Lightweight Streamlit/FastAPI frontend for public access.

---

## Dataset
- **Source:** MCA Annual Reports (2007–2025) from the Ministry of Corporate Affairs, Government of India.
- **Format:** PDF files, ~200+ pages each.
- **Content Types:**
  - Policy updates
  - Company law enforcement
  - SFIO case summaries
  - LLP and sectoral registration data
  - Statistical tables and charts

---

## System Architecture
**1. Document Processing**
- PDF parsing with `PyMuPDF` / `pdfplumber`
- Text cleaning & chunking by section/topic
- Embedding generation with OpenAI/SentenceTransformers

**2. Retrieval Layer**
- Vector storage in `FAISS` / `Chroma`
- Semantic search to return relevant chunks

**3. Agent Layer**
- RAG pipeline using `LangChain` / `LlamaIndex`
- LLM for summarization and answering queries
- Optional statistical analysis & visualization

---

## Tech Stack
- **Languages:** Python 3.10+
- **Libraries:**
  - **PDF Parsing:** `PyMuPDF`, `pdfplumber`
  - **Embeddings:** `openai`, `sentence-transformers`
  - **Vector DB:** `faiss-cpu`, `chromadb`
  - **RAG Framework:** `langchain`, `llama-index`
  - **Visualization:** `matplotlib`, `seaborn`, `plotly`
  - **UI:** `streamlit`, `fastapi`

---

## Usage
1. Upload or select an MCA Annual Report (2007–2025)
2. Ask a question like:
   - `"Summarize MCA21 Phase 2 implementation"`
   - `"How many LLPs were registered in 2015?"`
3. View:
   - Text answers
   - Extracted statistics
   - Interactive charts

---

## Research Value
This project is **not** a generic PDF summarizer. It:
1. Uses **RAG** to provide accurate, context-specific answers.
2. Integrates **statistics** with NLP for hybrid analysis.
3. Focuses on a **unique domain-specific corpus** (MCA reports) that has not been explored in existing literature.
4. Produces a **deployable prototype** for law-tech and public policy applications.

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.


