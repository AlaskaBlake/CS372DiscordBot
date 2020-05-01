import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation online')

    # Commands #

    # mod user #
    @commands.command()
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick user from channel. Only admin can user it."""
        if reason ==None:
            await ctx.send("You need to provide a reason to kick someone.")
        else:
            await member.kick(reason=reason)
            await ctx.send(f"{member.name} was kicked for: {reason}")

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        """Ban user from channel. Only admin can user it."""
        if reason == None:
            await ctx.send("Can't ban someone without a reason")
        else:

            await member.ban(reason = reason)
            await ctx.send(f"{member.name} was banned for: {reason}")


    # mod channel #
    @commands.command()
    async def clear(self, ctx,amount=1):
        """Clear a amount of messages. Default amount is one."""
        await ctx.channel.purge(limit=amount+1)

def setup(client):
    client.add_cog(Moderation(client))
