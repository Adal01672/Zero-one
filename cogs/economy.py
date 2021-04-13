import discord
from discord.ext import commands
import json

class Eco(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('economy is online')


def setup(client):
    client.add_cog(Eco(client))
