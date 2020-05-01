from random import random
from random import choice
import discord
from discord.ext import commands


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


# Stores all the links for cats.
# Bot randomly chooses from one of these images to send
catLinks = [
    "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cat-named-dymka-in-the-veterinary-clinic-best-where"
    "-it-had-news-photo-1582304174.jpg",
    "https://icatcare.org/app/uploads/2019/09/The-Kitten-Checklist-1.png",
    "https://media.npr.org/assets/img/2019/08/15/hank_wide-4df45b477add6d4b17d8e89e29a7572ba3dadc40.jpg",
    "https://www.aljazeera.com/mritems/imagecache/mbdxxlarge/mritems/Images/2020/4/13"
    "/ecab8c7af42a439d9043b0ade6e1f05b_18.jpg",
    "https://d17fnq9dkz9hgj.cloudfront.net/uploads/2018/03/Russian-Blue_01.jpg",
    "https://cdn.mos.cms.futurecdn.net/otjbibjaAbiifyN9uVaZyL-320-80.jpg",
    "https://wpcdn.us-east-1.vip.tn-cloud.net/www.channel3000.com/content/uploads/2020/04/cat.jpg",
    "https://cdn.vox-cdn.com/thumbor/hY2D3zvJkmJbkBtgnpMXYZUGl8E=/0x0:7952x5304/1200x675/filters:focal("
    "3340x2016:4612x3288)/cdn.vox-cdn.com/uploads/chorus_image/image/66701094/GettyImages_1127317526.0.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRtVfQZycBRHV3nMxhB_r6iCanq8LKOD0fKwEwUzYASXU9yqF2z&usqp"
    "=CAU",
    "https://api.time.com/wp-content/uploads/2015/02/cats.jpg"]


# Bot sends an image of a cat when pinged with cat
@commands.command(pass_context=True)
async def cat(ctx):
    await ctx.send(choice(catLinks))


# Stores all the links for dogs.
# Bot randomly chooses from one of these images to send
dogLinks = [
    "https://3snrvh1nlkatbz4yq1mpe7la-wpengine.netdna-ssl.com/wp-content/uploads/2011/07/cute-puppy-dog-wallpapers.jpg",
    "https://i0.wp.com/cdn-prod.medicalnewstoday.com/content/images/articles/292/292567/bichon-frise-dog.jpg",
    "https://i.ytimg.com/vi/Vp7nW2SP6H8/maxresdefault.jpg"
    "https://i.guim.co.uk/img/media/20098ae982d6b3ba4d70ede3ef9b8f79ab1205ce/0_0_969_1005/master/969.jpg",
    "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/large-dog-breeds-lead-1550810849.jpg",
]


# Bot sends an image of a cat when pinged with cat
@commands.command(pass_context=True)
async def dog(ctx):
    await ctx.send(choice(dogLinks))


# Bot says goodbye when pinged with bye
@commands.command(pass_context=True)
async def bye(ctx):
    await ctx.send("See you soon, friend!")


def setup(client):
    client.add_cog(Animal(client))
