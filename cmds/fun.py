import discord
from discord.ext import commands
from core.classes import cog_all
import json , datetime , random, asyncio
from typing import Union

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
    async def howgay(self,ctx,*,member: discord.Member = None):
        random_num=random.randint(1,100)
        if random_num>50:
            embed=discord.Embed(title=" ",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_author(name=" 假假計算器", icon_url=f"{member.avatar_url}")
            embed.add_field(name=member.display_name+f"是{random_num}% 的假🌈🌈", value="看來果然如此", inline=False)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=" ",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_author(name=" 假假計算器", icon_url=f"{member.avatar_url}")
            embed.add_field(name=member.display_name+f"是{random_num}% 的假🌈", value="我應該算錯了", inline=False)
            await ctx.send(embed=embed)

    @commands.command(aliases=["av"])
    async def avatar(self,ctx,*,member: discord.Member = None):
            link = str(member.avatar_url)
            link2=link.replace(".webp",".png")
            await ctx.message.delete()
            embed=discord.Embed(title=f"{member}  的頭貼",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_image(url = f"{link2}")
            a=await ctx.send(embed=embed)
            b=await ctx.send("十秒後刪除")
            await asyncio.sleep(10)
            await a.delete()
            await b.delete()     

    @commands.command(aliases=["be"])
    async def bigemoji(self,ctx,emoji:Union[discord.Emoji, discord.PartialEmoji]):
        if emoji.animated==False:
            await ctx.message.delete()
            embed=discord.Embed(title=f"{ctx.author} 要求的表符", description=f"`:{emoji.name}:{emoji.id}`", color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_image(url = f"{emoji.url}")
            await ctx.send(embed=embed)
        elif emoji.animated==True:
            await ctx.message.delete()
            embed=discord.Embed(title=f"{ctx.author} 要求的表符", description=f"`a:{emoji.name}:{emoji.id}`", color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_image(url = f"{emoji.url}")
            await ctx.send(embed=embed)

    @commands.command()
    async def ping(self,ctx):
        message=await ctx.send("🏓 Pinging...")
        await asyncio.sleep(1)
        await message.edit(content="延遲 "+f'{round(self.bot.latency*1000)} (ms)')


def setup(bot):
  bot.add_cog(fun(bot))