from turtle import title
import discord
from discord.ext import commands
import datetime
from core.classes import cog_all

class invite(cog_all):

    @commands.Cog.listener()
    async def on_member_join(self,member):
        if member.guild.id==1000468384556789862:
            embed=discord.Embed(title="",description="",color=0xfd12ca)
            embed.set_author(name=member.name,icon_url=member.avatar_url)
            embed.set_thumbnail(url=member.guild.icon_url)
            embed.add_field(name=f"Hi,{member.name},歡迎來到這裡",value=f"** **\n請先幫我前往 <#1000489504861339659> <#1000578909366141009>\n填一下資料\n\n再去 <#1000643596749389944>拿身分組\n不然看不到頻道唷\n\n讓我們更加認識彼此吧！\n")
            time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
            embed.set_footer(text=f"加入時間: {time}")
            a= await self.bot.fetch_channel(1000610946055671900)
            await a.send(embed=embed)
    

def setup(bot):
    bot.add_cog(invite(bot))