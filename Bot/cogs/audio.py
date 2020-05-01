import discord
from discord.ext import commands

players = {}

bot = commands.Bot(command_prefix = '.')

class Audio(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events

    # Commands
    @commands.command(pass_context=True)
    async def join(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command(pass_context=True)
    async def leave(ctx):
        await ctx.bot.disconnect()

    @commands.command(pass_context=True)
    async def play(ctx):
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('Oh_No.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

def setup(client):
    client.add_cog(Audio(client))

