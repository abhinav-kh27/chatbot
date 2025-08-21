# chat_memory.py

class ChatMemory:
    def __init__(self, max_memory=5):
        self.max_memory = max_memory
        self.memory = []

    def add(self, user_input, bot_response):
        self.memory.append((user_input, bot_response))
        if len(self.memory) > self.max_memory:
            self.memory.pop(0)

    def get_memory(self):
        return self.memory
