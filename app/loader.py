from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

class DocumentLoader:

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self):
       
        if not self.file_path.exists():
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        loader = PyPDFLoader(str(self.file_path))

        documents = loader.load()

        return documents