import discord
from discord.ext import commands
from core.classes import cog_all
import json , datetime , asyncio

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class fun_banner(cog_all):
    @commands.command()
    async def banner(self,ctx, member:discord.Member=None):
        if member == None:
            member = ctx.author
        if member.banner==None:
            embed=discord.Embed(title=f"{member} 的橫幅",description=" ", color=0xfd12ca,timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_image(url=f"{str(member.banner)}")
            a=await ctx.send(embed=embed)
            b=await ctx.send("十秒鐘後刪除")
            await asyncio.sleep(10)
            await a.delete()
            await b.delete()
        else:
            await ctx.reply("該使用者無橫幅")


def setup(bot):
    bot.add_cog(fun_banner(bot))