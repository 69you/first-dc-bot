import discord
from discord.ext import commands
import json,datetime
from core.classes import cog_all
from discord.ext import commands
with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class manage(cog_all):
    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self,ctx,deletenum :int):
        await ctx.channel.purge(limit= deletenum+1)
        embed=discord.Embed(title="管管們爆怒", description=f"導致 {deletenum} 條訊息被 {ctx.author.name} 吃掉了", color=0xfd12ca, timestamp= datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member,*,reason="未指定"):
        await member.kick()
        embed=discord.Embed(title=f"{member} 已被{ctx.author} 踢出伺服器", description=f"原因 : {reason}", color=0xfd12ca, timestamp= datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_author(name="<==被踢的人", icon_url=f"{member.avatar_url}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member,*,reason="未指定"):
        await member.ban(delete_message_days=0)
        embed=discord.Embed(title=f"{member} 已被{ctx.author} 停權", description=f"原因 : {reason}", color=0xfd12ca, timestamp= datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_author(name="<==被停權的人", icon_url=f"{member.avatar_url}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self,ctx,member:int):
        user = await self.bot.fetch_user(member)
        await ctx.guild.unban(user)
        embed=discord.Embed(title=f"{user} 已被 {ctx.author} 解除停權", description=" ", color=0xfd12ca,timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_author(name=f"{user}", icon_url=f"{user.avatar_url}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def pin(self,ctx,msg):
        await ctx.message.delete()
        pinmssg=await ctx.fetch_message(msg)
        await pinmssg.pin()
        await pinmssg.reply("此訊息已釘選",mention_author=False)
    
    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def unpin(self,ctx,msg):
        await ctx.message.delete()
        unpinmsg=await ctx.fetch_message(msg)
        await unpinmsg.unpin()
        await unpinmsg.reply("此訊息已解除釘選",mention_author=False)


def setup(bot):
    bot.add_cog(manage(bot))