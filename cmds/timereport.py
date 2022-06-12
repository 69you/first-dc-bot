import discord
from discord.ext import commands
import datetime , asyncio 
from core.classes import cog_all

class timereport(cog_all):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        async def report0():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "000000":
                    await self.channel.send("現在時間: 凌晨0點整")
                    await self.channel.send("大家晚安 <a:778203433701474364:977583066920931338>")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report0())     


        async def report1():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "010000":
                    await self.channel.send("現在時間: 半夜1點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report1()) 


        async def report2():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "020000":
                    await self.channel.send("現在時間: 半夜2點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report2()) 


        async def report3():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "030000":
                    await self.channel.send("好耶，三點了")
                    await self.channel.send("https://i.imgur.com/EGO35hf.jpg")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report3()) 


        async def report4():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "040000":
                    await self.channel.send("現在時間: 半夜4點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report4()) 


        async def report5():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "050000":
                    await self.channel.send("現在時間: 凌晨5點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report5())


        async def report6():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "060000":
                    await self.channel.send("現在時間: 凌晨6點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report6())


        async def report7():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "070000":
                    await self.channel.send("現在時間: 早上7點整")
                    await self.channel.send("大家早安")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report7())


        async def report8():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "080000":
                    await self.channel.send("現在時間: 早上8點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report8())


        async def report9():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "090000":
                    await self.channel.send("現在時間: 早上9點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report9())


        async def report10():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "100000":
                    await self.channel.send("現在時間: 早上10點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report10())


        async def report11():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "110000":
                    await self.channel.send("現在時間: 早上11點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report11())


        async def report12():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "120000":
                    await self.channel.send("現在時間: 早上12點整")
                    await self.channel.send("大家吃午餐了嗎? 🍚🥩🥬🍎")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report12())


        async def report13():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "130000":
                    await self.channel.send("現在時間: 下午1點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report13())


        async def report14():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "140000":
                    await self.channel.send("現在時間: 下午2點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report14())


        async def report15():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "150000":
                    await self.channel.send("現在時間: 下午3點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report15())


        async def report16():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "160000":
                    await self.channel.send("現在時間: 下午4點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report16())


        async def report17():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "170000":
                    await self.channel.send("現在時間: 下午5點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report17())


        async def report18():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "180000":
                    await self.channel.send("現在時間: 晚上6點整")
                    await self.channel.send("大家吃晚餐了嗎 🍙🧋")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report18())


        async def report19():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "190000":
                    await self.channel.send("現在時間: 晚上7點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report19())


        async def report20():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "200000":
                    await self.channel.send("現在時間: 晚上8點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report20())


        async def report21():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "210000":
                    await self.channel.send("現在時間: 晚上9點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report21())


        async def report22():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "220000":
                    await self.channel.send("現在時間: 晚上10點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report22())


        async def report23():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936568482756177921)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%H%M%S")   
                if now_time == "230000":
                    await self.channel.send("現在時間: 晚上11點整")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(report23())


def setup(bot):
    bot.add_cog(timereport(bot))        