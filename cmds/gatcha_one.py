import discord
from discord.ext import commands
import random,asyncio
from core.classes import cog_all

class gatcha_one(cog_all):

    @commands.command()
    async def 單抽(self,ctx):
        a=random.uniform(1,100)
        if(a>11.5):
            msga=await ctx.reply("<:pre2:986995238117720114>")
            await asyncio.sleep(2)
            await msga.edit(content="<:2s:986995284850667520>")
        elif(a<11.5 and a>3):
            b=random.uniform(1,100)
            if(b<10):
                msgb=await ctx.reply("<:pre3:986995251824717864>")
                await asyncio.sleep(2)
                await msgb.edit(content="<:4s:986995312046514227>")
            else:
                msgc=await ctx.reply("<:pre3:986995251824717864>")
                await asyncio.sleep(2)
                await msgc.edit(content="<:3s:986995297647460383>")
        elif(a<3):
            msgc=await ctx.reply("<:pre4:986995267742089386>")
            await asyncio.sleep(1)
            await msgc.edit(content="<:4s:986995312046514227>")


def setup(bot):
    bot.add_cog(gatcha_one(bot))