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

        if msg.content == "走開" and msg.author != self.bot.user:
            await msg.reply("你怎麼叫我走開QQ，不跟你好了啦")
            await msg.channel.send("<:emoji_46:935534306841997333>")  

        if msg.author.id == 869025114862284810 or msg.author.id == 647775766838378496 or msg.author.id == 942632954935541800 or msg.author.id == 927834871857033267 or msg.author.id == 878830839822176287 or msg.author.id == 883559220803436574 or msg.author.id == 711241728375652353 or msg.author.id == 571295524158963712 or msg.author.id == 935414869648351313 or msg.author.id == 860280256208437258 or msg.author.id ==880009654061645824:
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
                await msg.add_reaction("🇦")
                await msg.add_reaction("🇱")
                await msg.add_reaction("🇲")

        keyword8=["佬","大佬"]
        for key8 in keyword8:
            if key8 in msg.content and msg.author != self.bot.user:
                await msg.channel.send("<a:emoji_14:962669697881477279>")
                await msg.add_reaction("<a:emoji_14:962669697881477279>")
                break

        keyword9=["假","ru83"]
        for key9 in keyword9:
            if key9 in msg.content and msg.author != self.bot.user:
                await msg.add_reaction("<:u_:978299522172211200>")
                break

        keyword10=["您","sup6"]
        for key10 in keyword10:
            if key10 in msg.content and msg.author != self.bot.user:
                await msg.add_reaction("<:fake:978299535128420432>")
                break

        keyword11=["您假","sup6ru83"]
        for key11 in keyword11:
            if key11 in msg.content and msg.author != self.bot.user:
                await msg.add_reaction("<:u_:978299522172211200>")
                await msg.add_reaction("<:fake:978299535128420432>")
                break

        if msg.author.id == 927834871857033267:
            if "可愛" in msg.content and msg.author != self.bot.user:
                    await msg.reply("煋夜，你很可愛")
        

def setup(bot):
    bot.add_cog(respond(bot))