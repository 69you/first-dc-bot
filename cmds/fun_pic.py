import discord
from discord.ext import commands
from core.classes import cog_all
import json,random

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class fun_pic(cog_all):
    
    @commands.command()
    async def pic(self,ctx):
        await ctx.send((random.choice(jdata['pic'])))


def setup(bot):
    bot.add_cog(fun_pic(bot))
