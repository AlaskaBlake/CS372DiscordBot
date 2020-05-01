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
    async def roulette(self, ctx, arg1):
        """Given a number between zero and 25, starts that many rounds of russian roulette."""
        await ctx.send("Hey lets play russian roulette: paintball style")
        user_win = False
        bullets = int(arg1)
        num = randint(1, bullets)
        if bullets < 25:
            for i in range(num):
                if i % 2 == 0:
                    await ctx.send("<< CLICK")
                    user_win = True
                else:
                    await ctx.send("CLICK >>")
                    user_win = False
            await ctx.send("< B A N G >")
            if user_win:
                await ctx.send("You win!")
            if not user_win:
                await ctx.send("You lose!")
        else:
            await ctx.send("Less than 25 rounds please")
        await ctx.send("Game ended.")

    @commands.command(pass_context=True)
    async def guess(self, ctx, arg1, arg2):
        """First number is guess, second number is range of guessing game"""
        await ctx.send("The Guessing Game! The number is between 1 and " + str(arg2))
        guess = int(arg1)
        answer = int(randint(1, int(arg2)))
        if int(arg1) < int(arg2):
            if guess == answer:
                await ctx.send("Hey you won! Nice guess :)")
            else:
                await ctx.send("Nice try, too bad")
                await ctx.send("The answer was: " + str(answer))
        else:
            await ctx.send("Choose a valid range, your guess " + str(arg1) + " is greater than the range")
        await ctx.send("Game ended.")

    @commands.command(pass_context=True)
    async def character(self, ctx, *, arg1):
        """Give a single name for character generator"""
        alignments = ["lawful good", "neutral good", "chaotic good", "lawful neutral", "true neutral",
                      "chaotic neutral",
                      "lawful evil", "neutral evil", "chaotic evil"]
        races = ["human", "dwarf", "elf", "half-elf", "gnome", "orc", "half-orc", "goblin", "werewolf", "vampire"]
        classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue",
                   "sorcerer",
                   "warlock", "wizard"]
        eyes = ["yellow", "amber", "brown", "hazel", "green", "blue", "gray", "aqua", "red", "purple", "pale brown",
                "pale blue", "deep blue", "orange", "emerald", "sea green", "spring green"]
        skins = ["pale", "light tan", "tan", "orange tan", "medium brown", "ebony", "pale gray"]
        hairs = ["black", "gray", "platinum", "dark blond", "white", "bleach blond", "dark redhead",
                 "light redhead",
                 "brunette", "Auburn", "hazel", "lavender", "pale blue", "royal blue", "black with white streaks"]
        flaws = ["judges others harshly, and themselves even more severely",
                 "blindly trust those that profess faith in their god", "suspicious of strangers",
                 "can't resist a pretty face",
                 "money > friends", "convinced that no one could ever fool them in the way they fool others",
                 "willing to do anything to win fame and renown"
                 "the tyrant who rules the land will stop at nothing to see them killed",
                 "weakness for the vices of the city, especially hard drink", "would kill to acquire a noble title",
                 "harbors dark bloodthirsty thoughts that their isolation failed to quell",
                 "need to win arguments overshadow friendships and harmony",
                 "hiding a truly scandalous secret that could ruin their family forever.",
                 "no room for caution in a life lived to the fullest",
                 "unlocking an ancient mystery is worth the price of a civilization",
                 "can't keep a secret to save their life, or anyone else's",
                 "once someone questions their courage, I never back down no matter how dangerous the situation",
                 "can't help but pocket loose coins and other trinkets they come across",
                 "if they're outnumbered, they always run away from a fight",
                 "they'd rather kill someone in their sleep than fight fair"
                 ]
        abilities = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        await ctx.send("Name: " + str(arg1))
        await ctx.send("Alignment: " + alignments[randint(0, len(alignments) - 1)])
        await ctx.send("Class: " + classes[randint(0, len(classes) - 1)])
        await ctx.send("Race: " + races[randint(0, len(races) - 1)])
        await ctx.send("Eyes: " + eyes[randint(0, len(eyes) - 1)])
        await ctx.send("Skin: " + skins[randint(0, len(skins) - 1)])
        await ctx.send("Hair: " + hairs[randint(0, len(hairs) - 1)])
        await ctx.send("Flaw: " + flaws[randint(0, len(flaws) - 1)])
        await ctx.send("Best Ability: " + abilities[randint(0, len(abilities) - 1)])
        await ctx.send("There's your character!")

    @commands.command(pass_context=True)
    async def bear(self, ctx):
        """A bear minding it's own business"""
        await ctx.send(
            "https://66.media.tumblr.com/b1062ee309f5b95cf532be77842e9b0d/tumblr_nnysxtcv2C1s02vreo2_400.gif")


def setup(client):
    client.add_cog(Games(client))
