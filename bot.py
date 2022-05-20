from lib2to3.pgen2 import token
from ntpath import join
from operator import truediv
from tabnanny import check
import discord
import json
from discord.ext import commands
with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="//",intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")


@bot.event 
async def on_member_join(member):
    channel=bot.get_channel(977121281361182750)
    await channel.send(f'{member} has join')

@bot.event 
async def on_member_remove(member):
    channel=bot.get_channel(977121281361182750)
    await channel.send(f'{member} has leave ')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')


bot.run(jdata['token'])    