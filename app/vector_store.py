from pathlib import Path
from langchain_community.vectorstores import FAISS
from app.config import VECTOR_DB_PATH

class VectorStoreManager:
    def __init__(self , embedding_model):
        self.embedding_model = embedding_model
    
    def create_vector_store(self , chunks):
        vector_store = FAISS.from_documents(
            documents = chunks,
            embedding = self.embedding_model
        )
        return vector_store
    
    def save_vector_store(self,vector_store):
        save_path =Path(VECTOR_DB_PATH)

        save_path.parent.mkdir(parents = True , exist_ok = True)

        vector_store.save_local(str(save_path))
        print(f"Vector stored and saved at {save_path}")
    
    def load_vector_store(self):
        return FAISS.load_local(
            str(VECTOR_DB_PATH),
            self.embedding_model,
            allow_dangerous_deserialization = True
        )

    
    def get_vector_store(self, chunks):

        index_file = Path(VECTOR_DB_PATH) / "index.faiss"
        if index_file.exists():
            print("📂 Loading existing vector database...")
            return self.load_vector_store()

        print("⚡ Creating vector database...")
        vector_store = self.create_vector_store(chunks)
        self.save_vector_store(vector_store)
        return vector_store
