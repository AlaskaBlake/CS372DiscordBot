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

    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick user from channel. Need permission to use it."""
        if reason ==None:
            await ctx.send("You need to provide a reason to kick someone.")
        else:
            await member.kick(reason=reason)
            await ctx.send(f"{member.name} was kicked for: {reason}")

    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        """Ban user from channel. Need permission to use it."""
        if reason == None:
            await ctx.send("Can't ban someone without a reason")
        else:

            await member.ban(reason = reason)
            await ctx.send(f"{member.name} was banned for: {reason}")

    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    @commands.command()
    async def unban(self,ctx,*,member):
        """Unban a user. Need permission to use it. [all, last]"""
        try:
            banned = await ctx.guild.bans()

            if not banned:
                 await ctx.send("Not a single user is banned. Ban someone first.") 
                 return
           
            if member != "all" and member !="last":
                name, discr = member.split("#")
            if member == "last":
                user = banned[len(banned)-1].user
                await ctx.guild.unban(user)
                await ctx.send(f"{user.name} is no longer banned.")
                return

            for ban in banned:
                if member =="all":
                    await ctx.guild.unban(ban.user)
                    continue 
                elif(ban.user.name,ban.user.discriminator) ==(name,discr):
                    await ctx.guild.unban(ban.user)
                    await ctx.send(f"{ban.user.name} is no longer banned.")
                    return

            await ctx.send("All banned member are no longer banned.")
        except:
            await ctx.send("Error: ~unban need Attention.")

    @commands.command()
    async def banlist(self,ctx):
        """Get a list of all banned users."""
        banned_user="banned users: \n"
        banned = await ctx.guild.bans()
        if not banned:
            await ctx.send("No banned user.")
        else:
            for ban in banned:
               banned_user+=ban.user.name +"#"+ ban.user.discriminator+"\n"
            await ctx.send(banned_user)


    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    @commands.command()
    async def mute(self,ctx,member:discord.Member,*,reason = None):
        """Mute a user. Need permission to use it."""
        try:
            for role in ctx.guild.roles:
                if role.name =="mute":
                    await member.add_roles(role)
                    await ctx.send(f"{member.name} has been muted")
                    return
              
            per = discord.PermissionOverwrite(send_messages=False)
            role = await ctx.guild.create_role(name="mute")

            for ch in ctx.guild.text_channels:
                    await ch.set_permissions(role,overwrite=per)

                    await member.add_roles(role)
                    await ctx.send(f"{member.name} has been muted")

        except:
            ctx.send("Error: ~mute Need Attention.")

    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    @commands.command()
    async def unmute(self,ctx,member:discord.Member):
        """Unmute a user. Need permission to use it."""
        try:
            for role in ctx.guild.roles:
                if role.name=="mute":
                    await member.remove_roles(role)
                    await ctx.send(f"{member.name} is now unmuted")
                    return
        except:
             ctx.send("Error: ~unmute Need Attention.")

    # mod channel #
    @commands.command()
    async def clear(self, ctx,amount=1):
        """Delete a amount of messages. Default amount is one."""
        await ctx.channel.purge(limit=amount+1)

def setup(client):
    client.add_cog(Moderation(client))
