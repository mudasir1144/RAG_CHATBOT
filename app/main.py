from app.loader import DocumentLoader
from app.chunker import TextChunker
from app.embeddings import EmbeddingManager
from app.vector_store import VectorStoreManager
from app.retriever import Retriever
from app.prompt_builder import PromptBuilder
from app.llm import LLMManager

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
    
    prompt_builder = PromptBuilder()

    llm = LLMManager()

    print("Simple RAG based system")
    print("Type 'EXIT' to quit")

    while True:
        question = input("\nYou: ")
        if question.lower()=="exit":
            break
        retrieved_docs = retriever.retrieve(question)
        prompt = prompt_builder.build_prompt(
            question,
            retrieved_docs
        )
        answer = llm.generate_response(prompt)
        print(f"\nBot: {answer}")

    

if __name__ == "__main__":
    main()