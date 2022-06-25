import discord
from discord.ext import commands
import asyncio,datetime,json
from core.classes import cog_all

class info(cog_all):
    @commands.command(aliases=["sf"])
    async def severinfo(self,ctx):
        guild=ctx.guild
        #await ctx.send(f"{guild.banner_url}")
        #await ctx.send(f"`伺服器名稱:` {guild.name}")
        #await ctx.send(f"`伺服器擁有人:`　{guild.owner}")
        #await ctx.send(f"`伺服器創建日期：`　{guild.created_at}")
        cha=0
        for i in guild.text_channels:
            cha+=1
        #await ctx.send(f"`文字頻道數量:` {cha}")
        vcha=0
        for i in guild.voice_channels:
            vcha+=1
        #await ctx.send(f"`語音頻道數量:` {vcha}")
        emoji=0
        for i in guild.emojis:
            emoji+=1
        #await ctx.send(f"`表情符號數量:` {emoji}")
        #await ctx.send(str(guild.icon_url))
        role=0
        for i in guild.roles:
            role+=1
        #await ctx.send(f"`身分組數量:` {role}")
        #await ctx.send(bool(guild.large))
        member=0
        for i in guild.members:
            if i.bot==False:
                member+=1
        #await ctx.send(f"`伺服器人數:` {member}")
        bot=0
        for i in guild.members:
            if i.bot==True:
                bot+=1
        #await ctx.send(f"`機器人數量:` {member}")
        #await ctx.send(guild.splash_url)邀請背景
        #await ctx.send(f"`加成等級:` {guild.premium_tier}")
        #await ctx.send(f"`加成數量:` {guild.premium_subscription_count}")
        boost=""
        for i in guild.premium_subscribers:
            boost+="`"+i.name+"#"+i.discriminator+"` "
        #await ctx.send(f"`加成人員:` {boost}")


def setup(bot):
    bot.add_cog(info(bot))