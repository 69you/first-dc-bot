from lib2to3.pytree import convert
import discord
from discord.ext import commands
import json , asyncio, datetime
from core.classes import cog_all

class timereport(cog_all):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def onlinetime():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(977121281361182750)
            onlinetime=0
            while not self.bot.is_closed():
                await self.channel.send(f"沒忘記我吧,我已經上線了{onlinetime}分鐘")
                onlinetime+=900/60
                await asyncio.sleep(900) #sec
        self.testloop=self.bot.loop.create_task(onlinetime())

        async def test():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(977121281361182750)
            onlinetime=0
            while not self.bot.is_closed():
                await self.channel.send(f"沒忘記我吧,我已經上線了{onlinetime}分鐘")
                onlinetime+=900/60
                await asyncio.sleep(900) #sec
        self.testloop=self.bot.loop.create_task(test())        
    
    #for log online channel
    @commands.command()
    async def set_channel(self,ctx,channel:int):
        if ctx.author.id==878830839822176287:
            self.channel= self.bot.get_channel(channel)
            await ctx.send(f"set channel:{self.channel.mention}")
        else:
            await ctx.send("你以為你是 `侑介#4644` 嗎")
            await ctx.send("<a:691225128549482496:978100671020679168>")



def setup(bot):
    bot.add_cog(timereport(bot))