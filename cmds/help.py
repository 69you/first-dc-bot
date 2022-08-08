from turtle import title
import discord
from discord.ext import commands
from core.classes import cog_all
import datetime

class help(cog_all):

    @commands.command()
    async def help(self,ctx,command=None):
        av=((await ctx.guild.fetch_member(878830839822176287)).avatar_url)
        av2=((await ctx.guild.fetch_member(977086056967053353)).avatar_url)
        if command==None:
            embed=discord.Embed(title="人工智障的指令",description="`輸入*help <指令名稱> 以看更多`",color=0xfd12ca)
            embed.set_author(name="侑介#3856的垃圾機器人",icon_url=f"{av}")
            embed.set_thumbnail(url=f"{av2}")
            embed.set_image(url="https://media.discordapp.net/attachments/977142865836802059/1000298935719575632/undefined_-_Imgur.gif")
            embed.add_field(name="> 一般",value="`ping` `time` `pic` `howgay`",inline=False)
            embed.add_field(name="> 資訊類",value="`avatar` `banner` `serverinfo` `userinfo`",inline=False)
            embed.add_field(name="> 邀請類",value="`invite` `serverinvite` `allinvite`",inline=False)
            embed.add_field(name="> 表情符號類",value="`bigemoji` `createemoji` `deleteemoji`",inline=False)
            embed.add_field(name="> 機器人回應類",value="`sayd` `reply` `edit` `dm` `add` `defemoji`",inline=False)
            embed.add_field(name="> 管理類",value="`ban` `unban` `kick` `pin` `unpin` `clear` `nick`",inline=False)
            embed.add_field(name="> 世劃抽卡",value="`單抽` `十抽` `抽卡`",inline=False)
            embed.add_field(name="> 貓戰耍人(?,",value="待我思考到底要放啥",inline=False)
            embed.add_field(name="> 哈哈,智障作者專用",value="`load` `reload` `unload` `restart` `leaveg`",inline=False)
            time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
            embed.set_footer(text=f"我是人工智慧．{time}",icon_url="https://cdn.discordapp.com/emojis/990679568153190430.gif?size=4096")
            await ctx.send(embed=embed)
        if command=="ping":
            embed=discord.Embed(title="ping",description="指令:**  **`*ping`",color=0xfd12ca)
            embed.add_field(name="查看機器人延遲",value="所需權限:無")
            await ctx.send(embed=embed)
        if command=="time":
            embed=discord.Embed(title="time",description="指令:**  **`*time`",color=0xfd12ca)
            embed.add_field(name="查看現在時間",value="所需權限:無")
            await ctx.send(embed=embed)
        if command=="pic":
            embed=discord.Embed(title="pic",description="指令:**  **`*pic`",color=0xfd12ca)
            embed.add_field(name="隨機或的一個垃圾圖片",value="所需權限:無")
            embed.set_footer(text="真的別用,這是垃圾")
            await ctx.send(embed=embed)
        if command=="howgay":
            embed=discord.Embed(title="howgay",description="指令:**  **`*howgay <成員>`",color=0xfd12ca)
            embed.add_field(name="所需參數",value="<成員>--> `伺服器任一成員,如為空格,則為自己`",inline=False)  
            embed.add_field(name="隨機側一個人多甲",value="所需權限:無")
            embed.set_footer(text="真的別用,這是垃圾")
            await ctx.send(embed=embed)
        if command=="avatar" or command=="av":
            embed=discord.Embed(title="avatar",description="指令:**  **`*avatar <成員>`",color=0xfd12ca)
            embed.add_field(name="相同指令: `avatar`,`av`",value="** **",inline=False)
            embed.add_field(name="所需參數",value="<成員>--> `伺服器任一成員,如為空格,則為自己`",inline=False)  
            embed.add_field(name="顯示某人頭貼",value="所需權限:無") 
            await ctx.send(embed=embed)  
        if command=="banner":
            embed=discord.Embed(title="banner",description="指令:**  **`*banner <成員>`",color=0xfd12ca)
            embed.add_field(name="所需參數",value="<成員>--> `伺服器任一成員,如為空格,則為自己`",inline=False)  
            embed.add_field(name="顯示某人橫幅",value="所需權限:無")  
            embed.set_footer(text="因為作者智商不足,所以動態橫幅無法顯示")
            await ctx.send(embed=embed)
        if command=="serverinfo" or command=="sinfo":
            embed=discord.Embed(title="serverinfo",description="指令:**  **`*serverinfo`",color=0xfd12ca)
            embed.add_field(name="相同指令: `serverinfo`,`sinfo`",value="** **",inline=False)
            embed.add_field(name="傳送伺服器部分資料",value="所需權限:無",inline=False)
            await ctx.send(embed=embed)
        if command=="userinfo" or command=="uinfo":
            embed=discord.Embed(title="userinfo",description="指令:**  **`*userinfo <成員>`",color=0xfd12ca)
            embed.add_field(name="相同指令: `userinfo`,`uinfo`",value="** **",inline=False)
            embed.add_field(name="所需參數",value="<成員>--> `伺服器任一成員,如為空格,則為自己`",inline=False)
            embed.add_field(name="傳送成員部分資料",value="所需權限:無",inline=False)
            await ctx.send(embed=embed)
        if command=="invite":
            embed=discord.Embed(title="invite",description="指令:**  **`*invite`",color=0xfd12ca)
            embed.add_field(name="獲得機器人邀請連結",value="所需權限:無",inline=False)
            await ctx.send(embed=embed)
        if command=="serverinvite" or command=="si":
            embed=discord.Embed(title="serverinvite",description="指令:** **`*serverinvite`",color=0xfd12ca)
            embed.add_field(name="相同指令: `serverinvite`,`si`",value="** **",inline=False)
            embed.add_field(name="獲得伺服器邀請連結",value="所需權限:生成邀請連結",inline=False)
            embed.set_footer(text="沒必要請不要隨意使用")
            await ctx.send(embed=embed)
        if command=="allinvite":
            embed=discord.Embed(title="allinvite",description="指令:** **`*allinvite`",color=0xfd12ca)
            embed.add_field(name="取的人工智障所有存在的伺服器邀請連結",value="所需權限:無(?",inline=False)
            embed.set_footer(text="沒必要請不要隨意使用")
            await ctx.send(embed=embed)
        if command=="bigemoji" or command=="be":
            embed=discord.Embed(title="bigemoji",description="指令:** **`*bigemoji <表情符號>`",color=0xfd12ca)
            embed.add_field(name="相同指令: `bigemoji`,`be`",value="** **",inline=False)
            embed.add_field(name="所需參數",value="<表情符號>--> `任一表情符號(不得為空白)`",inline=False)
            embed.add_field(name="獲得表符的圖片",value="所需權限:無")
            await ctx.send(embed=embed)
        if command=="createemoji" or command=="ae" or command=="ce":
            embed=discord.Embed(title="createemoji",description="指令:** **`*createemoji <url> <name>`",color=0xfd12ca)
            embed.add_field(name="相同指令: `bigemoji`,`ae`,`ce`",value="** **",inline=False)
            embed.add_field(name="所需參數",value="<url>--> `圖片網址(不得為空)`\n<name>--> `表符名稱(可以為空)`",inline=False)
            embed.add_field(name="增加伺服器圖片",value="所需權限:管理表情符號")
            embed.set_footer(text="⚠️ | 不可使用動圖(對不起,我太笨)")
            await ctx.send(embed=embed)
        if command=="deleteemoji" or command=="de":
            embed=discord.Embed(title="deleteemoji",description="指令:** **`*deleteemoji <表情>`",color=0xfd12ca)
            embed.add_field(name="相同指令: `deleteemoji`,`de`",value="** **",inline=False)
            embed.add_field(name="所需參數",value="<表情>--> `伺服器的任一表符(不得為空)`",inline=False)
            embed.add_field(name="刪除伺服器的表符",value="所需權限:管理表情符號")
            await ctx.send(embed=embed)
        if command=="sayd":
            embed=discord.Embed(title="sayd",color=0xfd12ca)
            embed.add_field(name="會用的請自便",value="不會就算了")
            await ctx.send(embed=embed)
        if command=="reply":
            embed=discord.Embed(title="reply",color=0xfd12ca)
            embed.add_field(name="會用的請自便",value="不會就算了")
            await ctx.send(embed=embed)
        if command=="edit":
            embed=discord.Embed(title="edit",color=0xfd12ca)
            embed.add_field(name="會用的請自便",value="不會就算了")
            await ctx.send(embed=embed)
        if command=="dm":
            embed=discord.Embed(title="dm",color=0xfd12ca)
            embed.add_field(name="會用的請自便",value="不會就算了")
            await ctx.send(embed=embed)
        if command=="add":
            embed=discord.Embed(title="add",color=0xfd12ca)
            embed.add_field(name="會用的請自便",value="不會就算了")
            await ctx.send(embed=embed)
        if command=="defemoji":
            embed=discord.Embed(title="defemoji",color=0xfd12ca)
            embed.add_field(name="會用的請自便",value="不會就算了")
            await ctx.send(embed=embed)
        if command=="ban":
            embed=discord.Embed(title="ban",description="指令: `*ban <成員> <原因>`",color=0xfd12ca)
            embed.add_field(name="所需參數",value="<成員>--> `伺服器內成員(不可為白)`\n<原因>--> `問你啊,我看起來像知道嗎(可留空)`",inline=False)
            embed.add_field(name="停權伺服器成員",value="所需權限:停權成員")
            await ctx.send(embed=embed)
        if command=="unban":
            embed=discord.Embed(title="unban",description="指令: `*unban <成員>`",color=0xfd12ca)
            embed.add_field(name="所需參數",value="<成員>--> `成員id(不可為白)`",inline=False)
            embed.add_field(name="解除停權某人",value="所需權限:停權成員")
            await ctx.send(embed=embed)
        if command=="kick":
            embed=discord.Embed(title="kick",description="指令: `*kick <成員> <原因>`",color=0xfd12ca)
            embed.add_field(name="所需參數",value="<成員>--> `伺服器內成員(不可為白)`\n<原因>--> `問你啊,我看起來像知道嗎(可留空)`",inline=False)
            embed.add_field(name="踢除某成員",value="所需權限:踢除成員")
            await ctx.send(embed=embed)
        if command=="pin":
            embed=discord.Embed(title="pin",description="指令: `*pin <id>`",color=0xfd12ca)
            embed.add_field(name="所需參數",value="<id>--> `某訊息的id(不可留白)`",inline=False)
            embed.add_field(name="釘選某訊息",value="所需權限:管理訊息")
            embed.set_footer(text="你都按右鍵複製id了,為甚麼不直接釘選❓")
            await ctx.send(embed=embed)
        if command=="unpin":
            embed=discord.Embed(title="unpin",description="指令: `*unpin <id>`",color=0xfd12ca)
            embed.add_field(name="所需參數",value="<id>--> `某訊息的id(不可留白)`",inline=False)
            embed.add_field(name="解除釘選某訊息",value="所需權限:管理訊息")
            embed.set_footer(text="你都按右鍵複製id了,為甚麼不直接解除釘選❓")
            await ctx.send(embed=embed)
        if command=="單抽":
            embed=discord.Embed(title="單抽",description="指令: `*單抽`",color=0xfd12ca)
            embed.add_field(name="進行世界計畫一次抽卡的模擬(無保底)",value="所需權限:無",inline=False)
            embed.add_field(name="機率",value="<:2s:986995284850667520> 機率: 88.5%\n<:3s:986995297647460383> 機率: 8.5%\n<:4s:986995312046514227> 機率: 3%\n||<:3s:986995297647460383> --> <:4s:986995312046514227> 機率: 10%||")
            await ctx.send(embed=embed)
        if command=="十抽":
            embed=discord.Embed(title="十抽",description="指令: `*十抽`",color=0xfd12ca)
            embed.add_field(name="進行世界計畫十次抽卡的模擬(無保底)",value="所需權限:無",inline=False)
            embed.add_field(name="機率",value="<:2s:986995284850667520> 機率: 88.5%\n<:3s:986995297647460383> 機率: 8.5%\n<:4s:986995312046514227> 機率: 3%\n||<:3s:986995297647460383> --> <:4s:986995312046514227> 機率: 10%||")
            await ctx.send(embed=embed)
        if command=="抽卡":
            embed=discord.Embed(title="抽卡",description="指令: `*抽卡 <數量>`",color=0xfd12ca)
            embed.add_field(name="所需參數",value="<數量> --> `你打算抽的數量(需小於100萬)`",inline=False)
            embed.add_field(name="進行世界計畫任意抽卡數量的模擬(無保底)",value="所需權限:無",inline=False)
            embed.add_field(name="機率",value="<:2s:986995284850667520> 機率: 88.5%\n<:3s:986995297647460383> 機率: 8.5%\n<:4s:986995312046514227> 機率: 3%\n||<:3s:986995297647460383> --> <:4s:986995312046514227> 機率: 10%||")
            await ctx.send(embed=embed)
        if command=="load" or command=="reload" or command=="unload" or command=="restart" or command=="leaveg":
            embed=discord.Embed(title="你不用知道",color=0xfd12ca)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(help(bot))


'''
        #await ctx.message.delete()
        embed=discord.Embed(title="侑介のbot", url="http://yt1.piee.pw/46vhku", description="由侑介#4644所開發的人工智障", color=0xfd12ca, timestamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))
        embed.set_author(name="<==這是侑介", icon_url="https://cdn.discordapp.com/avatars/878830839822176287/e16a95f995ec014da521105e80a9de83.png?size=4096")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/977086056967053353/4f3cce3eb9e13327df584a48f127c7d0.png?size=4096")
        await ctx.send(embed=embed) 
'''
