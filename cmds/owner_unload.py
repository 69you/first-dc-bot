import discord
from discord.ext import commands
from core.classes import cog_all
import json

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class owner_unload(cog_all):
    @commands.command()
    async def unload(self,ctx,extension):
        if ctx.author.id == (int(jdata["yuusuke id"])):
            self.bot.unload_extension(f'cmds.{extension}')
            await ctx.send(f'unloaded {extension}')
        else :
            await ctx.send(jdata["are u yuusuke"])
            await ctx.send(jdata["ars hit"])


def setup(bot):
    bot.add_cog(owner_unload(bot))