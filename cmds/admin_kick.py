import discord
from discord.ext import commands
import json,datetime
from core.classes import cog_all
from discord.ext import commands

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class admin_kick(cog_all):
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member,*,reason="未指定"):
        await member.kick()
        embed=discord.Embed(title=f"{member} 已被{ctx.author} 踢出伺服器", description=f"原因 : {reason}", color=0xfd12ca, timestamp= datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_author(name="<==被踢的人", icon_url=f"{member.avatar_url}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(admin_kick(bot))