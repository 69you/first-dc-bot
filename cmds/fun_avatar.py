import discord
from discord.ext import commands
from core.classes import cog_all
import json , datetime , asyncio

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class fun_avatar(cog_all):

    @commands.command(aliases=["av"])
    async def avatar(self,ctx,member: discord.Member = None):
        if member==None:
            member=ctx.author             
        link = str(member.avatar_url_as(format="png"))
        await ctx.message.delete()
        embed=discord.Embed(title=f"{member}  的頭貼",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_image(url = f"{link}")
        a=await ctx.send(embed=embed)
        b=await ctx.send("十秒後刪除")
        await asyncio.sleep(10)
        await a.delete()
        await b.delete()  


def setup(bot):
    bot.add_cog(fun_avatar(bot))