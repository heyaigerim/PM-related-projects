# **Retrieval-Augmented Generation (RAG) for AI-Powered Search**
## INFO 290: Applied Generative AI and LLMs
## UC Berkeley, 2025

## Project Overview - Product Management & AI Integration

## **Project Summary**
This project focuses on building an AI-driven knowledge retrieval system using Retrieval-Augmented Generation (RAG), an emerging technology in AI-powered search and automation. By leveraging machine learning embeddings and intelligent text chunking, this system improves information retrieval accuracy, making it highly applicable to AI-driven products, chatbots, and search platforms.

This project demonstrates product thinking by solving a real-world challenge: improving search relevance and AI-powered knowledge retrieval. The system takes unstructured text from multiple documents, processes it into semantic chunks, generates embeddings for retrieval, and enables context-aware search results.

## **Key Product Areas Demonstrated:**
1. AI & NLP Product Strategy – Understanding how AI models retrieve and process information.
2. User-Centric Information Retrieval – Optimizing chunking and embeddings for better search experience.
3. Technical Feasibility & Model Performance – Ensuring embeddings and retrieval efficiency at scale.
4. Iterative Improvements – Refining retrieval accuracy through testing and adjustments.

## 📌 **Milestone 1: Data Processing & Chunking**

### **Objective**
Enable AI-powered retrieval by processing and structuring text data for machine learning models.

### **Problem Statement**
Most search engines and chatbots struggle with retrieving relevant, contextually accurate information from large text corpora. Poorly structured text leads to fragmented search results, reducing user experience and efficiency.

### **Solution Implemented**
1. Text Preprocessing & Cleaning
- Extracted and processed five AI-related documents into structured text.
- Removed noise, redundant spaces, and ensured high-quality input data.
- Intelligent Text Chunking
2. Fixed-size chunking: Ensured manageable 500-character segments without breaking sentences.
3. Semantic chunking: Grouped logically related paragraphs using NLP similarity techniques.
Output for AI Retrieval
4. Stored structured text chunks in a Pickle file (chunks.pkl), ensuring efficient retrieval.

## **Product Thinking & Challenges**
1. Scalability: How can AI handle large-scale unstructured data for search?
2. Usability: Does chunking preserve enough context for meaningful retrieval?
3. Iteration & Testing: Adjusted chunk sizes and models to optimize for accuracy.

## 📌 **Milestone 2: AI-Powered Retrieval & Embeddings**
### **Objective**
Transform structured text into AI-searchable knowledge using vector embeddings.

### **Problem Statement**
Keyword-based search engines fail to understand context, leading to irrelevant or incomplete results. To improve retrieval quality, machine learning embeddings must replace traditional keyword matching.

### **Solution Implemented**
1. Embedding Generation
- Used sentence-transformers (all-MiniLM-L6-v2) to convert text chunks into numerical embeddings.
- Stored embeddings efficiently for scalable AI-based search.
2. Vector Database Creation
- Stored embeddings in a Python dictionary where embeddings act as keys for chunk retrieval.
- Ensured efficient hashable storage for quick access.
3. Cosine Similarity-Based Search
- Implemented semantic search retrieval using cosine similarity.
- Users can input queries, and the system returns the most relevant text using vector comparisons.
4. Optimizations & Refinements
- Increased chunk size and applied semantic filtering for better query accuracy.
- Set a minimum similarity threshold (0.6) to eliminate weak matches.

## **Product Thinking & Challenges**
1. Relevance & Ranking: How do we prioritize the most useful results for users?
2. Performance Optimization: Reducing search latency with efficient embedding storage.
3. Iterative Testing: Refining similarity scoring & chunking strategy based on query performance.

## **Final Deliverables**
📄 Structured text chunks stored in **chunks.pkl**
📄 Vector embeddings stored in **vector_db.pkl**
📄 Fully functional AI-powered retrieval in **Milestone 1.ipynb** and **Milestone 2.ipynb**


## 🎯 **Product Insights & Takeaways**
1. AI-powered Search Improves Information Retrieval
- Traditional keyword-based search systems are limited in contextual understanding. By implementing machine learning embeddings, AI can interpret meaning, improving search accuracy and user experience.

2. Chunking Strategy Affects Performance
- Fine-tuning how text is structured and retrieved impacts search relevance.
- Smaller chunks lose context but improve precision.
- Larger chunks retain meaning but may introduce irrelevant information.

3. Machine Learning for Product Innovation
- This project applies AI & NLP techniques to create scalable, efficient search solutions, relevant for:
- ✔ AI-powered customer support bots
- ✔ Intelligent document retrieval systems
- ✔ Enterprise knowledge management tools

