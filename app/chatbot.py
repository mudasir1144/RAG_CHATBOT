from app.loader import DocumentLoader
from app.chunker import TextChunker
from app.embeddings import EmbeddingManager
from app.vector_store import VectorStoreManager
from app.retriever import Retriever
from app.prompt_builder import PromptBuilder
from app.llm import LLMManager

class ChatBot:
    def __init__(self):
        print(f"Chatbot Initialized")

        loader = DocumentLoader('Data\documents\sample.pdf')
        documents = loader.load()

        chunker = TextChunker()
        chunks = chunker.split_documents(documents)

        embedding_manager = EmbeddingManager()
        embedding_model = embedding_manager.get_embedding_model()

        vector_manager = VectorStoreManager(embedding_model)
        vector_store = vector_manager.get_vector_store(chunks)
    
        self.retriever = Retriever(vector_store)
    
        self.prompt_builder = PromptBuilder()

        self.llm = LLMManager()

        print("Chat bot Ready!")
        
    def ask(self , question:str)->str:
        retrieved_docs = self.retriever.retrieve(question)
        prompt = self.prompt_builder.build_prompt(
            question,
            retrieved_docs
        )
        answer = self.llm.generate_response(prompt)
        return answer
    
