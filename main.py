import discord
import os
from secretTokens import TOKEN
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(command_prefix = "!",intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user and:
        return
    print("message thing:")
    print(message.content)
    print("\n")

    


client.run(TOKEN)
