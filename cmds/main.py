import discord
from discord.ext import commands
from core.classes import cog_all

class load(cog_all):
    @commands.command()
    async def load(self,ctx,extension):
        self.bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'loaded {extension}')

class unload(cog_all):
    @commands.command()
    async def unload(self,ctx,extension):
        self.bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'unloaded {extension}')

class reload(cog_all):
    @commands.command()
    async def reload(self,ctx,extension):
        self.bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'reloaded {extension}')

def setup(bot):
    bot.add_cog(load(bot))
    bot.add_cog(unload(bot))
    bot.add_cog(reload(bot))