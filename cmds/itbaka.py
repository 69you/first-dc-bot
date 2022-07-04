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
    async def nova載點(self,ctx):
        embed=discord.Embed(title="NOVA載點", url="https://drive.google.com/file/d/1wPZ0VoT9hMPlyYqjG-G7FkUPY11OHeQh/view?usp=sharing", description="自己下載吧",  color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)

    @commands.command()
    async def NOVA載點(self,ctx):
        embed=discord.Embed(title="NOVA下載教學影片", url="http://surl.li/cineu", description="自己研究吧",  color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)

    @commands.command()
    async def tbd載點(self,ctx):
        embed=discord.Embed(title="tbd載點", url="https://drive.google.com/file/d/1wZplkwG8Lcd4QJLhJdhe7k94Ml84qsEh/view?usp=sharing", description="自己下載吧",  color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)

    @commands.command()
    async def TBD載點(self,ctx):
        embed=discord.Embed(title="tbd下載教學影片", url="http://surl.li/cineu", description="自己研究吧",  color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(baka(bot))        