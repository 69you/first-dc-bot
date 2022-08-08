import discord
from discord.ext import commands 
import json,datetime,asyncio,os,sys,random
from core.classes import cog_all

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


class image(cog_all):
    
    @commands.command(aliases=["av"])
    async def avatar(self,ctx,member: discord.Member = None):
        if member==None:
            member=ctx.author             
        link = str(member.avatar_url_as(format="png"))
        await ctx.message.delete()
        embed=discord.Embed(title=f"{member}  的頭貼",color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_image(url = f"{link}")
        a=await ctx.send(embed=embed)
        b=await ctx.send("十秒後刪除")
        await asyncio.sleep(10)
        await a.delete()
        await b.delete()  

    @commands.command()
    async def banner(self,ctx, user:discord.Member=None):
        if user == None:
            user = ctx.author
        req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
        banner_id = req["banner"]
        if banner_id:
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
            embed=discord.Embed(title=f"{user} 的橫幅",description=" ", color=0xfd12ca,timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
            embed.set_image(url=f"{banner_url}")
            await ctx.send(embed=embed)
        else:
            await ctx.reply("該使用者無橫幅")


class invite(cog_all):
    @commands.command()
    async def invite(self,ctx):
        embed=discord.Embed(title="人工智障的邀請函",url="https://discord.com/api/oauth2/authorize?client_id=977086056967053353&permissions=8&scope=bot%20applications.commands",description=f"邀請前請先找 `侑介#3856`", color=0xfd12ca)
        await ctx.send(embed=embed)

    @commands.command(aliases=["si"])
    async def serverinvite(self,ctx):
            link=await ctx.channel.create_invite()
            await ctx.send(str(link)) 

    @commands.command()
    async def allinvite(self,ctx):
        embed=discord.Embed(title="人工智障目前所在的所有有伺服器",color=0xfd12ca)
        embed.set_author(name="人工智障",icon_url="https://cdn.discordapp.com/emojis/990679568153190430.gif?size=4096")
        for i in self.bot.guilds:
            if i.name=="不知道" or i.name=="bot test" or i.name=="假の俱樂部" or i.name=="阿莎芯雅 的伺服器":
                pass
            else:
                for j in i.channels:
                    if i.description==None:
                        description="連結"
                    else:
                        description=i.description
                    a=await j.create_invite()
                    embed.add_field(name=f"{i.name}",value=f"[{description}]({str(a)})",inline=False)
                    break
        time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
        embed.set_footer(text=f"資料取得時間: {time}")
        await ctx.reply(embed=embed)


class trash(cog_all):

    @commands.command()
    async def pic(self,ctx):
        await ctx.send((random.choice(jdata['pic'])))

    @commands.command()
    async def time(self,ctx):
        now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
        america_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).strftime("%Y /%m /%d  %H :%M :%S")
        await ctx.channel.send(f"台灣香港時間: {now_time}\n亞利桑那時間: {america_time}") 

    @commands.command()
    async def howgay(self,ctx,member: discord.Member = None):
        random_num=random.randint(1,100)
        if member==None:
            member=ctx.author          
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
    

def setup(bot):
    bot.add_cog(image(bot))
    bot.add_cog(invite(bot))
    bot.add_cog(trash(bot))
