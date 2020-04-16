import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="~")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs/'):
    if filename.endswitch('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# This is not the Bots actual token, contributors have the correct token.
client.run('Dummy Token')
