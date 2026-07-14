from ollama import chat
from app.config import Model_name

class LLMManager:
    def __init__(self , model_name : str=Model_name):
        self.model_name = model_name
    def generate_response(self , prompt:str)->str:
        response = chat(
            model = self.model_name,
            messages = [{
                "role" : "user",
                "content" : prompt,
            }] ,
        )
        return response.message.content