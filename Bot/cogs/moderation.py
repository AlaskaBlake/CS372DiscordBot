import discord
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events

    # Commands
    @commands.command()
    async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason = reason)
        await ctx.send(member +" was kick. Reason: "+ reason)

def setup(client):
    client.add_cog(Moderation(client))
