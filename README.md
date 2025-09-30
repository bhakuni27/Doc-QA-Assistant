# 📄 Document Question Answering Assistant

This repository contains an example **PDF-based Question Answering assistant** that demonstrates how to combine **Large Language Models (LLMs)** with **retrieval techniques** to build grounded, reliable applications.

Instead of relying on a pre-trained model’s general knowledge, this assistant is designed to work **only with the content of the document you provide**. You upload a PDF, ask questions, and the system retrieves the most relevant parts of the text before generating an answer. If the assistant cannot find a meaningful answer in the document, it will not try to *hallucinate*. Instead, it responds with:

*"I don’t know based on this document."* 

This makes the project a simple but powerful example of **Retrieval-Augmented Generation (RAG)**, a widely used approach in modern LLM applications. It highlights how AI can be grounded in external data sources, ensuring **accuracy**, **transparency**, and **domain-specific answers**.

> **NOTE**: This project runs fully locally and does **not require any API keys**.


