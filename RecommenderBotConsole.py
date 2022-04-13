from neuralintents import GenericAssistant
import os
import nltk

chatbot = GenericAssistant('knowledge_base.json')
chatbot.train_model()
chatbot.save_model()

while True:
    message = input("User: ")
    if message.startswith("!bot "):
        message.replace("!bot ", "")
        response = chatbot.request(' '.join(message.split()[-5:]))
        print("Bot: ", response)