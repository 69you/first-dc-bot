import discord
from discord.ext import commands
import json,datetime
from core.classes import cog_all
with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class manage(cog_all):
    @commands.command()
    async def clear(self,ctx,deletenum :int):
        if  ctx.author.id == (int(jdata["誠 id"])) or ctx.author.id == (int(jdata["小飄 id"])) or ctx.author.id == (int(jdata["小小飄 id"])) or ctx.author.id == (int(jdata["煋夜 id"])) or ctx.author.id == (int(jdata["死神 id"])) or ctx.author.id == (int(jdata["小魚 id"]))  or ctx.author.id == (int(jdata["四季 id"])) or  ctx.author.id == (int(jdata["白日夢 id"])):
            await ctx.channel.purge(limit= deletenum+1)
            embed=discord.Embed(title="管管們爆怒", description=f"導致 {deletenum} 條訊息被 {ctx.author.name} 吃掉了", color=0xfd12ca, timestamp= datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            await ctx.send(embed=embed)
        elif ctx.author.id == (int(jdata["yuusuke id"])):
            await ctx.channel.purge(limit= deletenum+1)
        else:
            await ctx.message.delete()
            await ctx.send("你以為你是 `侑介#4644` 或是管管嗎")
            await ctx.send(jdata["ars hit"])


def setup(bot):
    bot.add_cog(manage(bot))