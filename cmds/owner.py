import discord
from discord.ext import commands
from core.classes import cog_all
import datetime ,os,sys,json,asyncio

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class load(cog_all):
    @commands.command()
    async def load(self,ctx,extension):
        if ctx.author.id == (int(jdata["yuusuke id"])):
            self.bot.load_extension(f'cmds.{extension}')            
            await ctx.send(f'loaded {extension}')
        else :
            await ctx.send(jdata["are u yuusuke"])
            await ctx.send("ars hit")

class reload(cog_all):
    @commands.command()
    async def reload(self,ctx,extension):
        if ctx.author.id == (int(jdata["yuusuke id"])):
            self.bot.reload_extension(f'cmds.{extension}')
            await ctx.send(f'reloaded {extension}')
        else:
            await ctx.send(jdata["are u yuusuke"])
            await ctx.send(jdata["ars hit"])

class unload(cog_all):
    @commands.command()
    async def unload(self,ctx,extension):
        if ctx.author.id == (int(jdata["yuusuke id"])):
            self.bot.unload_extension(f'cmds.{extension}')
            await ctx.send(f'unloaded {extension}')
        else :
            await ctx.send(jdata["are u yuusuke"])
            await ctx.send(jdata["ars hit"])

class restart(cog_all):
    @commands.command()
    async def restart(self,ctx):
        def restart_bot(): 
            os.execv(sys.executable, ['python'] + sys.argv)
        if ctx.author.id==878830839822176287:
            a=await ctx.send("<a:715586639623356438:989524987696254996> Restarting Bot...")
            await restart_bot()
            embed=discord.Embed(title="✅ Bot Has Been Restart",description=" ",color=0xfd12ca,timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            await a.reply(embed=embed) 



class leaveguild(cog_all):
    @commands.command()
    async def leaveg(self,ctx, id,time:int,reason=None):
        if ctx.author.id==878830839822176287 or ctx.author.id==915809531865477180:
            if reason==None:
                reason="問就是沒有"
            await ctx.message.delete()
            await ctx.send(f"距離離開此伺服器尚有{time} 秒\n原因: {reason}")
            await asyncio.sleep(time)
            await ctx.send("再見")
            guild = await self.bot.fetch_guild(id)
            await guild.leave()
            channel=await self.bot.fetch_channel(996340297497853992)
            await channel.send(f"i have left {guild}")
        else:
            await ctx.message.delete()
    
    @commands.command()
    async def print(self,ctx):
        count=0
        guild=""
        for i in self.bot.guilds:
            count+=1
            guild+=f"{count}. {i.name}\n"
        await ctx.send(guild)


def setup(bot):
    bot.add_cog(load(bot))
    bot.add_cog(reload(bot))
    bot.add_cog(unload(bot))
    bot.add_cog(restart(bot))
    bot.add_cog(leaveguild(bot))