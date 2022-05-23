import discord
from discord.ext import commands
from core.classes import cog_all
import json
import datetime

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
            await ctx.send("你是`侑介#4644` 嗎")
            await ctx.send("<a:691225128549482496:978100671020679168>")

class unload(cog_all):
    @commands.command()
    async def unload(self,ctx,extension):
        if ctx.author.id == 878830839822176287:
            self.bot.unload_extension(f'cmds.{extension}')
            await ctx.send(f'unloaded {extension}')
        else :
            await ctx.send("你是`侑介#4644` 嗎")
            await ctx.send("<a:691225128549482496:978100671020679168>")

class reload(cog_all):
    @commands.command()
    async def reload(self,ctx,extension):
        if ctx.author.id == 878830839822176287:
            self.bot.reload_extension(f'cmds.{extension}')
            await ctx.send(f'reloaded {extension}')
        else:
            await ctx.send("你是`侑介#4644` 嗎")
            await ctx.send("<a:691225128549482496:978100671020679168>")

class fun(cog_all):
    @commands.command()
    async def sayd(self,ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clear(self,ctx,deletenum :int):
        if ctx.author.id == 869025114862284810 or ctx.author.id == 647775766838378496 or ctx.author.id == 942632954935541800 or ctx.author.id == 927834871857033267 or ctx.author.id == 878830839822176287 or ctx.author.id == 883559220803436574 or ctx.author.id == 711241728375652353 or ctx.author.id == 571295524158963712 or ctx.author.id == 935414869648351313 or ctx.author.id == 860280256208437258 or ctx.author.id ==880009654061645824:
            await ctx.channel.purge(limit= deletenum+1)
            embed=discord.Embed(title="管管們爆怒", description=f"導致{deletenum}被吃掉了", color=0xfd12ca, timestamp= datetime.datetime.utcnow())
            msg = await ctx.send(embed=embed)
        else:
            await ctx.send("你以為你是 `侑介#4644` 或是管管嗎")
            await ctx.send("<a:691225128549482496:978100671020679168>")

def setup(bot):
    bot.add_cog(backevent(bot))
    bot.add_cog(load(bot))
    bot.add_cog(unload(bot))
    bot.add_cog(reload(bot))
    bot.add_cog(fun(bot))