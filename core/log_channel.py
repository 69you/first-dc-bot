from turtle import title
import discord
from discord.ext import commands,tasks
import asyncio,os,random,datetime
from core.classes import cog_all

class log_channel(cog_all):#944855324706344980s

    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel):
        ch=await self.bot.fetch_channel(995701316376612954)
        await ch.send(f"{channel.mention} has been created")
    
    @commands.Cog.listener()
    async def on_private_channel_create(self,channel):
        ch=await self.bot.fetch_channel(995701316376612954)
        await ch.send(f"{channel.mention} has been created")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self,channel):
        ch=await self.bot.fetch_channel(995701316376612954)
        await ch.send(f"{channel} has been deleted")

    @commands.Cog.listener()
    async def on_private_channel_create(self,channel):
        ch=await self.bot.fetch_channel(995701316376612954)
        await ch.send(f"{channel.mention} has been deleted")

    @commands.Cog.listener()
    async def on_guild_channel_update(self,before,after):
        ch=await self.bot.fetch_channel(995701316376612954)
        if before.name != after.name:
            await ch.send(f"a channel name has been update\n``before:`` {before.name}\n``after:`` {after.name}")
        elif before.position != after.position:
            await ch.send(f"{after.mention}'s position has been updated\n``before:`` {before.position}\n``after:`` {after.position}")
        elif before.category.name != after.category.name:
            await ch.send(f"{after.mention}'s category has been changed\n``before:`` {before.category.name}\n``after:`` {after.category.name}")
        elif before.permissions_synced != after.permissions_synced:
            if before.permissions_synced==True:
                await ch.send(f"{before.mention}'s permissions_synced has changed\n``before:`` {before.permissions_synced}\n``after:`` {after.permissions_synced}")
            elif before.permissions_synced==False:
                await ch.send(f"{before.mention}'s permissions_synced has changed\n``before:`` {before.permissions_synced}\n``after:`` {after.permissions_synced}")        

#on_guild_channel_pins_update


def setup(bot):
    bot.add_cog(log_channel(bot))