import cmd
from email import message
from lib2to3.pgen2 import token
from ntpath import join
from operator import truediv
from ssl import CHANNEL_BINDING_TYPES
from tabnanny import check
import discord
import json
import random
import os
import datetime
import asyncio
from discord.ext import commands

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="*",intents=intents,help_command=None)
datetime.timezone

@bot.event
async def on_ready():
    print("Bot is ready")
    channel=bot.get_channel(977121281361182750)
    await channel.send("Ready <a:emoji_33:971218065259913226>" ) 
    

for filename in os.listdir('./cmds'):
    if filename.endswith(".py"):
        bot.load_extension(f'cmds.{filename[:-3]}')


if __name__=='__main__':
    bot.run(jdata['token'])  