import discord
import json
import random
import os
import datetime
import asyncio
from discord.ext import commands
import keep_alive
 

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="*",intents=intents,help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="“hello, world 2022”"),status=discord.Status.dnd)
    print("\nBot is ready")

@bot.command()
async def ping(ctx):
    message=await ctx.send("🏓 Pinging...")
    await asyncio.sleep(1)
    await message.edit(content="延遲 "+f'{round(bot.latency*1000)} (ms)')


def run():
    for filename in os.listdir('./cmds'):
        if filename.endswith(".py"):
            print(f'{filename[:-3]}')
            bot.load_extension(f'cmds.{filename[:-3]}')

def init():
        os.system("pip uninstall discord.py")
        os.system("cls")
        os.system("pip install discord.py")
        os.system("cls")  

if __name__=='__main__':
    try:
        init()
        run()
        keep_alive.keep_alive()
        bot.run("OTc3MDg2MDU2OTY3MDUzMzUz.GQoqEG.rSOmEvwWjNYA6Ip-uNKvdkw7XdeR3WUVT8IFtY")
    except:
        os.system("kill 1")