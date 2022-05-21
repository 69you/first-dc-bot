from ast import keyword
import discord
from discord.ext import commands
from core.classes import cog_all

class respond(cog_all):
    @commands.Cog.listener()
    async def on_message(self,msg):

        keyword1=["早安","早"]
        if msg.content in keyword1 and msg.author != self.bot.user:
            await msg.reply("早安")
            await msg.channel.send("<a:emoji_33:971218065259913226>")

        keyword2=["午安"]
        if msg.content in keyword2 and msg.author != self.bot.user:
            await msg.reply("午安 <:kohane:969515581353123911>")

        keyword3=["晚安","睡覺"]
        if msg.content in keyword3 and msg.author != self.bot.user:
            await msg.reply("晚安")
            await msg.channel.send("<a:778203433701474364:977583066920931338>")   

        keyword4=["走開"]
        if msg.content in keyword4 and msg.author != self.bot.user:
            await msg.reply("你怎麼叫我走開QQ，不跟你好了啦")
            await msg.channel.send("<:emoji_46:935534306841997333>")  

def setup(bot):
    bot.add_cog(respond(bot))