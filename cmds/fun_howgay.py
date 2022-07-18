import discord
from discord.ext import commands
from core.classes import cog_all
import json , datetime , random

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class fun_howgay(cog_all):

    @commands.command()
    async def howgay(self,ctx,member: discord.Member = None):
        random_num=random.randint(1,100)
        if member==None:
            member=ctx.author          
        if random_num>50:
            embed=discord.Embed(title=" ",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_author(name=" 假假計算器", icon_url=f"{member.avatar_url}")
            embed.add_field(name=member.display_name+f" 是{random_num}% 的假🌈🌈", value="看來果然如此", inline=False)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=" ",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_author(name=" 假假計算器", icon_url=f"{member.avatar_url}")
            embed.add_field(name=member.display_name+f" 是{random_num}% 的假🌈", value="我應該算錯了", inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun_howgay(bot))