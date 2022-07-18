import discord
from discord.ext import commands
from core.classes import cog_all
import json 

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class fun_invite(cog_all):

    @commands.command()
    async def invite(self,ctx):
        embed=discord.Embed(title="人工智障的邀請函",url="https://discord.com/api/oauth2/authorize?client_id=977086056967053353&permissions=8&scope=bot%20applications.commands",description=f"邀請前請先找 `侑介#4644`", color=0xfd12ca)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun_invite(bot))