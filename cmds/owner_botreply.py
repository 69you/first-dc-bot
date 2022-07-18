import discord 
from discord.ext import commands
from core.classes import cog_all
import json

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class owner_botreply(cog_all):

    @commands.command(aliases=["re"])
    async def reply(self,ctx,remes:int,tag,*,message):
        if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
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


def setup(bot):
    bot.add_cog(owner_botreply(bot))