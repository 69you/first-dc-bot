from ast import keyword
import string
import discord
from discord.ext import commands
from core.classes import cog_all
import json , datetime

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


class backevent(cog_all):
    @commands.Cog.listener() 
    async def on_member_join(self,member):
        channel=self.bot.get_channel(977121281361182750)
        await channel.send(f'{member.mention} has join `{member.guild}`')

    @commands.Cog.listener() 
    async def on_member_remove(self,member):
        channel=self.bot.get_channel(977121281361182750)
        await channel.send(f'{member.mention} has leave `{member.guild}`')

class load(cog_all):
    @commands.command()
    async def load(self,ctx,extension):
        if ctx.author.id == (int(jdata["yuusuke id"])):
            self.bot.load_extension(f'cmds.{extension}')            
            await ctx.send(f'loaded {extension}')
        else :
            await ctx.send(jdata["are u yuusuke"])
            await ctx.send("ars hit")

class unload(cog_all):
    @commands.command()
    async def unload(self,ctx,extension):
        if ctx.author.id == (int(jdata["yuusuke id"])):
            self.bot.unload_extension(f'cmds.{extension}')
            await ctx.send(f'unloaded {extension}')
        else :
            await ctx.send(jdata["are u yuusuke"])
            await ctx.send(jdata["ars hit"])

class reload(cog_all):
    @commands.command()
    async def reload(self,ctx,extension):
        if ctx.author.id == (int(jdata["yuusuke id"])):
            self.bot.reload_extension(f'cmds.{extension}')
            await ctx.send(f'reloaded {extension}')
        else:
            await ctx.send(jdata["are u yuusuke"])
            await ctx.send(jdata["ars hit"])

class fun(cog_all):
    @commands.command()
    async def sayd(self,ctx, *,msg):
        if ctx.author.id == (int(jdata["yuusuke id"])) or ctx.author.id == (int(jdata["煋夜 id"])):
            await ctx.message.delete()
            await ctx.send(msg)

    @commands.command()
    async def clear(self,ctx,deletenum :int):
        if ctx.author.id == (int(jdata["yuusuke id"])) or ctx.author.id == (int(jdata["誠 id"])) or ctx.author.id == (int(jdata["小飄 id"])) or ctx.author.id == (int(jdata["小小飄 id"])) or ctx.author.id == (int(jdata["煋夜 id"])) or ctx.author.id == (int(jdata["死神 id"])) or ctx.author.id == (int(jdata["小魚 id"])) or ctx.author.id == (int(jdata["昆布 id"])) or ctx.author.id == (int(jdata["四季 id"])) or ctx.author.id == (int(jdata["夏旪 id"])) or ctx.author.id == (int(jdata["白日夢 id"])):
            await ctx.channel.purge(limit= deletenum+1)
            embed=discord.Embed(title="管管們爆怒", description=f"導致 {deletenum} 條訊息被 {ctx.author.name} 吃掉了", color=0xfd12ca, timestamp= datetime.datetime.utcnow())
            msg = await ctx.send(embed=embed)
        else:
            await ctx.send("你以為你是 `侑介#4644` 或是管管嗎")
            await ctx.send(jdata["ars hit"])

class help(cog_all):
    @commands.command()
    async def help(self,ctx):
        #await ctx.message.delete()
        embed=discord.Embed(title="侑介のbot", url="http://yt1.piee.pw/46vhku", description="由侑介#4644所開發的人工智障", color=0xfd12ca, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="<==這是侑介", icon_url="https://cdn.discordapp.com/avatars/878830839822176287/e947993f71d34bd423b0a24e166ccf42.png?size=4096")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/977086056967053353/ebc17adf1bc26fe27571586430b56ae8.png?size=4096")
        await ctx.send(embed=embed) 

def setup(bot):
    bot.add_cog(backevent(bot))
    bot.add_cog(load(bot))
    bot.add_cog(unload(bot))
    bot.add_cog(reload(bot))
    bot.add_cog(fun(bot))
    bot.add_cog(help(bot))