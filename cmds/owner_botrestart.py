import discord
from discord.ext import commands
from core.classes import cog_all
import datetime ,os,sys

class owner_botrestart(cog_all):

    @commands.command()
    async def restart(self,ctx):
        def restart_bot(): 
            os.execv(sys.executable, ['python'] + sys.argv)
        if ctx.author.id==878830839822176287:
            a=await ctx.send("<a:715586639623356438:989524987696254996> Restarting Bot...")
            await restart_bot()
            embed=discord.Embed(title="✅ Bot Has Been Restart",description=" ",color=0xfd12ca,timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            await a.reply(embed=embed)  

def setup(bot):
    bot.add_cog(owner_botrestart(bot))