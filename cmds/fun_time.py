import discord
from discord.ext import commands
from core.classes import cog_all
import json,datetime

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class fun_time(cog_all):
    
    @commands.command()
    async def time(self,ctx):
        now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
        await ctx.channel.send(f"現在時間: {now_time}")  


def setup(bot):
    bot.add_cog(fun_time(bot))