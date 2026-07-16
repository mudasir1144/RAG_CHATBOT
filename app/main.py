from app.loader import DocumentLoader
from app.chunker import TextChunker
from app.embeddings import EmbeddingManager

def main():
    loader = DocumentLoader('Data\documents\sample.pdf')
    documents = loader.load()

    chunker = TextChunker()
    chunks = chunker.split_documents(documents)

    embedding_manager = EmbeddingManager()
    embedding_model = embedding_manager.get_embedding_model()
    vector = embedding_model.embed_query(
        chunks[0].page_content  
    )

    print(f"Page Loaded: {len(documents)}")
    print(f"Chunk Created: {len(chunks)}")

    print(f"Embedding Dimensions are: {len(vector)}")


    print("\nFirst Chunk")
    print(chunks[0].page_content)
    print("\nMetadata")
    print(chunks[0].metadata)
    print(vector[:10])

if __name__ == "__main__":
    main()