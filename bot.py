from lib2to3.pgen2 import token
from ntpath import join
from operator import truediv
from tabnanny import check
import discord
from discord.ext import commands

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="@@",intents=intents)
token="OTc3MDg2MDU2OTY3MDUzMzUz.Gk_nmf.V7bpZIwE94TbKIOW644HRgFSWO3vMLsHTf-7EQ"

@bot.event
async def on_ready():
    channel=bot.get_channel(977121281361182750)
    await channel.send( 'Ready :white_check_mark:' )


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
    channel=bot.channel


bot.run(token)    