import discord
from discord.ext import commands
import random,asyncio
from core.classes import cog_all

class gatcha_random(cog_all):

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
    bot.add_cog(gatcha_random(bot))