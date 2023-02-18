import discord
import os

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run('MTA3NjU3OTc0MDUzNTc1MDY2Ng.GgLLbJ.Yv5DyJMNqdskiAb9R_eyf2MzZ29wQuFk6VS-SQ')
