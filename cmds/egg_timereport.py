import discord
from discord.ext import commands
import datetime , asyncio ,json
from core.classes import cog_all
#957607990079393822
with open ('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class timereport2(cog_all):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        async def report0():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "000000": 
                    await self.channel.send("現在時間: 台灣香港凌晨0點整\n大家晚安 <a:778203433701474364:977583066920931338>")
                    await self.channel.send("現在時間: 亞利桑那早上9點")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report0())     


        async def report1():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "010000":
                    await self.channel.send("現在時間: 台灣香港半夜1點整")
                    await self.channel.send("現在時間: 亞利桑那早上10點")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report1()) 


        async def report2():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "020000":
                    await self.channel.send("現在時間: 台灣香港半夜2點整")
                    await self.channel.send("現在時間: 亞利桑那早上11點")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report2()) 


        async def report3():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "030000":
                    await self.channel.send("好耶，台灣和香港3點了")
                    await self.channel.send("https://cdn.discordapp.com/emojis/1000438030798172191.gif?size=4096")
                    await self.channel.send("好耶，亞利桑那中午12點了\n<@957607990079393822> 吃午餐了嗎? 🍚🥩🥬🍎")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report3()) 


        async def report4():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "040000":
                    await self.channel.send("現在時間: 台灣香港半夜4點整")
                    await self.channel.send("現在時間: 亞利桑那下午1點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report4()) 


        async def report5():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "050000":
                    await self.channel.send("現在時間: 台灣香港凌晨5點整")
                    await self.channel.send("現在時間: 亞利桑那下午2點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report5())


        async def report6():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "060000":
                    await self.channel.send("現在時間: 台灣香港凌晨6點整")
                    await self.channel.send("現在時間: 亞利桑那下午3點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report6())


        async def report7():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "070000":
                    await self.channel.send("現在時間: 台灣香港早上7點整\n大家早安 <:cat_high:980786769463230486>")
                    await self.channel.send("現在時間: 亞利桑那下午4點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report7())


        async def report8():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "080000":
                    await self.channel.send("現在時間: 台灣香港早上8點整")
                    await self.channel.send("現在時間: 亞利桑那下午5點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report8())


        async def report9():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "090000":
                    await self.channel.send("現在時間: 台灣香港早上9點整")
                    await self.channel.send("現在時間: 亞利桑那晚上6點整\n<@957607990079393822> 吃午餐了嗎? 🍚🥩🥬🍎")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report9())


        async def report10():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "100000":
                    await self.channel.send("現在時間: 台灣香港早上10點整")
                    await self.channel.send("現在時間: 亞利桑那晚上7點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report10())


        async def report11():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "110000":
                    await self.channel.send("現在時間: 台灣香港早上11點整")
                    await self.channel.send("現在時間: 亞利桑那晚上8點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report11())


        async def report12():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "120000":
                    await self.channel.send("現在時間: 台灣香港早上12點整\n大家吃午餐了嗎? 🍚🥩🥬🍎")
                    await self.channel.send("現在時間: 亞利桑那晚上9點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report12())


        async def report13():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "130000":
                    await self.channel.send("現在時間: 台灣香港下午1點整")
                    await self.channel.send("現在時間: 亞利桑那晚上10點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report13())


        async def report14():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "140000":
                    await self.channel.send("現在時間: 台灣香港下午2點整")
                    await self.channel.send("現在時間: 亞利桑那晚上11點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report14())


        async def report15():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "150000":
                    await self.channel.send("現在時間: 台灣香港下午3點整")
                    await self.channel.send("現在時間: 亞利桑那凌晨0點整\n<@957607990079393822> 晚安 <a:778203433701474364:977583066920931338>")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report15())


        async def report16():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "160000":
                    await self.channel.send("現在時間: 台灣香港下午4點整")
                    await self.channel.send("現在時間: 亞利桑那半夜1點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report16())


        async def report17():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "170000":
                    await self.channel.send("現在時間: 台灣香港下午5點整")
                    await self.channel.send("現在時間: 亞利桑那半夜2點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report17())


        async def report18():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "180000":
                    await self.channel.send("好耶，台灣香港晚上6點整\n大家吃晚餐了嗎 🍙🧋")
                    await self.channel.send("好耶，亞利桑那半夜3點整")
                    await self.channel.send("https://cdn.discordapp.com/emojis/1000438030798172191.gif?size=4096")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report18())


        async def report19():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "190000":
                    await self.channel.send("現在時間: 台灣香港晚上7點整")
                    await self.channel.send("現在時間: 亞利桑那半夜4點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report19())


        async def report20():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "200000":
                    await self.channel.send("現在時間: 台灣香港晚上8點整")
                    await self.channel.send("現在時間: 亞利桑那半夜5點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report20())


        async def report21():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "210000":
                    await self.channel.send("現在時間: 台灣香港晚上9點整")
                    await self.channel.send("現在時間: 亞利桑那半夜6點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report21())


        async def report22():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "220000":
                    await self.channel.send("現在時間: 台灣香港晚上10點整")
                    await self.channel.send("現在時間: 亞利桑那早上7點整\n<@957607990079393822> 早安 <:cat_high:980786769463230486>")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report22())


        async def report23():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(948899012340244520)
            while (jdata["stop"]=="False"):
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "230000":
                    await self.channel.send("現在時間: 台灣香港晚上11點整")
                    await self.channel.send("現在時間: 亞利桑那早上8點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report23())
              

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def stop(self,ctx):
        if ctx.author.guild.id==944855324706344980:
            if jdata["stop"]=="True":
                embed=discord.Embed(title="自動報時已經關閉",color=0xfd12ca)
                await ctx.reply(embed=embed)
            else:
                jdata["stop"]="True"
                with open ('setting.json',mode='w',encoding='utf8') as jfile:
                    json.dump(jdata,jfile,indent=4)
                self.bot.reload_extension(f'cmds.egg_timereport')
                embed=discord.Embed(title="關閉自動報時",color=0xfd12ca)
                await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def start(self,ctx):
        if ctx.author.guild.id==944855324706344980:
            if jdata["stop"]=="False":
                embed=discord.Embed(title="自動報時已經開啟",color=0xfd12ca)
                await ctx.reply(embed=embed)
            else:
                jdata["stop"]="False"
                with open ('setting.json',mode='w',encoding='utf8') as jfile:
                    json.dump(jdata,jfile,indent=4)
                self.bot.reload_extension(f'cmds.egg_timereport')
                embed=discord.Embed(title="自動報時中",color=0xfd12ca)
                await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(timereport2(bot))        