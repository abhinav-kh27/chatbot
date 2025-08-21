# app.py

from interface import Chatbot

def main():
    bot = Chatbot()
    print("Chatbot is ready! (type /exit to quit)\n")

    while True:
        user_input = input("User: ")
        response, should_exit = bot.respond(user_input)
        print(f"Bot: {response}")
        if should_exit:
            break

if __name__ == "__main__":
    main()
