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
from discord.ext import commands

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="*",intents=intents)
datetime.timezone

@bot.event
async def on_ready():
    print("Bot is ready")
    channel=bot.get_channel(977121281361182750)
    await channel.send("Ready <a:emoji_33:971218065259913226>" )

@bot.command()
async def help1(ctx):
    embed=discord.Embed(title="侑介のbot", url="http://yt1.piee.pw/46vhku", description="由侑介#4644所開發的人工智障", color=0xfd12ca, timestamp=datetime.datetime.utcnow())
    embed.set_author(name="<==這是侑介", icon_url="https://cdn.discordapp.com/avatars/878830839822176287/e947993f71d34bd423b0a24e166ccf42.png?size=4096")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/977086056967053353/ebc17adf1bc26fe27571586430b56ae8.png?size=4096")
    await ctx.send(embed=embed) 
    

for filename in os.listdir('./cmds'):
    if filename.endswith(".py"):
        bot.load_extension(f'cmds.{filename[:-3]}')


if __name__=='__main__':
    bot.run(jdata['token'])    