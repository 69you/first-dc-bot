import string
import discord
from discord.ext import commands
from core.classes import cog_all
import json , datetime , random, asyncio,os,sys

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

class help(cog_all):
    @commands.command()
    async def help(self,ctx):
        #await ctx.message.delete()
        embed=discord.Embed(title="侑介のbot", url="http://yt1.piee.pw/46vhku", description="由侑介#4644所開發的人工智障", color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_author(name="<==這是侑介", icon_url="https://cdn.discordapp.com/avatars/878830839822176287/e16a95f995ec014da521105e80a9de83.png?size=4096")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/977086056967053353/ebc17adf1bc26fe27571586430b56ae8.png?size=4096")
        await ctx.send(embed=embed) 

class helpful(cog_all):
    @commands.command()
    async def restart(self,ctx):
        def restart_bot(): 
            os.execv(sys.executable, ['python'] + sys.argv)
        if ctx.author.id==878830839822176287:
            a=await ctx.send("<a:715586639623356438:989524987696254996> Restarting Bot...")
            await restart_bot()
            embed=discord.Embed(title="✅ Bot Has Been Restart",description=" ",color=0xfd12ca,timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            await a.reply(embed=embed)  

    @commands.command()
    async def print(self,ctx):
      if ctx.author.id==(int(jdata["yuusuke id"])):
          for filename in os.listdir('./cmds'):
              if filename.endswith(".py"):
                  await ctx.send(f'cmds.{filename}')
      else: ctx.message.delete()
        

def setup(bot):
    bot.add_cog(backevent(bot))
    bot.add_cog(load(bot))
    bot.add_cog(unload(bot))
    bot.add_cog(reload(bot))
    bot.add_cog(help(bot))
    bot.add_cog(helpful(bot))