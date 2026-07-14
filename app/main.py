from app.loader import DocumentLoader
from app.chunker import TextChunker

def main():
    loader = DocumentLoader('Data\documents\sample.pdf')
    documents = loader.load()

    chunker = TextChunker()
    chunks = chunker.split_documents(documents)

    print(f"Page Loaded: {len(documents)}")
    print(f"Chunk Created: {len(chunks)}")

    print("\nFirst Chunk")
    print(chunks[0].page_content)
    print("\nMetadata")
    print(chunks[0].metadata)

if __name__ == "__main__":
    main()