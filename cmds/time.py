from lib2to3.pytree import convert
import discord
from discord.ext import commands
import json , asyncio, datetime
from core.classes import cog_all

class timereport(cog_all):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        async def test():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(977121281361182750)
            onlinetime=0
            while not self.bot.is_closed():
                await self.channel.send(f"沒忘記我吧,我已經上線了{onlinetime}分鐘")
                onlinetime+=900/60
                await asyncio.sleep(900) #sec
        self.testloop=self.bot.loop.create_task(test())

    @commands.command()
    async def set_channel(self,ctx,channel:int):
        self.channel= self.bot.get_channel(channel)
        await ctx.send(f"set channel:{self.channel.mention}")


def setup(bot):
    bot.add_cog(timereport(bot))