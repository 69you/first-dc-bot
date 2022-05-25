import discord
from discord.ext import commands
import json , random
from core.classes import cog_all

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class pic(cog_all):
    @commands.command()
    async def pic(self,ctx):
        ramdon_pic=random.choice(jdata['pic'])
        await ctx.send(ramdon_pic)

def setup(bot):
    bot.add_cog(pic(bot))