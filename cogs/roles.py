import discord
from discord.ext import commands
import json

class Eco(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('role is online')

    def get_roleid(client, message):
        with open("roles.json","r") as f:
            roleid=json.load(f)
        
        return str(roleid[str(message.guild.id)])


def setup(client):
    client.add_cog(Eco(client))