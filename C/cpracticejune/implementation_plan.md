# Implementation Plan - Beginner-Friendly RAG Chatbot

We will build a complete Retrieval-Augmented Generation (RAG) chatbot from scratch, focusing on teaching the core concepts along the way. We will avoid complex libraries like LangChain or LlamaIndex to keep the pipeline manual and clear.

## Proposed Project Structure

We will create the following files and directories in the workspace `c:\Users\sahil\RAG-chatbot`:

```text
c:\Users\sahil\RAG-chatbot/
├── frontend/
│      index.html        - Modern dark design chat and upload UI
│      style.css         - Premium visual styling and micro-animations
│      script.js         - Frontend chat/upload API client logic
│
├── backend/
│      main.py           - FastAPI server and routes
│      config.py         - Configuration (environment variables loading)
│
│      services/
│          pdf_loader.py - Extracts text from PDFs using pypdf
│          chunker.py    - Splitting text into overlapping chunks
│          embeddings.py - Generates embeddings using sentence-transformers (all-MiniLM-L6-v2)
│          vectordb.py   - Interacts with ChromaDB
│          retriever.py  - Selects relevant chunks for a query
│          llm.py        - Interface for Groq API or Local LLM (Ollama)
│          rag.py        - Coordinates the full RAG pipeline
│
│      uploads/          - Temp folder for uploaded PDFs
│      database/         - ChromaDB persistent storage directory
│      prompts/          - Prompt templates
│      utils/            - Helper utilities
│
├── requirements.txt     - Project dependencies list
├── .env.example         - Environment variable templates
├── .gitignore           - Git ignore rules
└── README.md            - Project documentation and explanation
```

---

## Technical Approach & Explanations

### Concept: What is RAG?
Retrieval-Augmented Generation (RAG) is a technique that extends the capability of an LLM by pulling in relevant information from a custom knowledge base (like a PDF) and feeding it as context along with the user's prompt. 
Instead of fine-tuning the LLM, we search for the specific text parts that answer the query and prepend them to the prompt.

### Concept: Embeddings & Vector Databases
- **Embeddings**: An embedding is a vector (list of numbers) representing the semantic meaning of a piece of text. Texts with similar meanings will have vectors that point in similar directions in a high-dimensional space.
- **Vector Database**: A database designed to store vector embeddings and perform fast similarity searches (e.g., finding the top 3 text chunks whose embeddings are closest to the query's embedding using cosine similarity).

---

## 12-Phase Implementation Plan

### Phase 1: Workspace & Dependencies
1. Create directories: `frontend`, `backend`, `backend/services`, `backend/uploads`, `backend/database`, `backend/prompts`, `backend/utils`.
2. Write `.gitignore` and `.env.example`.
3. Create `requirements.txt` with:
   - `fastapi`
   - `uvicorn`
   - `python-multipart` (for file uploads)
   - `python-dotenv`
   - `pypdf`
   - `sentence-transformers`
   - `chromadb`
   - `requests` (for local LLM API communication)
   - `groq` (Groq official client)
4. Teach the user about each dependency in `requirements.txt`.

### Phase 2: Frontend Design (UI Only)
1. Build `frontend/index.html` with a modern dark theme, sidebar/panel for PDF uploads, chat log area with auto-scroll, and message inputs.
2. Build `frontend/style.css` using sleek dark mode colors, responsive layout, CSS variables, transitions, and loading states.
3. Build `frontend/script.js` with placeholders for the API requests, updating the UI dynamically for message bubbles and file uploading states.

### Phase 3: FastAPI Backend Setup ("Hello World")
1. Initialize `backend/main.py` with FastAPI.
2. Add a `GET /` route for a health check.
3. Verify that the backend runs locally on port 8000 using `uvicorn`.

### Phase 4: Connect Frontend and Backend
1. Update `backend/main.py` to allow CORS (Cross-Origin Resource Sharing) for the local frontend.
2. Add a dummy `POST /chat` route that accepts a user question and returns a mock chatbot answer.
3. Implement `script.js` to call the `/chat` route when the send button is pressed, and render the returned mock response.

### Phase 5: PDF Upload
1. Implement `POST /upload` in `backend/main.py` using `UploadFile` from FastAPI.
2. Store the uploaded file in `backend/uploads/`.
3. Connect the frontend upload button to POST to `/upload` and display the status (success/error).

### Phase 6: PDF Reading & Text Extraction
1. Create `backend/services/pdf_loader.py`. Use `pypdf.PdfReader` to extract text.
2. Log/print the extracted text to show how it looks.
3. Explain to the user how PDF structures store text and how `pypdf` extracts it.

### Phase 7: Text Chunking
1. Create `backend/services/chunker.py`.
2. Implement a simple chunking utility (e.g., character-based or word-based with sliding window/overlap).
3. Explain why chunking is required (LLM context limits, cost, and keeping retriever focus sharp), and details of chunk size vs overlap.

### Phase 8: Generating Embeddings
1. Create `backend/services/embeddings.py`.
2. Load the `sentence-transformers/all-MiniLM-L6-v2` model.
3. Define functions to encode text into embeddings.
4. Explain what embeddings represent, what the dimensions mean, and why semantic search is powerful.

### Phase 9: ChromaDB Vector Storage
1. Create `backend/services/vectordb.py`.
2. Initialize a persistent ChromaDB client inside `backend/database/`.
3. Add helper methods to create/get a collection, upsert chunk texts + metadata + embeddings.
4. Explain collections, IDs, metadata, and persistent vector databases.

### Phase 10: Retrieval & Cosine Similarity
1. Create `backend/services/retriever.py`.
2. Implement querying of the vector database for the top $K$ matching documents.
3. Expose a temporary API route `POST /retrieve` or print logs to inspect retrieved text snippets.
4. Explain cosine similarity and distance metrics.

### Phase 11: LLM Service & Configuration
1. Create `backend/config.py` to read provider selection (`groq` vs `local`) and API keys from `.env`.
2. Create `backend/services/llm.py`. Implement functions to send prompt context + question to Groq or local Ollama API.
3. Keep logic clean and modular to switch based on environment variables.

### Phase 12: Complete RAG Pipeline Orchestration
1. Create `backend/services/rag.py` to bind PDF processing (Extract $\rightarrow$ Chunk $\rightarrow$ Embed $\rightarrow$ Store) and query processing (Embed Question $\rightarrow$ Retrieve Context $\rightarrow$ Format Prompt $\rightarrow$ Query LLM).
2. Wire up the backend APIs to run these services.
3. Test the chatbot end-to-end and document the project in `README.md`.

---

## Verification Plan

### Automated/Local Tests
- Run `uvicorn backend.main:app --reload` to start the server.
- Test endpoint health check via browser (`http://localhost:8000/`).
- Test backend functions using simple test scripts or inline python calls.

### Manual Verification
- Upload test PDFs (e.g., short articles, resume, documentation).
- Chat with the bot and verify that the retrieved context is used in the answers.
- Inspect ChromaDB database folders to ensure persistence.
