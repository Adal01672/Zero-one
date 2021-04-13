import discord
from discord.ext import commands
import TenGiphPy


class Role(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

    @commands.command()
    async def clap(self, ctx, member: discord.Member = None):
        giftag = "animeclap"
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        getgifurl = t.random(giftag)
        if member == None:
            embed = discord.Embed(title=f"{ctx.author.name} claps")
            embed.set_image(url=f"{getgifurl}")
            await ctx.channel.send(embed=embed)
        if member == True:
            embed = discord.Embed(
                title=f"{ctx.author.name} claps at {member.name}")
            embed.set_image(url=f"{getgifurl}")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def bite(self, ctx, member: discord.Member = None):
        giftag = "animebite"
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        getgifurl = t.random(giftag)
        if member == None:
            embed = discord.Embed(title=f"{ctx.author.name} bites")
            embed.set_image(url=f"{getgifurl}")
            await ctx.send(embed=embed)
        if member == True:
            embed = discord.Embed(
                title=f"{ctx.author.name} bites {member.name}")
            embed.set_image(url=f"{getgifurl}")
            await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animecry"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} is crying")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} cried for {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)

    @commands.command()
    async def cuddle(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animecuddle"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} cuddles")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} is cuddling with {member.name}")
            embed.set_image(url=f"{getgifurl}")

        await ctx.send(embed=embed)

    @commands.command()
    async def dance(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animedance"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} dances")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} dances with {member.name}")
            embed.set_image(url=f"{getgifurl}")

        await ctx.send(embed=embed)

    @commands.command()
    async def facepalm(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animefacepalm"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} facepalms")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} facepalms at {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)

    @commands.command()
    async def glare(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animeglare"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} glares")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(title=f"{ctx.author.name} glares at {member.name}")
            embed.set_image(url=f"{getgifurl}")

        await ctx.send(embed=embed)

    @commands.command()
    async def greet(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animegreet"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} greets")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} greets {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)

    @commands.command()
    async def highfive(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animehighfive"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} highfives")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} highfives {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animehug"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} hugs")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} hugs {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)

    @commands.command()
    async def laugh(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animelaugh"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} laughs")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} laughs at {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def kiss(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animekiss"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} kisses")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} kisses {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def lick(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animelick"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} licks")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} licks {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def pat(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animepat"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} pats")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} pats {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def poke(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animepoke"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} pokes")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} pokes {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def pout(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animepout"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} pouts")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} pouts {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def punch(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animepunch"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} punches")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} punches {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def purr(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animepurr"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} purrs")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} purrs at {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def run(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animerun"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} runs")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} runs with {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def sad(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animepurr"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} is sad")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} and {member.name} is sad")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def shoot(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animeshoot"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} has a gun")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} shoots {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def shrug(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animeshrug"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} shrugs")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(title=f"{ctx.author.name} shrugs at {member.mention}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def shy(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animeshy"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} is feeling shy")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} is shy because of {member.mention}")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def slap(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animeslap"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} slaps")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} slaps {member.name}")
            embed.set_image(url=f"{getgifurl}")
        
        await ctx.send(embed=embed)

    @commands.command()
    async def smile(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animesmile"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} smiles")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} smiles at {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)

    @commands.command()
    async def stare(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animestare"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} stares")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} stares at {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)

    @commands.command()
    async def stomp(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animestomp"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} stomps")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} stomps {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
    @commands.command()
    async def die(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animedie"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} dies")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} and {member.name} die together")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def wiggle(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animewiggle"
        getgifurl = t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} wiggles")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} wiggles with {member.name}")
            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def wag(self, ctx, member: discord.Member = None):
        t = TenGiphPy.Tenor(token='Z1834KI2C7O3')
        giftag = "animesmile"
        getgifurl =     t.random(giftag)

        if not member:
            embed = discord.Embed(title=f"{ctx.author.name} wags")
            embed.set_image(url=f"{getgifurl}")

        if member:
            embed = discord.Embed(
                title=f"{ctx.author.name} wags with {member.name}")
            embed.set_image(url=f"{getgifurl}")

            embed.set_image(url=f"{getgifurl}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Role(client))
