# bot.py

import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def ping(message):
    await message.send(f"{round(client.latency * 1000)}ms")


@client.command()
async def shrug(message, *, text):
    await message.send(str(text)+str("¯\_(ツ)_/¯"))


@client.command()
async def embed(message, title:str=None, description:str=None, location:int=None):
    if title is None:
        title=""
    if description is None:
        description=""
    title=title.replace("_"," ")
    description=description.replace("_"," ")
    embed=discord.Embed(title=title, description=description)
    if location is None:
        await message.send(embed=embed)
    else:
        channel = client.get_channel(location)
        await channel.send(embed=embed)
        
@client.command()
async def colorme(message):
    if 


client.run(TOKEN)