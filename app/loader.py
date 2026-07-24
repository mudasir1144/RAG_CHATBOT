from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

class DocumentLoader:

    def __init__(self, file_path=None):
        self.file_path = file_path

    def load(self):
        loader = PyPDFLoader(self.file_path)
        return loader.load()

    def load_directory(self, folder_path):
        documents = []

        pdf_files = sorted(Path(folder_path).glob("*.pdf"))

        print(f"📚 Found {len(pdf_files)} PDF(s).")

        for pdf in pdf_files:
            print(f"Loading: {pdf.name}")

            loader = PyPDFLoader(str(pdf))
            documents.extend(loader.load())

        return documents