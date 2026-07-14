from app.llm import LLMManager

def main():
    llm = LLMManager()

    question  = "What is Machine learning?"
    answer = llm.generate_response(question)

    print(f"Question : {question}")
    print(f"Answer: {answer}")

if __name__ =="__main__":
    main()