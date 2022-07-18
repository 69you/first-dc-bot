import discord
from discord.ext import commands
import json,datetime
from core.classes import cog_all
from discord.ext import commands

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class admin_unban(cog_all):

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self,ctx,member:int):
        user = await self.bot.fetch_user(member)
        await ctx.guild.unban(user)
        embed=discord.Embed(title=f"{user} 已被 {ctx.author} 解除停權", description=" ", color=0xfd12ca,timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_author(name=f"{user}", icon_url=f"{user.avatar_url}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(admin_unban(bot))