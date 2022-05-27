import discord
from discord.ext import commands
import datetime , asyncio
from core.classes import cog_all


class timereport(cog_all):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def time_task():
            await self.bot.wait_until_reaady()
            self.channel=self.bot.get_channel(977121281361182750)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now().strftime("%H%M")   
                if now_time == "0958":
                    await self.channel.send("check")
                    await asyncio.sleep(1)
                else:
                    asyncio.sleep(1)
                    pass      

        self.bg_task =self.bot.loop.create_task(time_task())     


def setup(bot):
    bot.add_cog(timereport(bot))        