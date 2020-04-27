import discord
import os
from discord.ext import commands

# This is the bot command prefix and chan be changed to almost anything.
# Just change the characters in the string on line 8 to what ever you like
# and it will be the new prefix for the bot.
client = commands.Bot(command_prefix="~")


# This is command is used when you want to add a cog while the bot is online
# without having to restart the bot.
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


# This command is used when you would not like the implementation of a certain cog.
# For example: you do not want the bot to be capable of music so you unload that cog
# and the commands for music are therefore unusable.
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


# This command is meant for development when the bot is online. If a cog is updated
# and you do not want to restart the bot simple reload the specified cog.
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


# This loads all cogs in the cogs folder on start up.
for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# This handle generic errors
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('No such command exist')

# This is not the Bots actual token. In the readme.md it describes how to create a bot
# and get its token. This is where the token needs to go for the bot to run. Please never
# upload yours bots actual token anywhere online. Discord's systems scans for bot tokens and
# will automatically regenerate a new token for the bot.
client.run('NzAwMTQzNDQxNjI3MDU0MDgx.XqZSEA.Ffmei27i-HYMkph8dXOczCoVOVc')
