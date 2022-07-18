import py_compile
import discord 
from discord.ext import commands
from core.classes import cog_all
import json,asyncio

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class owner_leaveguild(cog_all):

    @commands.command()
    async def leaveg(self,ctx, id,time:int,reason=None):
        if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
            if reason==None:
                reason="問就是沒有"
            await ctx.message.delete()
            await ctx.send(f"距離離開此伺服器尚有{time} 秒\n原因: {reason}")
            await asyncio.sleep(time)
            await ctx.send("再見")
            guild = await self.bot.fetch_guild(id)
            await guild.leave()
            channel=await self.bot.fetch_channel(996340297497853992)
            await channel.send(f"i have left {guild}")
        else:
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(owner_leaveguild(bot))