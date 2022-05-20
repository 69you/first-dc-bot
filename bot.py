from lib2to3.pgen2 import token
from ntpath import join
from operator import truediv
import discord
from discord.ext import commands
intents=discord.Intents.default()



bot=commands.Bot(command_prefix="@@",intents=intents)

token="OTc3MDg2MDU2OTY3MDUzMzUz.Gk_nmf.V7bpZIwE94TbKIOW644HRgFSWO3vMLsHTf-7EQ"

@bot.event

async def on_ready():
    print(">> Bot is ready")

@bot.event 

async def on_member_join(member):
    print(f'{member}join')

@bot.event 

async def on_member_remove(member):
    print(f'{member}leave')

bot.run(token)    