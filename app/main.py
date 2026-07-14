from app.loader import DocumentLoader

def main():
    loader = DocumentLoader("Data\documents\sample.pdf")
    documents = loader.load()
    print(f"Total Pages: {len(documents)}\n")
    print("="*60)
    print(documents[0].page_content)
    print('='*60)
    print(documents[0].metadata)

if __name__ == "__main__":
    main()