import discord
from discord.ext import commands
from core.classes import cog_all
import json , datetime 

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class fun_allinvite(cog_all):

    @commands.command()
    async def allinvite(self,ctx):
        embed=discord.Embed(title="人工智障目前所在的所有有伺服器",color=0xfd12ca)
        embed.set_author(name="人工智障",icon_url="https://cdn.discordapp.com/emojis/990679568153190430.gif?size=4096")
        for i in self.bot.guilds:
            if i.name=="不知道" or i.name=="bot test" or i.name=="假の俱樂部":
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


def setup(bot):
    bot.add_cog(fun_allinvite(bot))