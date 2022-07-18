import discord
from discord.ext import commands
from core.classes import cog_all
import json

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class owner_load(cog_all):
    @commands.command()
    async def load(self,ctx,extension):
        if ctx.author.id == (int(jdata["yuusuke id"])):
            self.bot.load_extension(f'cmds.{extension}')            
            await ctx.send(f'loaded {extension}')
        else :
            await ctx.send(jdata["are u yuusuke"])
            await ctx.send("ars hit")


def setup(bot):
    bot.add_cog(owner_load(bot))