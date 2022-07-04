import discord,asyncio,random
from discord.ext import commands
from core.classes import cog_all
import psutil
import discord_slash
from discord_slash import cog_ext

class botinfo(cog_all):
    @commands.command()
    async def a(self,ctx,member:discord.Member):
        a=str(member.avatar_url_as(format=".jpg"))
        await ctx.send(a)

    @cog_ext.cog_slash(name="avatar",description="取得某人頭貼")
    async def a(self,ctx,member:discord.Member):
        a=str(member.avatar_url_as(format=".jpg"))
        await ctx.send(a)


def setup(bot):
    bot.add_cog(botinfo(bot))