import discord
from secretTokens import TOKEN
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix="!", intents = intents)
text_name_list = []
channel_name = ["announcement", "announcements"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("---------------------------------------------")
    for guild in client.guilds:
        for channel in guild.text_channels:
            text_name_list.append(channel.name)
    
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content[0] == "!":
        await client.process_commands(message)
        return
    
    print("message thing:")
    print(message.content)
    print("\n")

@client.command()
async def shutdown(ctx):
    print("Shutting down Clubot")
    print("---------------------------------------------")
    await ctx.bot.close()
    
@client.command()
async def msg(ctx, user:discord.Member, *, message=None):
    message = "Rohits a bitch"
    embed = discord.Embed(title=message)
    await user.send(embed=embed)


client.run(TOKEN)
