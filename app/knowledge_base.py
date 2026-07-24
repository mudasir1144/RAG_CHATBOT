from app.loader import DocumentLoader
from app.chunker import TextChunker
from app.embeddings import EmbeddingManager
from app.vector_store import VectorStoreManager

class KnowledgeBase:
    def __init__(self , pdf_path:str):
        self.pdf_path  =pdf_path

        self.embedding_manager = EmbeddingManager()
        self.embedding_model = (self.embedding_manager.get_embedding_model())

        self.vector_manager = VectorStoreManager(
            self.embedding_model
        )
    def get_vector_store(self):
        loader = DocumentLoader()
        documents = loader.load_directory("Data/documents")

        chunker = TextChunker()
        chunks= chunker.split_documents(documents)

        vector_store = self.vector_manager.get_vector_store(chunks)
        return vector_store