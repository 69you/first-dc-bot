import discord 
from discord.ext import commands
from core.classes import cog_all
import json

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class owner_dm(cog_all):

    @commands.command()
    async def dm(self,ctx,member:discord.Member,*,message):
        if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
            await member.send(message)
            await ctx.message.add_reaction("✅")
            await ctx.message.delete()
        else:
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(owner_dm(bot))