from lib2to3.pgen2 import token
import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="@@")

token="OTc3MDg2MDU2OTY3MDUzMzUz.Gk_nmf.V7bpZIwE94TbKIOW644HRgFSWO3vMLsHTf-7EQ"

@bot.event

async def on_ready():
    print(">> Bot is ready")

bot.run(token)    