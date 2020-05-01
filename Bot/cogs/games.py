import discord
from discord.ext import commands
from random import randint

class Games(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bear deployed')

    @commands.command(pass_context=True)
    async def roulette(ctx, arg1):
        await ctx.send("Hey lets play russian roulette: paintball style")
        userW = False
        bulletz = int(arg1)
        num = randint(1, bulletz)
        if bulletz < 25:
            for i in range(num):
                if i % 2 == 0:
                    await ctx.send("<< CLICK")
                    userW = True
                else:
                    await ctx.send("CLICK >>")
                    userW = False
            await ctx.send("< B A N G >")
            if userW:
                await ctx.send("You win!")
            if not userW:
                await ctx.send("You lose!")
        else:
            await ctx.send("Less than 25 rounds please")
        await ctx.send("Game ended.")

    @commands.command(pass_context=True)
    async def guess(ctx, arg1, arg2):
        await ctx.send("The Guessing Game! The number is between 1 and " + str(arg2))
        guess = int(arg1)
        answ = int(randint(1, int(arg2)))
        if int(arg1) < int(arg2):
            if guess == answ:
                await ctx.send("Hey you won! Nice guess :)")
            else:
                await ctx.send("Nice try, too bad")
                await ctx.send("The answer was: " + str(answ))
        else:
            await ctx.send("Choose a valid range, your guess " + str(arg1) + " is greater than the range")
        await ctx.send("Game ended.")

    @commands.command(pass_context=True)
    async def bear(ctx):
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

def setup(client):
    client.add_cog(Games(client))