import discord 
from discord.ext import commands
from core.classes import cog_all
import json

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class owner_edit(cog_all):

    @commands.command(aliases=["ed"])
    async def edit(self,ctx,msgid:int,*,message):
        if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
            await ctx.message.delete()
            msg=await ctx.fetch_message(msgid)
            await msg.edit(content=message)
        else:
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(owner_edit(bot))