import discord
import ical
import datetime
from secretTokens import TOKEN
from discord.ext import commands
from pytz import timezone

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guild_scheduled_events = True
client = commands.Bot(command_prefix="!", intents = intents)
text_name_list = []
channel_name = ["announcement", "announcements"]

@client.event
async def on_ready():
    print("---------------------------------------------")
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
    print("---------------------------------------------")
    print("Shutting down Clubot")
    print("---------------------------------------------")
    await ctx.bot.close()
    
    
@client.command()
async def msg(ctx, user:discord.Member, *, message):
    await user.send(message)
    
@client.event
async def on_scheduled_event_create(event:discord.ScheduledEvent):
    mst = timezone('MST')
    cal = ical.iCal()
    
    start_date = "%d/%d/%d" % (event.start_time.year, event.start_time.month, event.start_time.day)
    end_date = "%d/%d/%d" % (event.end_time.year, event.end_time.month, event.end_time.day)
    start_time = "%d:%d" % (event.start_time.astimezone(tz = mst).hour, event.start_time.astimezone(tz = mst).minute)
    end_time = "%d:%d" % (event.end_time.astimezone(tz = mst).hour, event.end_time.astimezone(tz = mst).minute)
    
    file = cal.make_event(event.name, event.description, start_time, end_time, start_date, end_date)
    
client.run(TOKEN)
