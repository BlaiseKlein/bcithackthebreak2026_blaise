<<<<<<< HEAD
from src.openai_service import get_ai_bot_response
=======
from openai_service import get_ai_bot_response
>>>>>>> dev

def main():
    prompt = input("Ask about a command: ")
    response = get_ai_bot_response(prompt)
    print(response)

if __name__ == "__main__":
    main()