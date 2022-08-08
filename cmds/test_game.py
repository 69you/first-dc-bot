import discord
from discord.ext import commands
from matplotlib.pyplot import title
from core.classes import cog_all
import asyncio,random


class OOXX(cog_all):
    @commands.command()
    async def ooxx(self,ctx,enemy=None):
        if enemy==None:
            embed=discord.Embed(title="請輸入對手",color=0xfd12ca)
            await ctx.reply(embed=embed)
        if enemy==ctx.author:
            embed=discord.Embed(title="請不要跟自己過不去",color=0xfd12ca)
            await ctx.reply(embed=embed)
        
        else:
            board=["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"]
            out_put=""
            for i in range(1,10):
                if(i%3==0):
                    out_put+=f"{board[i-1]}\n\n"
                else:
                    out_put+=f"{board[i-1]}      "
            await ctx.send(out_put)


def setup(bot):
    bot.add_cog(OOXX(bot))

##await ctx.send("**\t\t**1**\t\t  **2**  \t\t**3\nA**  **🟦**      **🟦**      **🟦\n\nB**   **🟦**      **🟦**      **🟦\n\nC**   **🟦**      **🟦**      **🟦")