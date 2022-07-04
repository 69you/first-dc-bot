import discord
from discord.ext import commands
from core.classes import cog_all
import json
import asyncio,datetime

with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class respond(cog_all):
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.guild.id != 761900239572434954:  
            keyword1=["早安","早昂"]
            for key1 in keyword1:
                if key1 in msg.content and msg.author != self.bot.user:
                    await msg.reply("早安 <a:emoji_33:971218065259913226>")
                    break

            keyword2=["午安"," 午安阿"]
            for key2 in keyword2:
                if key2 in msg.content and msg.author != self.bot.user:
                    await msg.reply("午安 <:kohane:969515581353123911>")
                    break

            keyword3=["晚安","睡覺","睡覺去","<:sleep:969505662289735750>"]
            for key3 in keyword3:
                if key3 in msg.content and msg.author != self.bot.user:
                    await msg.reply("晚安 <a:778203433701474364:977583066920931338>")
                    break  

            if msg.content == "走開" and msg.author != self.bot.user:
                await msg.reply("你怎麼叫我走開QQ，不跟你好了啦 <:emoji_46:935534306841997333")

            if msg.author.id == (int(jdata["yuusuke id"])) or msg.author.id == (int(jdata["小飄 id"])) or msg.author.id == (int(jdata["小小飄 id"])) or msg.author.id == (int(jdata["煋夜 id"])) or msg.author.id == (int(jdata["死神 id"])) or msg.author.id == (int(jdata["小魚 id"]))  or msg.author.id == (int(jdata["白日夢 id"])):
                if msg.content == "簽" and msg.author != self.bot.user:
                    await msg.add_reaction("✅")

            keyword6=["❓","?","？"]
            for key6 in keyword6:
                if msg.content == key6 and msg.author != self.bot.user:
                    await msg.add_reaction("❓")
                    break

            keyword7=["<:fu:969506818160209920>"]
            for key7 in keyword7:
                if key7 in msg.content and msg.author != self.bot.user:
                    await msg.add_reaction("🇨")
                    await asyncio.sleep(1)
                    await msg.add_reaction("🇦")
                    await asyncio.sleep(1)
                    await msg.add_reaction("🇱")
                    await asyncio.sleep(1)
                    await msg.add_reaction("🇲")

            keyword8=["佬","大佬"]
            for key8 in keyword8:
                if key8 in msg.content and msg.author != self.bot.user and msg.author.id == (int(jdata["yuusuke id"])):
                    await msg.add_reaction("<a:emoji_14:962669697881477279>")
                    await msg.channel.send("<a:emoji_14:962669697881477279>")
                    break
                elif key8 in msg.content and msg.author != self.bot.user and msg.author.id != (int(jdata["yuusuke id"])):
                    await msg.add_reaction("↖️") 
                    await msg.add_reaction("<a:emoji_14:962669697881477279>")
                    await msg.channel.send("<a:emoji_14:962669697881477279>")
                    break

            if msg.author.id == (int(jdata["煋夜 id"])):
                if "可愛" in msg.content and msg.author != self.bot.user:
                    await msg.reply("煋夜，你很可愛")

            keyword12=["E","e"]
            for key12 in keyword12:
                if msg.content == key12 and msg.author != self.bot.user and msg.author.id != (int(jdata["yuusuke id"])):
                    await msg.reply("||請問你在工三小?||"+jdata["ars hit"])
                    break

            if msg.content=="幹":
                await msg.reply("請停止你的行為 "+ jdata["ars hit"])

            keyword9=["假","ru83"]
            if msg.guild.id==938012107167920138:
                for key9 in keyword9:
                    if key9 in msg.content and msg.author != self.bot.user:
                        await msg.add_reaction("<:u_:978299522172211200>")
                        break

            keyword10=["您","sup6"]
            if msg.guild.id==938012107167920138:
                for key10 in keyword10:
                    if key10 in msg.content and msg.author != self.bot.user:
                        await msg.add_reaction("<:fake:978299535128420432>")
                        break

            keyword11=["您假","sup6ru83"]
            if msg.guild.id==938012107167920138:        
                for key11 in keyword11:
                    if key11 in msg.content and msg.author != self.bot.user:
                        await msg.add_reaction("<:u_:978299522172211200>")
                        await msg.add_reaction("<:fake:978299535128420432>")
                        break

            keyword12=["群假","群甲"]
            if msg.guild.id==938012107167920138:
                for key12 in keyword12:
                    if key12 in msg.content and msg.author!= self.bot.user:
                        await msg.reply("除我")
                        break


def setup(bot):
    bot.add_cog(respond(bot))

