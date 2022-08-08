import discord
from discord.ext import commands
from core.classes import cog_all
import datetime

class baka(cog_all):
    @commands.command()
    async def it載點(self,ctx):
        embed=discord.Embed(title="IT版載點", url="https://drive.google.com/file/d/1wUn6pHr-KVDpagX9bApktrfQkr045gBY/view?usp=sharing", description="自己下載吧",  color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)

    @commands.command()
    async def IT載點(self,ctx):
        embed=discord.Embed(title="IT版下載教學影片", url="http://surl.li/cineu", description="自己研究吧",  color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)

    @commands.command()
    async def 真載點(self,ctx):
        embed=discord.Embed(title="IT下載教學影片", url="https://www.youtube.com/watch?v=yGdkHlD5zVU", description="真．載點",  color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(baka(bot))        