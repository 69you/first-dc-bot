import discord
from discord.ext import commands
import random,asyncio
from core.classes import cog_all

class gatcha(cog_all):
    @commands.command()
    async def 單抽(self,ctx):
        a=random.uniform(1,100)
        if(a>11.5):
            msga=await ctx.reply("<:pre2:986995238117720114>")
            await asyncio.sleep(2)
            await msga.edit(content="<:2s:986995284850667520>")
        elif(a<11.5 and a>3):
            b=random.uniform(1,100)
            if(b<10):
                msgb=await ctx.reply("<:pre3:986995251824717864>")
                await asyncio.sleep(2)
                await msgb.edit(content="<:4s:986995312046514227>")
            else:
                msgc=await ctx.reply("<:pre3:986995251824717864>")
                await asyncio.sleep(2)
                await msgc.edit(content="<:3s:986995297647460383>")
        elif(a<3):
            msgc=await ctx.reply("<:pre4:986995267742089386>")
            await asyncio.sleep(1)
            await msgc.edit(content="<:4s:986995312046514227>")

    @commands.command()
    async def 十抽(self,ctx):
        list=""
        for i in range(0,5):
            a=random.uniform(1,100)
            if(a<=3):
                list=list+("<:4s:986995312046514227> ")
            elif(a>3 and a<=11.5):
                b=random.uniform(1,100)
                if(b<=10):
                    list=list+("<:4s:986995312046514227> ")
                else:
                    list=list+("<:3s:986995297647460383> ")
            else:
                list=list+("<:2s:986995284850667520> ")
        list=list+("\n")
        for i in range(0,5):
            a=random.uniform(1,100)
            if(a<=3):
                list=list+("<:4s:986995312046514227> ")
            elif(a>3 and a<=11.5):
                b=random.uniform(1,100)
                if(b<=10):
                    list=list+("<:4s:986995312046514227> ")
                else:
                    list=list+("<:3s:986995297647460383> ")
            else:
                list=list+("<:2s:986995284850667520> ")

        if "<:4s:986995312046514227>" in list and "<:3s:986995297647460383>" not in list:
            a=await ctx.reply("<:pre4:986995267742089386>")
            await asyncio.sleep(2)
            await a.edit(content=list)
        elif "<:3s:986995297647460383>" not in list and "<:4s:986995312046514227>" not in list:
            newlist=list[:-25]
            newlist=newlist+"<:3s:986995297647460383>"
            a=await ctx.reply("<:pre3:986995251824717864>")
            await asyncio.sleep(2)
            await a.edit(content=newlist)
        else:
            a=await ctx.reply("<:pre3:986995251824717864>")
            await asyncio.sleep(1)
            await a.edit(content=list)

    @commands.command()
    async def 抽卡(self,ctx,num:int):
        if num>1000000:
            embed=discord.Embed(name="數量過大",description="為了我自己找想，請輸入小於100w的數字",color=0xfd12ca)
            embed.set_author(name="我會壞掉",icon_url="https://cdn.discordapp.com/emojis/585569938803261461.webp?size=4096")
            await ctx.reply(embed=embed)
        else:
            twostar=0
            threestar=0
            fourstar=0
            for i in range(1,num+1,1):
                a=random.uniform(1,100)
                if(a<=3):
                    fourstar+=1
                elif(a>3 and a<=11.5):
                    b=random.uniform(1,100)
                    if(b<=10):
                        fourstar+=1
                    else:
                        threestar+=1
                else:
                    twostar+=1
            probability=round((fourstar/num*100),3)
            a=await ctx.reply(f"<a:715586639623356438:989524987696254996>")
            await asyncio.sleep(1)
            await a.edit(content="<a:881774587325599775:993187866911985725>")
            await asyncio.sleep(2)
            await a.edit(content=f"本次共 {num} 抽\n二星數量: {twostar}\n三星數量: {threestar}\n四星數量: {fourstar}\n出彩機率: {probability}%")


def setup(bot):
    bot.add_cog(gatcha(bot))