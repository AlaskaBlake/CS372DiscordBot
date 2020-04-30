![Discord Logo](https://github.com/AlaskaBlake/CS372DiscordBot/blob/master/Discord%20Logo.jpg)

# CS372DiscordBot

This is repository that can be used for people to create their own discord bot. This code was made for a discord bot token to be put 
in the location listed in the main.py file. Once the token is put in and main.py is compiled with the other files in the "cog" folder, 
you will have a fully functional discord bot with the capabilities listed below. For how to make a discord bot, inviting it to your
server, and getting its token see below as well.

# Moderation



# Games



# Image Searching



# Music



# Making a Discord Bot and Obtaining its Token

1. Create a discord account at [Discord](https://discordapp.com/).
2. Once your account is created, under the Developers tab select the [Developers Portal](https://discordapp.com/developers/applications).
3. In the top right create a new application and give it a name.
4. On the left hand side of the window select Bot.
5. On the right hand side select Add Bot.
6. At the bottom of the Bot tab in the permissions section select administrator. This is needed because the bot will be capable of
      moderation tasks.
7. You can then select Click To Reveal Token. 

# Inviting the Bot to Your Server

1. You have to have admin privileges for the server.
2. Go into the developer portal you used to create the bot.
3. Click on the desired application then go to the OAuth2 tab.
4. In the scopes section select "bot"
5. Copy the invite link into a web browser and invite it to your chosen server.

# Development

The bot is made to be a starting point for people to create their own bot. Please use the example cog as a demonstration for the
syntax for the bot. We are adhering to the Clang Tidy standards for clean code in Python. If you believe you have a cog that should
be added to the project please submit a pull request to add the cog. Pull Requests will not be accepted if they edit the existing cogs
unless and issue is found.
