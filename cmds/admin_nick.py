import discord
from discord.ext import commands
import json,datetime
from core.classes import cog_all
from discord.ext import commands

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class admin_nick(cog_all):

    @commands.command()
    @commands.has_guild_permissions(manage_nicknames=True)
    async def nick(self,ctx, member:discord.Member, nick=None):
        if nick==None:
                name=member.display_name
                await ctx.message.delete()
                await member.edit(nick=member.name)
                embed=discord.Embed(title=f"{member} 的暱稱已經更改",description=f"前: `{name}` ,後: `{member.name}` ", color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
                await ctx.send(embed=embed)            
        else:
            name=member.display_name
            if name=="None":
                await ctx.message.delete()
                await member.edit(nick=nick)
                embed=discord.Embed(title=f"{member} 的暱稱已經更改",description=f"前: `{member.name}` ,後: `{nick}` ", color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
                await ctx.send(embed=embed)
            else:
                await ctx.message.delete()
                await member.edit(nick=nick)
                embed=discord.Embed(title=f"{member} 的暱稱已經更改",description=f"前: `{name}` ,後: `{nick}` ", color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(admin_nick(bot))