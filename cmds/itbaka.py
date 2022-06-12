import discord
from discord.ext import commands
from core.classes import cog_all
import datetime

class baka(cog_all):
    @commands.command()
    async def it載點(self,ctx):
        embed=discord.Embed(title="IT版載點", url="https://drive.google.com/file/d/1UbujzGnivrAS47MvjNg7S-K6w_BvRr8v/view?usp=sharing", description="自己下載吧",  color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)

    @commands.command()
    async def IT載點(self,ctx):
        embed=discord.Embed(title="IT版載點", url="https://drive.google.com/file/d/1UbujzGnivrAS47MvjNg7S-K6w_BvRr8v/view?usp=sharing", description="自己下載吧",  color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)

    @commands.command()
    async def tbd載點(self,ctx):
        embed=discord.Embed(title="tbd載點", url="https://drive.google.com/file/d/1UbujzGnivrAS47MvjNg7S-K6w_BvRr8v/view?usp=sharing", description="自己下載吧",  color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(baka(bot))        