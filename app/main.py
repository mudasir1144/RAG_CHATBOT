from app.chatbot import ChatBot

def main():
    chatbot =ChatBot()

    print("A simple RAG Based Chatbot")
    print("Type exit to quit")

    while True:
        question = input("Ask: ")

        if question.lower() == "exit":
            print("Good Byeee!")
            break
        answer = chatbot.ask(question)
        print(f"Bot Says : {answer}")

if __name__ == "__main__":
    main()