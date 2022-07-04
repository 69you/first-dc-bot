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
    async def howgay(self,ctx,member: discord.Member = None):
        random_num=random.randint(1,100)
        if member==None:
            if random_num>50:
                embed=discord.Embed(title=" ",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
                embed.set_author(name=" 假假計算器", icon_url=f"{ctx.author.avatar_url}")
                embed.add_field(name=ctx.author.display_name+f" 是{random_num}% 的假🌈🌈", value="看來果然如此", inline=False)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title=" ",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
                embed.set_author(name=" 假假計算器", icon_url=f"{ctx.author.avatar_url}")
                embed.add_field(name=ctx.author.display_name+f" 是{random_num}% 的假🌈", value="我應該算錯了", inline=False)
                await ctx.send(embed=embed)            
        else:
            if random_num>50:
                embed=discord.Embed(title=" ",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
                embed.set_author(name=" 假假計算器", icon_url=f"{member.avatar_url}")
                embed.add_field(name=member.display_name+f" 是{random_num}% 的假🌈🌈", value="看來果然如此", inline=False)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title=" ",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
                embed.set_author(name=" 假假計算器", icon_url=f"{member.avatar_url}")
                embed.add_field(name=member.display_name+f" 是{random_num}% 的假🌈", value="我應該算錯了", inline=False)
                await ctx.send(embed=embed)

    @commands.command(aliases=["av"])
    async def avatar(self,ctx,member: discord.Member = None):
        if member==None:
            link = str(ctx.author.avatar_url_as(format="png"))
            await ctx.message.delete()
            embed=discord.Embed(title=f"{ctx.author}  的頭貼",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_image(url = f"{link}")
            a=await ctx.send(embed=embed)
            b=await ctx.send("十秒後刪除")
            await asyncio.sleep(10)
            await a.delete()
            await b.delete()             
        else:
            link = str(member.avatar_url_as(format="png"))
            await ctx.message.delete()
            embed=discord.Embed(title=f"{member}  的頭貼",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_image(url = f"{link}")
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

    @commands.command()
    async def invite(self,ctx):
        embed=discord.Embed(title="人工智障的邀請函",url="https://discord.com/api/oauth2/authorize?client_id=977086056967053353&permissions=8&scope=bot%20applications.commands",description=f"邀請前請先找 `侑介#4644`", color=0xfd12ca)
        await ctx.send(embed=embed)

    @commands.command()
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
    
    @commands.command(aliases=["si"])
    async def serverinvite(self,ctx):
            link=await ctx.channel.create_invite()
            await ctx.send(str(link))    


def setup(bot):
  bot.add_cog(fun(bot))