import discord 
from discord.ext import commands
from core.classes import cog_all
from typing import Union
import json,os,sys,datetime

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class botreaction(cog_all):
    @commands.command()
    async def dm(self,ctx,member:discord.Member,*,message):
        if ctx.author.id==878830839822176287:
            await member.send(message)
            await ctx.message.add_reaction("✅")
            await ctx.message.delete()

    @commands.command(aliases=["re"])
    async def reply(self,ctx,remes:int,tag,*,message):
        if ctx.author.id==878830839822176287:
            keyword1=["t","true","True","1","o"]
            keyword2=["f","false","False","0","x"]
            for key1 in keyword1:
                if tag==key1:
                    await ctx.message.delete()
                    msg = await ctx.fetch_message(remes)
                    await msg.reply(message,mention_author=True)
                    break
            for key2 in keyword2:
                if tag==key2:
                    await ctx.message.delete()
                    msg = await ctx.fetch_message(remes)
                    await msg.reply(message,mention_author=False)       
                    break  
        else:
            await ctx.message.delete() 

    @commands.command(aliases=["ed"])
    async def edit(self,ctx,msgid:int,*,message):
        if ctx.author.id==878830839822176287:
            await ctx.message.delete()
            msg=await ctx.fetch_message(msgid)
            await msg.edit(content=message)
        else:
            await ctx.message.delete()

    @commands.command()
    async def add(self,ctx,remes:int,emoji:Union[discord.Emoji, discord.PartialEmoji]):
        if ctx.author.id==878830839822176287:
            await ctx.message.delete()
            msg = await ctx.fetch_message(remes)
            await msg.add_reaction(emoji)

    @commands.command(aliases=["s"])
    async def sayd(self,ctx, *,msg):
        if ctx.author.id == (int(jdata["yuusuke id"])):
            await ctx.message.delete()
            await ctx.send(msg)
        else :
            await ctx.message.delete()
    
    @commands.command(aliases=["st"])
    async def status(self,ctx,status,kind,*,name,url=None):
        if ctx.author.id==(int(jdata["yuusuke id"])):
            if status=="dnd":
                if kind=="game":
                    await self.bot.change_presence(activity=discord.Game(name=f"{name}"),status=discord.Status.dnd)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
                elif kind=="streaming" or kind=="stream":
                    await self.bot.change_presence(activity=discord.Streaming(name=f"{name}",url=(f"{url}")),status=discord.Status.dnd)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
                elif kind=="listing" or kind=="lis":
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{name}"),status=discord.Status.dnd)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
                elif kind=="watching" or kind=="watch":
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{name}"),status=discord.Status.dnd)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
            elif status=="idle":
                if kind=="game":
                    await self.bot.change_presence(activity=discord.Game(name=f"{name}"),status=discord.Status.idle)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
                elif kind=="streaming" or kind=="stream":
                    await self.bot.change_presence(activity=discord.Streaming(name=f"{name}",url=(f"{url}")),status=discord.Status.idle)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
                elif kind=="listing" or kind=="lis":
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{name}"),status=discord.Status.idle)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
                elif kind=="watching" or kind=="watch":
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{name}"),status=discord.Status.idle)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
            elif status=="on":
                if kind=="game":
                    await self.bot.change_presence(activity=discord.Game(name=f"{name}"),status=discord.Status.online)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
                elif kind=="streaming" or kind=="stream":
                    await self.bot.change_presence(activity=discord.Streaming(name=f"{name}",url=(f"{url}")),status=discord.Status.online)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
                elif kind=="listing" or kind=="lis":
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{name}"),status=discord.Status.online)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
                elif kind=="watching" or kind=="watch":
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{name}"),status=discord.Status.online)
                    embed=discord.Embed(title="✅ Changing Status Complted!",description=" ",color=0xfd12ca)
                    await ctx.send(embed=embed)
                    
    @commands.command()
    async def restart(self,ctx):
        def restart_bot(): 
            os.execv(sys.executable, ['python'] + sys.argv)
        if ctx.author.id==878830839822176287:
            a=await ctx.send("<a:715586639623356438:989524987696254996> Restarting Bot...")
            await restart_bot()
            embed=discord.Embed(title="✅ Bot Has Been Restart",description=" ",color=0xfd12ca,timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            await a.reply(embed=embed)    


              


def setup(bot):
    bot.add_cog(botreaction(bot))