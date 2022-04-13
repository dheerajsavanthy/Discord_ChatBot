import discord
from neuralintents import GenericAssistant
import os 
import nltk

chatbot = GenericAssistant('Knowledge_base.json')
chatbot.train_model()
chatbot.save_model()


client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!bot'):
        response = chatbot.request(message.content[5:])
        await message.channel.send(response)
    

    

client.run('OTUyODMzMjcyNzgwNTg3MDM5.Yi7xIw.E06xUUwTEF1roz_SZsAR6e_6_1A')
