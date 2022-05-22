from array import array
from ast import keyword
from email import message
import imp
import discord
from discord.ext import commands
from core.classes import cog_all

import json
import random
with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


class respond(cog_all):
    @commands.Cog.listener()
    async def on_message(self,msg):

        keyword1=["早安"]
        for key1 in keyword1:
            if key1 in msg.content and msg.author != self.bot.user and msg.author.id !=338222603829510164:
                await msg.reply("早安")
                await msg.channel.send("<a:emoji_33:971218065259913226>")
                break

        keyword2=["午安"]
        if msg.content in keyword2 and msg.author != self.bot.user:
            await msg.reply("午安 <:kohane:969515581353123911>")

        keyword3=["晚安","睡覺","睡覺去"]
        for key3 in keyword2:
            if msg.content in keyword3 and msg.author != self.bot.user:
                await msg.reply("晚安")
                await msg.channel.send("<a:778203433701474364:977583066920931338>") 
                break  

        keyword4=["走開"]
        if msg.content in keyword4 and msg.author != self.bot.user:
            await msg.reply("你怎麼叫我走開QQ，不跟你好了啦")
            await msg.channel.send("<:emoji_46:935534306841997333>")  

        keyword5=["簽","ㄑ"]
        for key5 in keyword5:
            if msg.content in keyword5 and msg.author != self.bot.user:
                await msg.add_reaction("✅")
                break

        keyword6=["❓","?","？"]
        for key6 in keyword6:
            if msg.content in keyword6 and msg.author != self.bot.user:
                await msg.add_reaction("❓")
                break

        keyword7=["<:fu:969506818160209920>"]
        if msg.content in keyword7 and msg.author != self.bot.user:
            await msg.add_reaction("🇨")
            await msg.add_reaction("🇦")
            await msg.add_reaction("🇱")
            await msg.add_reaction("🇲")
        
        if msg.content =="<@584677291318312963>" :
            ramdon_word=random.choice(jdata['word'])
            await msg.channel.send("<@584677291318312963>")
            await msg.channel.send(ramdon_word)

def setup(bot):
    bot.add_cog(respond(bot))