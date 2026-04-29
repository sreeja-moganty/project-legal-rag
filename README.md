# Agentic RAG System for Legal Case Analysis

##  Problem

Legal research involves analyzing large volumes of case documents and judgments.  
Traditional keyword-based search systems fail to capture semantic meaning and require users to manually sift through documents, making the process time-consuming and inefficient.

---

##  Solution

We built a **Retrieval-Augmented Generation (RAG) system** that:

- Uses **semantic search (FAISS + embeddings)** to retrieve relevant documents  
- Uses **Large Language Models (LLMs)** to generate explainable answers  
- Provides **context-aware and reasoning-based outputs**  

This system allows users to input natural language queries and receive structured, meaningful responses.

---

##  Tech Stack

- Python  
- Sentence Transformers  
- FAISS (Vector Search)  
- OpenAI API  

---

##  Project Structure
project-legal-rag/
│
├── README.md
├── requirements.txt
├── Domain Note.pdf
│
├── src/
│ ├── download_data.py
│ ├── retriever.py
│ ├── rag_pipeline.py
│
├── data/
├── notebooks/
├── results/


---

## How to Run

### 1. Install dependencies
pip3 install -r requirements.txt
---

### 2. Download and prepare dataset


python3 src/download_data.py


---

### 3. Run retrieval system


python3 src/retriever.py


---

### 4. Run full RAG pipeline


python3 src/rag_pipeline.py


---

## 📥 Dataset

The dataset is not uploaded to the repository due to size limitations.

To generate the dataset locally, run:


python3 src/download_data.py


---

##  Key Highlight

This project demonstrates an **end-to-end GenAI pipeline** combining retrieval and LLM-based reasoning to generate explainable outputs.

---

## Future Work

- Integrate real Indian legal datasets  
- Improve retrieval accuracy  
- Add agent-based reasoning architecture  
