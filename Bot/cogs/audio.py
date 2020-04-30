import discord
from discord.ext import commands
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

KEY = config['JAKE_SERVER']['BOT_KEY']
bot = commands.Bot(command_prefix = '.')

players = {}

@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(pass_context=True)
async def leave(ctx):
    await ctx.bot.disconnect()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.command(pass_context=True)
async def play(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('Oh_No.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)


bot.run(KEY)