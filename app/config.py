from pathlib import Path
Model_name = 'llama3.2:3b'

EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

VECTOR_DB_PATH = Path("data/vector_db/faiss_index")