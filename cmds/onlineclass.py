import discord
from discord.ext import commands
import datetime , asyncio 
from core.classes import cog_all

class onlineclass(cog_all):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#monday        
        async def class1():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "1081000":
                    await self.channel.send("下節是莉莉的美勞課")
                    await self.channel.send("https://meet.google.com/lookup/fl3okgx6ml")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class1())     


        async def class2():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "1101000":
                    await self.channel.send("下節是紹偉的基電課")
                    await self.channel.send("https://meet.google.com/ypx-uwss-ssu")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class2()) 


        async def class3():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "1130000":
                    await self.channel.send("下節是國文課")                    
                    await self.channel.send("https://meet.google.com/rxj-qyih-jjp")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class3()) 


        async def class4():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "1140000":
                    await self.channel.send("下節是不能和老師當朋友的國防課")
                    await self.channel.send("https://meet.google.com/zzj-bzsn-kvo")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class4()) 


        async def class5():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "1150000":
                    await self.channel.send("下節是掛機體育課")
                    await self.chaannel.send("https://meet.google.com/mhd-mbha-xft")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class5()) 

#tuesday
        async def class6():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "20810000":
                    await self.channel.send("下節是紹偉的基電課")
                    await self.channel.send("https://meet.google.com/ypx-uwss-ssu")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class6())


        async def class7():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "2091000":
                    await self.channel.send("下節是英文課")
                    embed=discord.Embed(title="英文課", color=0xfd12ca)
                    embed.add_field(name="A組", value="https://meet.google.com/ijc-idvz-qxh?authuser=0", inline=False)
                    embed.add_field(name="B組", value="https://meet.google.com/lookup/bsi5jiarqn", inline=False)
                    embed.add_field(name="C組", value="https://meet.google.com/cfr-jqnj-unh", inline=False)
                    await self.channel.send(embed=embed)
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class7())


        async def class8():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "2111000":
                    await self.channel.send("下節是奇異果數學課")
                    await self.channel.send("https://meet.google.com/arv-ymyk-jfb")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class8())


        async def class9():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "2130000":
                    await self.channel.send("下節是掛機物理課")
                    await self.channel.sned("https://meet.google.com/hrr-mnrf-qzy?pli=1&authuser=2")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class9())


        async def class10():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "2140000":
                    await self.channel.send("連續兩節的國文課")
                    await self.channel.sned("https://meet.google.com/rxj-qyih-jjp")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class10())

#wed
        async def class11():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "3081000":
                    await self.channel.send("下節是英文")
                    embed=discord.Embed(title="英文課", color=0xfd12ca)
                    embed.add_field(name="A組", value="https://meet.google.com/ijc-idvz-qxh?authuser=0", inline=False)
                    embed.add_field(name="B組", value="https://meet.google.com/lookup/bsi5jiarqn", inline=False)
                    embed.add_field(name="C組", value="https://meet.google.com/cfr-jqnj-unh", inline=False)
                    await self.channel.send(embed=embed)
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class11())

        async def class12():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "3091000":
                    embed=discord.Embed(title="實習課", color=0xfd12ca)
                    embed.add_field(name="A組", value="https://meet.google.com/bpg-yyks-xbi", inline=False)
                    embed.add_field(name="B組", value="https://meet.google.com/kdv-hhih-cqd", inline=False)
                    await self.channel.send(embed=embed)
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class12())


        async def class13():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "3130000":
                    embed=discord.Embed(title="實習課", color=0xfd12ca)
                    embed.add_field(name="A組", value="https://meet.google.com/kdv-hhih-cqd", inline=False)
                    embed.add_field(name="B組", value="https://meet.google.com/bpg-yyks-xbi", inline=False)
                    await self.channel.send(embed=embed)
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class13())

#thursday
        async def class14():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "4081000":
                    await self.channel.send("下節是國文課")
                    await self.channel.send("https://meet.google.com/rxj-qyih-jjp")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class14())


        async def class15():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "4091000":
                    await self.channel.send("連續兩節的物理課")
                    await self.channel.sned("https://meet.google.com/hrr-mnrf-qzy?pli=1&authuser=2")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class15())


        async def class16():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "4111000":
                    await self.channel.send("下節是英文課")
                    embed=discord.Embed(title="英文課", color=0xfd12ca)
                    embed.add_field(name="A組", value="https://meet.google.com/ijc-idvz-qxh?authuser=0", inline=False)
                    embed.add_field(name="B組", value="https://meet.google.com/lookup/bsi5jiarqn", inline=False)
                    embed.add_field(name="C組", value="https://meet.google.com/cfr-jqnj-unh", inline=False)
                    await self.channel.send(embed=embed)
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class16())


        async def class17():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "4130000":
                    await self.channel.send("掛機體育課")
                    await self.channel.send("https://meet.google.com/mhd-mbha-xft")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class17())


        async def class18():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "4140000":
                    await self.channel.send("連續兩節奇異果的課")
                    await self.channel.sned("https://meet.google.com/njw-uutj-geb")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class18())

#friday
        async def class19():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "5081000":
                    await self.channel.send("兩節歷史課")
                    await self.channel.send("https://meet.google.com/bjp-zwdc-azy")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class19())


        async def class20():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "5101000":
                    await self.channel.send("奇異果的數學課課")
                    await self.channel.send("https://meet.google.com/yvs-xhau-xyc")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class20())


        async def class21():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "5130000":
                    await self.channel.send("社團課，放飛自我去")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class21())


        async def class22():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(981775025839423561)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%u%H%M%S")   
                if now_time == "5150000":
                    await self.channel.send("最後一節課:班會")
                    await self.channel.send("https://meet.google.com/ywv-wehx-qny")                    
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.bg_task =self.bot.loop.create_task(class22())


def setup(bot):
    bot.add_cog(onlineclass(bot))        