# CluBot - University Club Announcement Scraper
CluBot is a Discord bot that scrapes university club announcements and sends them to users as private messages. The bot can also generate .ics files when community events are created in the Discord server. CluBot only sends messages to people who opt into the notifications using reactions to a server form.

## Getting Started
To use CluBot, you will need to have Python, the icalendar library, and the discord.py library installed on your computer.

Download and install Python from the official website: https://www.python.org/downloads/
<br><br>
Install the icalendar library by running the following command in your terminal:
```pip install icalendar```<br><br>
Install the discord.py library by running the following command in your terminal:
```pip install discord.py```<br><br>
Clone the CluBot repository to your local machine:

```git 
git clone https://github.com/YOUR_USERNAME/CluBot.git
```
<br>
Create a Discord bot and invite it to your server. Follow the instructions in the Discord Developer Portal to create a new bot and get its token.

Set up the necessary environment variables. Create a .env file in the root directory of the project and add the following variables:

```python
DISCORD_TOKEN=your-bot-token-goes-here
```
<br>
Run the bot by executing the following command in your terminal:

```python
python bot.py
```
<br>
# Usage
To start using CluBot, simply react with the corresponding emoji on the server form to opt into notifications. The bot will then send you private messages when new announcements or events are posted in the server.

## Commands
'!help': Displays a help message with a list of available commands.<br>
'!shutdown': Stops the bot.<br>
'!create_announcements_channel': Creates the channel of your server where CluBot can scrape data<br>

## What I Learned
During the development of CluBot, I learned several new skills and concepts, including:

1) Working with Discord's API: I gained experience with using Discord's API to interact with the server and users, including sending private messages and generating .ics files.<br>
2) Using .ics files: I learned about the structure and syntax of .ics files, and how they can be used to store event data. I also learned about the iCalendar standard and how it is used to exchange calendar data.<br>
3) Collaborating with Git in a group: I learned about the best practices for using Git in a team environment, including branch management, code review, and resolving conflicts. I also gained experience with using GitHub to manage a group project.<br>
4) Writing modular code: I learned about the benefits of writing modular code and breaking down a large project into smaller, more manageable components. This made it easier to test and debug individual parts of the bot and made it more extensible for future development.<br>
5) Implementing error handling: I learned about the importance of implementing error handling in a bot to ensure it is robust and can handle unexpected input or errors. I used try-except blocks and logging to catch and handle errors in CluBot.<br>
6) Understanding permissions: I gained a better understanding of the different levels of permissions in Discord and how they can be used to control access to different parts of a server. I also learned about the various types of Discord roles and how they can be used to grant permissions to users.
