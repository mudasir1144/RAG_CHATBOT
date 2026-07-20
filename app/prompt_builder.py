from langchain_core.documents import Document

class PromptBuilder:
    def build_prompt(self , question : str , documents=list[Document])->str:
        context = "\n".join(
            doc.page_content
            for doc in documents
        )
        prompt = f"""
You are a helpful AI Assistant,
Answer only using the provide context.
If the answer is not in context ,replay exactly: "I don't know on basis of provided documenent"
Context:{context}
Question:{question}
Answer:"""
        return prompt.strip()
