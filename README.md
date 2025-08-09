# RAG Learning Project

This project demonstrates a Retrieval-Augmented Generation (RAG) system using ChromaDB and Google's Gemini Pro model. It allows you to ask questions about growing vegetables in Florida, and the system will retrieve relevant information from a PDF document and generate a response based on that context.

## Project Structure

- `chroma_db/`: This directory stores the ChromaDB persistent client data, which includes the vectorized embeddings of the PDF document.
- `data/`: This directory contains the PDF documents used as the knowledge base for the RAG system. Currently, it includes `VH021.pdf`.
- `rag-learning/`: This directory contains the Python virtual environment for the project.
