import discord
from discord.ext import commands
import datetime
from core.classes import cog_all

class info_user(cog_all):

    @commands.command(aliases=["uinfo"])
    async def userinfo(self,ctx,member=None):
        if member==None:
            user=ctx.author
        else:
            user=await ctx.guild.fetch_member(member)
        embed=discord.Embed(title="使用者訊息", description=" ", color=0xfd12ca)
        embed.set_author(name="人工智障取得的資料", icon_url="https://cdn.discordapp.com/emojis/990679568153190430.gif?size=4096")  
        icon=user.avatar_url_as(format="png")
        embed.set_thumbnail(url=f"{icon}")   
        embed.add_field(name="`使用者名稱`",value=f"{user.name}#{user.discriminator}",inline=True)
        if user.nick==None:
            embed.add_field(name="`伺服器暱稱`",value="無設定暱稱",inline=True)
        else:
            embed.add_field(name="`伺服器暱稱`",value=f"{user.nick}",inline=True)
        embed.add_field(name="`使用者id`",value=f"{user.id}",inline=True)   
        embed.add_field(name="`使用者帳號色彩`",value=f"{user.color}",inline=True)
        ctime=str(user.created_at)
        embed.add_field(name="`創建帳號時間`",value=f"{ctime[:-7]}",inline=True)
        jtime=str(user.joined_at) 
        embed.add_field(name="`加入伺服器時間`",value=f"{jtime[:-7]}",inline=True)        
        role=""
        for i in range(len(user.roles)-1,0,-1):
            role+=f"{user.roles[i].mention}"+" "   
        embed.add_field(name="`使用者身分組:`",value=f"{role}",inline=True)
        time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
        embed.set_footer(text=f"資料取得時間: {time}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(info_user(bot))