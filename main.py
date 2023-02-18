import discord
from secretTokens import TOKEN
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix="!", intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("---------------------------------------------")
    
@client.command()
async def shutdown(ctx):
    print("Shutting down Clubot")
    print("---------------------------------------------")
    await ctx.bot.close()
    
client.run(TOKEN) 