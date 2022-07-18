import discord 
from discord.ext import commands
from core.classes import cog_all
from typing import Union
import json,asyncio

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class owner_sayd(cog_all):

    @commands.command(aliases=["s"])
    async def sayd(self,ctx, *,msg=None):
        if msg==None:
            msg="** **"
        if ctx.author.id == (int(jdata["yuusuke id"])) or ctx.author.id==915809531865477180:
            await ctx.message.delete()
            await ctx.send(msg)
        else :
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(owner_sayd(bot))