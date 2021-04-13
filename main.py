import discord
from discord.ext import commands
import os
import TenGiphPy
import json
def get_prefix(client,message):
    with open("prefixes.json","r") as f:
        prefixes=json.load(f)
    return prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix=get_prefix)

@client.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '!'#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

@client.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True) #ensure that only administrators can use this command
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f: #writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)
    em=discord.Embed(title=f"prefix changed to `{prefix}`",color=0x4287f5)

    await ctx.send(embed=em) #confirms the prefix it's been changed to
#next step completely optional: changes bot nickname to also have prefix in the nickname
    name=f'{prefix}BotBot'

@client.event
async def on_message(msg):
    
    if str(client.user.id) in msg.content:
        with open("prefixes.json","r") as f:
            prefixes = json.load(f)

        pre =prefixes[str(msg.guild.id)]
        em=discord.Embed(title=f"My prefix is `{pre}` for this server",color=0x4287f5)

        await msg.channel.send(embed=em)

    await client.process_commands(msg)


@client.event
async def on_ready():
    print("Lets goo")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f"cogs.{filename[:-3]}")
        except Exception as error:
            print(f"An Error occured: {error}")
            print(f"Filename: {filename}")



client.run(os.environ.get("TOKEN"))

