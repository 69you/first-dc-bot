import discord
from discord.ext import commands
from core.classes import cog_all
import json , asyncio
from typing import Union

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class fun_ping(cog_all):
    @commands.command()
    async def ping(self,ctx):
        message=await ctx.send("🏓 Pinging...")
        await asyncio.sleep(1)
        await message.edit(content="延遲 "+f'{round(self.bot.latency*1000)} (ms)')


def setup(bot):
    bot.add_cog(fun_ping(bot))