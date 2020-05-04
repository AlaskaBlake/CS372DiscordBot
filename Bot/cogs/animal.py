import random
from http import client
import self as self
from discord.ext.commands import Bot
import ctx as ctx
import discord
from discord.ext import commands
import embedlinks


class Animal(commands.Cog):

    def __init__(self, client):
        self.client = client


@commands.Cog.listener()
async def on_ready(self):
    print("Bot Online!")


# Bot says hi when pinged with hello!
@commands.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Hey!")


# Bot says goodbye when pinged with bye
@commands.command(pass_context=True)
async def bye():
    await ctx.send("See you soon, friend!")


# Bot sends an image of a cat with pinged with cat
@commands.command(pass_context=True)
async def cat(ctx):
    chosen_image = random.choice(embedlinks.catLinks)

    embed = discord.Embed(color=0xff69b4)
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f"Requested by: {ctx.author.name}")

    await ctx.send(embed=embed)


# Bot sends an image of a dog when pinged with dog
@commands.command(pass_context=True)
async def dog(ctx):
    chosen_image = random.choice(embedlinks.dogLinks)

    embed = discord.Embed(color=0xff69b4)
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f"Requested by: {ctx.author.name}")

    await ctx.send(embed=embed)


# Bot sends an image of a random animal when pinged with surprise
@commands.command(pass_context=True)
async def surprise(ctx):
    chosen_image = random.choice(embedlinks.surpriseLinks)

    embed = discord.Embed(color=0xff69b4)
    embed.set_image(url=chosen_image)
    embed.set_footer(text=f"Requested by: {ctx.author.name}")

    await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Animal(client))
