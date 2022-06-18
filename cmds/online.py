import discord
from discord.ext import commands
import json , asyncio
from core.classes import cog_all

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


class onlinereport(cog_all):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def onlinetime():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(977121281361182750)
            onlinetime=0
            while not self.bot.is_closed():
                await self.channel.send(f"沒忘記我吧,我已經上線了{onlinetime}小時")
                onlinetime+=1
                await asyncio.sleep(3600) #sec
        self.testloop=self.bot.loop.create_task(onlinetime())

def setup(bot):
    bot.add_cog(onlinereport(bot))


'''
#for log online time channel
@commands.command()
async def set_channel(self,ctx,channel:int):
    if ctx.author.id== (int(jdata["yuusuke id"])):
        self.channel= self.bot.get_channel(channel)
        await ctx.send(f"set channel:{self.channel.mention}")
    else:
        await ctx.send("你以為你是 `侑介#4644` 嗎")
        await ctx.send("<a:691225128549482496:978100671020679168>")'''
