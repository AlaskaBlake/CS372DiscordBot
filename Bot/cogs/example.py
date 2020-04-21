import discord
from discord.ext import commands


# This cog is an example cog and serves to purpose except to be a demonstration on how
# you should set up your own cog if you choose to do so.
class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events should look like the below on_ready event.
    # They should begin with the @commands.Cog.listener() and have the function definition below it.
    # These are things that you do not need to input a command for it to execute.
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    # Commands should look like the below ping command.
    # Like events each command should begin with @commands.command() followed by it function definition.
    # The name of the function will be what you input for the command in a discord chat.
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')


def setup(client):
    client.add_cog(Example(client))
