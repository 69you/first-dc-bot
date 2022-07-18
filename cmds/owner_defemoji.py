from time import clock_settime
import discord 
from discord.ext import commands
from core.classes import cog_all
import json

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class owner_defemoji(cog_all):

    @commands.command()
    async def defemoji(self,ctx,msg,emoji):
        if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
            await ctx.message.delete()
            msg = await ctx.fetch_message(msg)
            await msg.add_reaction(emoji)
        else:
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(owner_defemoji(bot))