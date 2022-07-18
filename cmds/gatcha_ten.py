import discord
from discord.ext import commands
import random,asyncio
from core.classes import cog_all

class gatcha_ten(cog_all):

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


def setup(bot):
    bot.add_cog(gatcha_ten(bot))