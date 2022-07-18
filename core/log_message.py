import discord
from discord.ext import commands,tasks
import asyncio,os,random,datetime
from core.classes import cog_all


class log_msg(cog_all):

    @commands.Cog.listener()
    async def on_message_delete(self,msg):
        embed=discord.Embed(title=f"{msg.author} 刪除了訊息", description=f"刪除位置: {msg.channel.mention}",color=discord.Colour.from_rgb(231,76,60))
        embed.set_author(name=f"{msg.author}",icon_url=f"{msg.author.avatar_url}")
        embed.add_field(name=f"**刪除內容:    **{msg.content}",value="** **",inline=True)
        time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
        embed.set_footer(text=f"{time} ,id={msg.author.id}")
        ch=await self.bot.fetch_channel(996340297497853992)
        await ch.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self,before,after):
        embed=discord.Embed(title=f"{before.author} 編輯了訊息", description=f"編輯位置: {before.channel.mention}",color=discord.Colour.from_rgb(231,76,60))
        embed.set_author(name=f"{before.author}",icon_url=f"{before.author.avatar_url}")
        embed.add_field(name=f"**編輯前:   **{before.content}",value="** **",inline=False)
        embed.add_field(name=f"**編輯後:   **{after.content}",value=f"[傳送們]({after.jump_url})",inline=False)       
        time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
        embed.set_footer(text=f"{time} ,id={before.author.id}")
        ch=await self.bot.fetch_channel(996340297497853992)
        await ch.send(embed=embed)
    
    




def setup(bot):
    bot.add_cog(log_msg(bot))