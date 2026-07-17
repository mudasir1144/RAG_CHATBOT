from app.loader import DocumentLoader
from app.chunker import TextChunker
from app.embeddings import EmbeddingManager
from app.vector_store import VectorStoreManager

def main():
    loader = DocumentLoader('Data\documents\sample.pdf')
    documents = loader.load()

    chunker = TextChunker()
    chunks = chunker.split_documents(documents)

    embedding_manager = EmbeddingManager()
    embedding_model = embedding_manager.get_embedding_model()

    vector_manager = VectorStoreManager(embedding_model)
    vector_store = vector_manager.create_vector_store(chunks)
    vector_manager.save_vectore_store(vector_store)

    print("FAISS Database successfully created")
    
    print(f"indexed chunks :{len(chunks)}")


if __name__ == "__main__":
    main()