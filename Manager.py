import discord
from discord.ext import commands
from pystyle import *
import json

with open('config.json') as f:
    data = json.load(f)
    token = data["token"]


default_intents = discord.Intents.all()
default_intents.members = True

client = discord.Client(intents=default_intents)

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot prêt")
    await bot.change_presence(status=discord.Status.online,
            activity=discord.Game("""
!help | Developped by GameCreep35#5395"""))
    
@bot.event
async def on_member_join(member: discord.Member):
    await member.send('Bienvenue')

@bot.event
async def on_message(message):
    user = message.author
    if message.author.name == 'Manager Bot':
        exit
    else:
        print("{0} > {1} : {2}".format(message.channel ,message.author.name, message.content))
    welcome_channel = 964214338770571424
    if 'free nitro' in message.content:
        await user.kick()
        await message.channel.send('{} has been kick for : free nitro'.format(user))
        print('has been kick for : free nitro')

    if message.content.startwith('a'):
        await message.channel.send('feur')
    elif message.content == 'Quoi':
        await message.channel.send('feur')
    elif message.content == 'ouge':
        await message.channel.send('gorge')
    elif message.content == 'Ouge':
        await message.channel.send('gorge')
    elif message.content == 'profonde':
        await message.channel.send('ément')
    elif message.content == 'Profonde':
        await message.channel.send('ément')

@bot.event
async def on_member_join(message):
    member = message.author.name
    channel = bot.get_channel(964214338770571424)
    embed=discord.Embed(
        title="Bienvenue {}.".format(message.author.name),
        description="Merci d'avoir rejoint le serveur !",
        color = discord.Color.yellow()
    )
    await channel.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------------------

bot.run(token)