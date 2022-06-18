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

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="“hello, world 2022”"),status=discord.Status.dnd)
    print("\nBot is ready")
    channel=bot.get_channel(977121281361182750)
    await channel.send("Ready <a:emoji_33:971218065259913226>" ) 
    online_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
    await channel.send(f"啟動時間: {online_time}")
    
for filename in os.listdir('./cmds'):
    if filename.endswith(".py"):
        print(f'{filename[:-3]}')
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__=='__main__':
    bot.run("OTc3MDg2MDU2OTY3MDUzMzUz.GwZaQ0.w5u9B5NpOEgEGUWpmgdkRckDN2qhGbgRSRP9Ps") 