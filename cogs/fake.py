import discord
from discord.ext import commands
import json
import praw
import random


class lame(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('random is online')



    

    @commands.command(pass_context=True)
    async def meme(self,ctx):
        reddit = praw.Reddit(
    client_id="Nsuc_eNCAZnadQ",
    client_secret="RLs2uA5nKzHAD6MkykQjrF7zzQ3B0A",
    password="adal016724",
    user_agent="pythonpraw",
    username="adal01672",
    )
        
        subreddit = reddit.subreddit("DarlingInTheMemes")
        all_subs = []

        top = subreddit.top(limit=50)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed(title = name, color=0x4287f5)

        embed.set_image(url=url)

        await ctx.send(embed=embed)

    


    @commands.command(pass_context=True)
    async def support(self,ctx):
        em=discord.Embed(title="You can always get support here at https://discord.gg/RzuQn7BfqS", color=0x4287f5)
        await ctx.send(embed=em)



def setup(client):
    client.add_cog(lame(client))