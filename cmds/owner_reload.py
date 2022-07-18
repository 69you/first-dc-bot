import discord
from discord.ext import commands
from core.classes import cog_all
import json

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class reload(cog_all):
    @commands.command()
    async def reload(self,ctx,extension):
        if ctx.author.id == (int(jdata["yuusuke id"])):
            self.bot.reload_extension(f'cmds.{extension}')
            await ctx.send(f'reloaded {extension}')
        else:
            await ctx.send(jdata["are u yuusuke"])
            await ctx.send(jdata["ars hit"])


def setup(bot):
    bot.add_cog(reload(bot))