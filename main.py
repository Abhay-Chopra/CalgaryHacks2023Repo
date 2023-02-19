import discord
from secretTokens import TOKEN
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix="!", intents = intents)
text_channel_list = []
channel_name = ["announcement", "announcements"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("---------------------------------------------")
    for guild in client.guilds:
        for channel in guild.text_channels:
            text_channel_list.append(channel)

    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content[0] == "!":
        await client.process_commands(message)
        return
    for channel in text_channel_list:
        for cname in channel_name:
            if channel.name == cname:
                announcement_channel = channel
    if message.channel == announcement_channel:
        await announcement(message)
    else:
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
    
@client.event
async def announcement(message):  
    for user in message.guild.members:
        if user != client.user:
            embed = discord.Embed(title= "😎 " +message.guild.name+ " 😎", description=message.content)
            await user.send(embed=embed)


client.run(TOKEN)
