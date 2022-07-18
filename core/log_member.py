import discord
from discord.ext import commands,tasks
import asyncio,os,random,datetime
from core.classes import cog_all

class log_member(cog_all):

    @commands.Cog.listener()
    async def on_member_join(self,member):
        embed=discord.Embed(title="一個新成員加入伺服器",color=discord.Colour.from_rgb(46,204,113), timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name=f"{member}",value=f"id= {member.id}")
        ch=await self.bot.fetch_channel(996340297497853992)
        await ch.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        embed=discord.Embed(title="一個成員離開伺服器",color=discord.Colour.from_rgb(46,204,113), timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name=f"{member}",value=f"id= {member.id}")
        ch=await self.bot.fetch_channel(996340297497853992)
        await ch.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self,guild,member):
        embed=discord.Embed(title="一個成員被停權",color=discord.Colour.from_rgb(46,204,113), timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name=f"{member}",value=f"id= {member.id}")
        ch=await self.bot.fetch_channel(996340297497853992)
        await ch.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self,guild,member):
        embed=discord.Embed(title="一個成員被解除停權",color=discord.Colour.from_rgb(46,204,113), timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name=f"{member}",value=f"id= {member.id}")
        ch=await self.bot.fetch_channel(996340297497853992)
        await ch.send(embed=embed)

    #@commands.Cog.listener()
    #async def on_member_update(self,before,after):
        

    
#on_member_update
#on_user_update


def setup(bot):
    bot.add_cog(log_member(bot))
