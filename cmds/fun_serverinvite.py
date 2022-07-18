import discord
from discord.ext import commands
from core.classes import cog_all
import json 

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


class fun_serverinvite(cog_all):

    @commands.command(aliases=["si"])
    async def serverinvite(self,ctx):
            link=await ctx.channel.create_invite()
            await ctx.send(str(link)) 

def setup(bot):
    bot.add_cog(fun_serverinvite(bot))   