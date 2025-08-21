# interface.py

import random
from model_loader import load_knowledge
from chat_memory import ChatMemory

class Chatbot:
    def __init__(self):
        self.knowledge_base = load_knowledge()
        self.memory = ChatMemory()

    def respond(self, user_input):
        user_input = user_input.lower().strip()

        if user_input == "/exit":
            return "Exiting chatbot. Goodbye!", True

        # Capital question
        if "capital of" in user_input:
            country = user_input.replace("what is the capital of", "").strip().rstrip("?")
            if country in self.knowledge_base:
                response = f"The capital of {country.capitalize()} is {self.knowledge_base[country]}."
            else:
                response = "Sorry, I don't know that yet."

        elif "and what about" in user_input:
            country = user_input.replace("and what about", "").strip().rstrip("?")
            if country in self.knowledge_base:
                response = f"The capital of {country.capitalize()} is {self.knowledge_base[country]}."
            else:
                response = "Sorry, I don't know that yet."

        else:
            generic_responses = [
                "I'm not sure about that, but I'm learning!",
                "Can you rephrase?",
                "Hmm, I need to think about that."
            ]
            response = random.choice(generic_responses)

        self.memory.add(user_input, response)
        return response, False
