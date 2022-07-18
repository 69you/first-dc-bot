import discord
from discord.ext import commands
from core.classes import cog_all
import json , datetime 
from typing import Union

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class fun_bigemoji(cog_all):

    @commands.command(aliases=["be"])
    async def bigemoji(self,ctx,emoji:Union[discord.Emoji, discord.PartialEmoji]):
        if emoji.animated==False:
            await ctx.message.delete()
            embed=discord.Embed(title=f"{ctx.author} 要求的表符", description=f"`:{emoji.name}:{emoji.id}`", color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_image(url = f"{emoji.url}")
            await ctx.send(embed=embed)
        elif emoji.animated==True:
            await ctx.message.delete()
            embed=discord.Embed(title=f"{ctx.author} 要求的表符", description=f"`a:{emoji.name}:{emoji.id}`", color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_image(url = f"{emoji.url}")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun_bigemoji(bot))