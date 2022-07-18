import discord
from discord.ext import commands
from core.classes import cog_all
import datetime

class help(cog_all):

    @commands.command()
    async def help(self,ctx):
        #await ctx.message.delete()
        embed=discord.Embed(title="侑介のbot", url="http://yt1.piee.pw/46vhku", description="由侑介#4644所開發的人工智障", color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_author(name="<==這是侑介", icon_url="https://cdn.discordapp.com/avatars/878830839822176287/e16a95f995ec014da521105e80a9de83.png?size=4096")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/977086056967053353/ebc17adf1bc26fe27571586430b56ae8.png?size=4096")
        await ctx.send(embed=embed) 


def setup(bot):
    bot.add_cog(help(bot))