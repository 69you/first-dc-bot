import discord
from discord.ext import commands
import json,datetime
from core.classes import cog_all
from discord.ext import commands

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class admin_clear(cog_all):
    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self,ctx,deletenum :int):
        await ctx.channel.purge(limit= deletenum+1)
        embed=discord.Embed(title="管管們爆怒", description=f"導致 {deletenum} 條訊息被 {ctx.author.name} 吃掉了", color=0xfd12ca, timestamp= datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(admin_clear(bot))