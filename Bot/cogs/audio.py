import discord
import configparser
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

KEY = config['JAKE_SERVER']['BOT_KEY']
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! No, no, please, no!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(str(KEY))