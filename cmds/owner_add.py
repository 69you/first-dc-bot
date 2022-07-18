import discord 
from discord.ext import commands
from core.classes import cog_all
from typing import Union
import json

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class owner_add(cog_all):

    @commands.command()
    async def add(self,ctx,remes:int,emoji:Union[discord.Emoji, discord.PartialEmoji]):
        if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
            await ctx.message.delete()
            msg = await ctx.fetch_message(remes)
            await msg.add_reaction(emoji)
        else:
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(owner_add(bot))