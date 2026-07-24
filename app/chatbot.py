from app.knowledge_base import KnowledgeBase
from app.retriever import Retriever
from app.prompt_builder import PromptBuilder
from app.llm import LLMManager

class ChatBot:
    def __init__(self):
        print(f"Chatbot Initialized")

        knowledge_base = KnowledgeBase(
            "data/documents/sample.pdf"
        )

        vector_store = knowledge_base.get_vector_store()
    
        self.retriever = Retriever(vector_store)
    
        self.prompt_builder = PromptBuilder()

        self.llm = LLMManager()

        print("Chat bot Ready!")
        
    def ask(self , question):
        docs = self.retriever.retrieve(question)
        prompt = self.prompt_builder.build_prompt(question , docs)
        answer = self.llm.generate_response(prompt)
        return answer
    
