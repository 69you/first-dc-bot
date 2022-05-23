import discord
from discord.ext import commands
from core.classes import cog_all
import json

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


class backevent(cog_all):
    @commands.Cog.listener() 
    async def on_member_join(self,member):
        channel=self.bot.get_channel(977121281361182750)
        await channel.send(f'{member} has join')

    @commands.Cog.listener() 
    async def on_member_remove(self,member):
        channel=self.bot.get_channel(977121281361182750)
        await channel.send(f'{member} has leave ')

class load(cog_all):
    @commands.command()
    async def load(self,ctx,extension):
        if ctx.author.id == 878830839822176287:
            self.bot.load_extension(f'cmds.{extension}')            
            await ctx.send(f'loaded {extension}')
        else :
            await ctx.send("你是侑介#4644 嗎")
            await ctx.send("<a:691225128549482496:978100671020679168>")

class unload(cog_all):
    @commands.command()
    async def unload(self,ctx,extension):
        if ctx.author.id == 878830839822176287:
            self.bot.unload_extension(f'cmds.{extension}')
            await ctx.send(f'unloaded {extension}')
        else :
            await ctx.send("你是侑介#4644 嗎")
            await ctx.send("<a:691225128549482496:978100671020679168>")

class reload(cog_all):
    @commands.command()
    async def reload(self,ctx,extension):
        if ctx.author.id == 878830839822176287:
            self.bot.reload_extension(f'cmds.{extension}')
            await ctx.send(f'reloaded {extension}')
        else:
            await ctx.send("你是侑介#4644 嗎")
            await ctx.send("<a:691225128549482496:978100671020679168>")

def setup(bot):
    bot.add_cog(backevent(bot))
    bot.add_cog(load(bot))
    bot.add_cog(unload(bot))
    bot.add_cog(reload(bot))