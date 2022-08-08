import discord
from discord.ext import commands
from matplotlib.pyplot import title
from core.classes import cog_all
import asyncio,random


class guess_num(cog_all):
    @commands.command()
    async def guess(self,ctx,num:int=None,round:int=None):
        if num==None:
            num=100
        else:
            num=num
        if round==None:
            round=5
        else:
            round=round
        target_num=random.randint(1,num)
        def check(msg):
            return msg.author==ctx.author and msg.channel==ctx.channel
        embed=discord.Embed(title=f"數字已經決定,範圍落在1~{num}\n你有{round}次機會,請進行猜測",color=0xfd12ca)
        await ctx.reply(embed=embed)
        guess_time=round
        end=False
        while(guess_time>=0):
            try:
                guess_num = await self.bot.wait_for('message',check=check,timeout=20.0)
                guess = int(guess_num.content)

            except ValueError:
                if guess_num.content=="*stop":
                    embed=discord.Embed(title="已停止遊戲",color=0xfd12ca)
                    await guess_num.reply(embed=embed)
                    break
                else:
                    embed=discord.Embed(title=f"請輸入 1~{num} 間的數字",color=0xfd12ca)
                    await guess_num.reply(embed=embed)

            except asyncio.TimeoutError:
                embed=discord.Embed(title="已超時",description="如要再玩,請重新輸入指令",color=0xfd12ca)
                await ctx.send(f"{ctx.author.mention}",embed=embed)
                break
                
            else:
                if(int(guess_num.content)<=0 or int(guess_num.content)>num):
                    embed=discord.Embed(title=f"請輸入 1~{num} 間的數字",color=0xfd12ca)
                    await guess_num.reply(embed=embed)
                else:
                    guess_time-=1
                    if guess_time !=0 and guess > target_num:
                        embed=discord.Embed(title=f'比 {guess} 還小',color=0xfd12ca)
                        embed.set_footer(text=f"還剩 {guess_time} 次機會")
                        await guess_num.reply(embed=embed)
                    if guess_time !=0 and guess < target_num:
                        embed=discord.Embed(title=f'比 {guess} 還大',color=0xfd12ca)
                        embed.set_footer(text=f"還剩 {guess_time} 次機會")
                        await guess_num.reply(embed=embed)
                    if guess==target_num:
                        embed=discord.Embed(title=f'恭喜你答對了',color=0xfd12ca)
                        await guess_num.reply(embed=embed)
                        end=True
                        break
                    if guess_time==0 and end==False and guess!=target_num:
                        embed=discord.Embed(title="可惜你沒猜對",description=f"正確答案是 {target_num}",color=0xfd12ca)
                        await guess_num.reply(embed=embed)
                        break


def setup(bot):
    bot.add_cog(guess_num(bot))