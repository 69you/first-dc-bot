import discord 
from discord.ext import commands
from core.classes import cog_all
from typing import Union
import json

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


class dm(cog_all):
    @commands.command()
    async def dm(self,ctx,member:discord.Member,*,message):
        #if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
            await member.send(message)
            await ctx.message.add_reaction("✅")
            await ctx.message.delete()
        #else:
        #    await ctx.message.delete()

class sayd(cog_all):
    @commands.command(aliases=["s"])
    async def sayd(self,ctx, *,msg=None):
        if msg==None:
            msg="** **"
        #if ctx.author.id == (int(jdata["yuusuke id"])) or ctx.author.id==915809531865477180:
            await ctx.message.delete()
            await ctx.send(msg)
        #else :
        #    await ctx.message.delete()

class reply(cog_all):
    @commands.command(aliases=["re"])
    async def reply(self,ctx,remes:int,tag,*,message):
        #if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
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
        #else:
        #    await ctx.message.delete() 

class edit(cog_all):
    @commands.command(aliases=["ed"])
    async def edit(self,ctx,msgid:int,*,message):
        #if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
            await ctx.message.delete()
            msg=await ctx.fetch_message(msgid)
            await msg.edit(content=message)
        #else:
        #    await ctx.message.delete()

class addemoji(cog_all):
    @commands.command()
    async def add(self,ctx,remes:int,emoji:Union[discord.Emoji, discord.PartialEmoji]):
        #if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
            await ctx.message.delete()
            msg = await ctx.fetch_message(remes)
            await msg.add_reaction(emoji)
        #else:
        #    await ctx.message.delete()
    
    @commands.command()
    async def defemoji(self,ctx,msg,emoji):
        #if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
            await ctx.message.delete()
            msg = await ctx.fetch_message(msg)
            await msg.add_reaction(emoji)
        #else:
        #    await ctx.message.delete()


def setup(bot):
    bot.add_cog(dm(bot))
    bot.add_cog(sayd(bot))
    bot.add_cog(reply(bot))
    bot.add_cog(edit(bot))
    bot.add_cog(addemoji(bot))