from ast import alias
import discord
from discord.ext import commands
import asyncio,datetime,json
from core.classes import cog_all

class info(cog_all):
    @commands.command(aliases=["sf"])
    async def severinfo(self,ctx):
        guild=ctx.guild
        #await ctx.send(f"{guild.banner_url}")
        await ctx.send(f"{guild.owner}")
        await ctx.send(f"{guild.created_at}")
        ch=(guild.channels)
        for i in (len(ch)):
            print (ch[i])


def setup(bot):
    bot.add_cog(info(bot))