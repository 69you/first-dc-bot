from ast import keyword
import string
import discord
from discord.ext import commands
from core.classes import cog_all
import json , datetime , random, asyncio

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class fun(cog_all):
    @commands.command()
    async def pic(self,ctx):
        await ctx.send((random.choice(jdata['pic'])))

    @commands.command()
    async def time(self,ctx):
        now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
        await ctx.channel.send(f"現在時間: {now_time}")        

    @commands.command()
    async def ping(self,ctx):
        message=await ctx.send("🏓 Pinging...")
        await asyncio.sleep(1)
        await message.edit(content="延遲 "+f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def sayd(self,ctx, *,msg):
        if ctx.author.id == (int(jdata["yuusuke id"])):
            await ctx.message.delete()
            await ctx.send(msg)
        else :
            await ctx.message.delete()

    @commands.command()
    async def howgay(self,ctx,*,member: discord.Member = None):
        random_num=random.randint(1,100)
        if random_num>50:
            await ctx.message.delete()
            embed=discord.Embed(title=" ",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_author(name=" 假假計算器", icon_url=f"{member.avatar_url}")
            embed.add_field(name=member.display_name+f"是{random_num}% 的假🌈🌈", value="看來果然如此", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            embed=discord.Embed(title=" ",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_author(name=" 假假計算器", icon_url=f"{member.avatar_url}")
            embed.add_field(name=member.display_name+f"是{random_num}% 的假🌈", value="我應該算錯了", inline=False)
            await ctx.send(embed=embed)

    @commands.command(aliases=["av"])
    async def avatar(self,ctx,*,member: discord.Member = None):
            link = (member.avatar_url)
            await ctx.message.delete()
            embed=discord.Embed(title=f"{member}  的頭貼")
            embed.set_image(url = f"{link}")
            await ctx.send(embed=embed)
            await ctx.send("十秒後刪除")
            await asyncio.sleep(10)
            await ctx.channel.purge(limit= 2)


def setup(bot):
  bot.add_cog(fun(bot))