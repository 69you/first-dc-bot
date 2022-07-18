import discord
from discord.ext import commands
import json,datetime
from core.classes import cog_all
from discord.ext import commands

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class admin_unpin(cog_all):

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def unpin(self,ctx,msg):
        await ctx.message.delete()
        unpinmsg=await ctx.fetch_message(msg)
        await unpinmsg.unpin()
        await unpinmsg.reply("此訊息已解除釘選",mention_author=False)


def setup(bot):
    bot.add_cog(admin_unpin(bot))