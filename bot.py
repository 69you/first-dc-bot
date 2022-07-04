import discord
import json
import random
import os
import datetime
import asyncio
from discord.ext import commands
import discord_slash
from discord_slash import SlashCommand

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="**",intents=intents,help_command=None)
slash=SlashCommand(bot,sync_commands=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="“hello, world 2022”"),status=discord.Status.dnd)
    print("\nBot is ready")
    channel=bot.get_channel(977121281361182750)
    await channel.send("Ready <a:emoji_33:971218065259913226>" ) 
    online_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
    await channel.send(f"啟動時間: {online_time}")

@bot.event
async def on_message_delete(before):
    if before.channel.id==910799151384633344:
        if before.author.bot==False:
            link = str(before.author.avatar_url_as(format="png"))
            embed=discord.Embed(title=f"{before.author},id= {before.author.id}",description=f"{before.content}",color=0xfd12ca,timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_author(name=f"{before.author}",icon_url=f"{link}")
            await before.channel.send(embed=embed)

for filename in os.listdir('./cmds'):
    if filename.endswith(".py"):
        print(f'{filename[:-3]}')
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__=='__main__':
    bot.run("OTgwMzU4OTE1MTg1MzE5OTg2.GXLzLc.k5xEbULmmQfncxaZWojY1lqH4BMkJ-2J3LpdE0")