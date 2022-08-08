import discord
from discord.ext import commands
from core.classes import cog_all
import json , datetime ,requests
from typing import Union
from io import BytesIO
from PIL import Image

class emoji(cog_all):

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
    
    @commands.command(aliases=["ae","ce"])
    @commands.has_guild_permissions(manage_emojis=True)
    async def createemoji(self,ctx,emoji,name=None):
        nowemoji=0
        for i in ctx.guild.emojis:
            nowemoji+=1
        if nowemoji==ctx.guild.emoji_limit:
            await ctx.reply("已達到表符最大數量，不可再增加 <a:760172996119232595:1000620660365742081>")
        else:
            t=0
            if name==None:
                for i in ctx.guild.emojis:
                    t+=1
                name=f"emoji_{t}"
            else:
                name=name
            
            r=requests.get(emoji)
            img=Image.open(BytesIO(r.content),mode="r")
            b=BytesIO()
            img.save(b,format="PNG")
            b.value=b.getvalue()
            emoji=await ctx.guild.create_custom_emoji(image=b.value,name=name)
            await ctx.send(f"成功新增表情 <:{emoji.name}:{emoji.id}>")
    
    @commands.command(aliases=["de"])
    @commands.has_guild_permissions(manage_emojis=True)
    async def deleteemoji(self,ctx,emoji:discord.Emoji):
        name=emoji.name
        #emoji=ctx.guild.fetch_emoji(emoji.id)
        await emoji.delete()
        await ctx.send(f"已刪除表情 `{name}` <:{emoji.name}:{emoji.id}>")


def setup(bot):
    bot.add_cog(emoji(bot))