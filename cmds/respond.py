from array import array
from ast import keyword
from email import message
import imp
import discord
from discord.ext import commands
from core.classes import cog_all


class respond(cog_all):
    @commands.Cog.listener()
    async def on_message(self,msg):

        keyword1=["早安","早昂"]
        for key1 in keyword1:
            if key1 in msg.content and msg.author != self.bot.user:
                await msg.reply("早安")
                await msg.channel.send("<a:emoji_33:971218065259913226>")
                break

        keyword2=["午安"," 午安阿"]
        for key2 in keyword2:
            if key2 in msg.content and msg.author != self.bot.user:
                await msg.reply("午安 <:kohane:969515581353123911>")
                break

        keyword3=["晚安","睡覺","睡覺去"]
        for key3 in keyword3:
            if key3 in msg.content and msg.author != self.bot.user:
                await msg.reply("晚安")
                await msg.channel.send("<a:778203433701474364:977583066920931338>") 
                break  

        keyword4=["走開"]
        for key4 in keyword4:
            if key4 in msg.content and msg.author != self.bot.user:
                await msg.reply("你怎麼叫我走開QQ，不跟你好了啦")
                await msg.channel.send("<:emoji_46:935534306841997333>")  

        keyword5=["簽","ㄑ"]
        for key5 in keyword5:
            if key5 in msg.content and msg.author != self.bot.user:
                await msg.add_reaction("✅")
                break

        keyword6=["❓","?","？"]
        for key6 in keyword6:
            if key6 in msg.content and msg.author != self.bot.user:
                await msg.add_reaction("❓")
                break

        keyword7=["<:fu:969506818160209920>"]
        for key7 in keyword7:
            if key7 in msg.content and msg.author != self.bot.user:
                await msg.add_reaction("🇨")
                await msg.add_reaction("🇦")
                await msg.add_reaction("🇱")
                await msg.add_reaction("🇲")

        keyword8=["佬","大佬"]
        for key8 in keyword8:
            if key8 in msg.content and msg.author != self.bot.user:
                await msg.channel.send("<a:emoji_14:962669697881477279>")
                await msg.add_reaction("<a:emoji_14:962669697881477279>")
                break
        

def setup(bot):
    bot.add_cog(respond(bot))