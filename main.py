import discord
import os
from secretTokens import TOKEN

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user or message:
        return
    print("message sent")



client.run(TOKEN)
