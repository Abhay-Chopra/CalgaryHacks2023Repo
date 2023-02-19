import discord
import ical
import datetime
from secretTokens import TOKEN
from discord.ext import commands
from pytz import timezone
from io import BytesIO

intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.message_content = True
intents.guild_scheduled_events = True
intents.guilds = True
client = commands.Bot(command_prefix="!", intents = intents)
client.remove_command('help')
text_channel_list = []
channel_name = ["announcement", "announcements"]

@client.event
async def on_ready():
    print("---------------------------------------------")
    print('We have logged in as {0.user}'.format(client))
    print("---------------------------------------------")
    for guild in client.guilds:
        for channel in guild.text_channels:
            text_channel_list.append(channel)


@client.event
async def on_guild_join(guild):
    form = await guild.create_text_channel("form")
    
    embed = discord.Embed(title = "Opt in for Anouncment DM's ",description="Would you like to opt in to DM notifications?")
    msg = form.send(embed)
    msg.add_reaction("\u2705")
    msg.add_reaction("\u274E")


    
@client.event
async def on_raw_reaction_add(ctx):
    g = client.get_guild(ctx.guild_id)
    if ctx.channel_id != discord.utils.get(g.channels, name="form").id:
        return

    u = client.get_user(ctx.user_id)
       
    

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

#TODO Check Permissions for shutdown command
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
    del(cal)
    cal = ical.iCal()
    
    start_date = "%d/%d/%d" % (event.start_time.year, event.start_time.month, event.start_time.day)
    end_date = "%d/%d/%d" % (event.end_time.year, event.end_time.month, event.end_time.day)
    start_time = "%d:%d" % (event.start_time.astimezone(tz = mst).hour, event.start_time.astimezone(tz = mst).minute)
    end_time = "%d:%d" % (event.end_time.astimezone(tz = mst).hour, event.end_time.astimezone(tz = mst).minute)
    
    bin_file = cal.make_event(event.name, event.description, start_time, end_time, start_date, end_date)
    for user in event.guild.members:
        if bin_file is None: 
            break
        if user != client.user:
            out = BytesIO(bin_file)
            del(out)
            out = BytesIO(bin_file)
            file = discord.File(fp = out, filename = event.name + ".ics")
            out.flush()
            out.seek(0)
            await user.send(file=file)

@client.event
async def announcement(message, file=None):  
    for user in message.guild.members:
        if user != client.user:
            embed = discord.Embed(title = "Announcement from: " + message.guild.name, description = message.content)
            await user.send(embed=embed)

@client.group(invoke_without_command=True)
async def help(ctx):
    help = discord.Embed(title= "Help", description="Use !help <<command>> for detailed help about a command. Use an ! at the start of your CluBot command.")
    help.add_field(name="Moderation", value="msg | shutdown | announce | schedule")
    await ctx.send(embed = help)


@help.command()
async def msg(ctx):
    msg = discord.Embed(title= "msg", description="Send a message through CluBot to a specific user.")
    msg.add_field(name="SYNTAX: ", value="!msg [user]")
    await ctx.send(embed = msg)

@help.command()
async def shutdown(ctx):
    shut = discord.Embed(title= "shutdown", description="Shut down CluBot.")
    shut.add_field(name="SYNTAX: ", value="!shutdown")
    await ctx.send(embed = shut)

@help.command()
async def announce(ctx):
    announce = discord.Embed(title= "announce", description="Shut down CluBot.")
    announce.add_field(name="SYNTAX: ", value="Automatic when message is sent in an announcement channel, sent to all users who have opted in to CluBot.")
    await ctx.send(embed = announce)

@help.command()
async def schedule(ctx):
    schedule = discord.Embed(title= "schedule", description="Schedule a meeting and send an iCal file with CluBot.")
    schedule.add_field(name="SYNTAX: ", value="Automatic when Discord event is created, sent to all users who have opted in to CluBot.")
    await ctx.send(embed = schedule)

@client.command()
async def create_form(ctx):
    form = await ctx.guild.create_text_channel("form")
    
    embed = discord.Embed(title = "Opt in for Anouncment DM's ",description="Would you like to opt in to DM notifications?")
    msg = await form.send(embed=embed)
    await msg.add_reaction("\u2705")
    await msg.add_reaction("\u274E")
    

client.run(TOKEN)
