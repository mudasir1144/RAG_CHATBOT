from app.loader import DocumentLoader
from app.chunker import TextChunker
from app.embeddings import EmbeddingManager
from app.vector_store import VectorStoreManager
from app.retriever import Retriever

def main():
    loader = DocumentLoader('Data\documents\sample.pdf')
    documents = loader.load()

    chunker = TextChunker()
    chunks = chunker.split_documents(documents)

    embedding_manager = EmbeddingManager()
    embedding_model = embedding_manager.get_embedding_model()

    vector_manager = VectorStoreManager(embedding_model)
    vector_store = vector_manager.create_vector_store(chunks)
    
    retriever = Retriever(vector_store)
    query = input("What is your question?")
    result = retriever.retrieve(query)

    print("Retrived chunnks")
    print("="*70)
    for i,doc in enumerate(result ,start=1):
        print("\nChunks {i}")
        print(doc.page_content)
        print()
        print(doc.metadata)
        print("-" * 70)


    

if __name__ == "__main__":
    main()