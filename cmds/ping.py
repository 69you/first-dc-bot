import discord
from discord.ext import commands
from core.classes import cog_all

class ping(cog_all):
    @commands.command()
    async def ping(self,ctx):
        await ctx.send("延遲 "+f'{round(self.bot.latency*1000)} (ms)')

def setup(bot):
    bot.add_cog(ping(bot))