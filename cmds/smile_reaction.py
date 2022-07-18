from os import remove
import discord
from discord.ext import commands
from core.classes import cog_all

class reaction(cog_all):
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        #vitual signer
        if payload.message_id==987020543708499968:
            #miku
            if str(payload.emoji)=="<:miku:987022984898297857>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935466934001090570)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #rin
            elif str(payload.emoji)=="<:rin:987025131903791144>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935467469726953602)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #ren
            elif str(payload.emoji)=="<:ren:987025143215845427>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935467354102591499)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #ruka
            elif str(payload.emoji)=="<:ruka:987025158197895229>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935467601377779712)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #meiko
            elif str(payload.emoji)=="<:meiko:987025174475980801>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935467709028765696)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #kaito
            elif str(payload.emoji)=="<:kaito:987025184450035732>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935467817019518977)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
        #ln
        elif payload.message_id==987020793579978812:
            #一歌
            if str(payload.emoji)=="<:ichika:987028320153653319>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935468138621968454)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #咲希
            elif str(payload.emoji)=="<:saki:987028330098360340>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935467982644207646)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #穗波
            elif str(payload.emoji)=="<:honami:987028311064580156>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935468241638277212)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #志步
            elif str(payload.emoji)=="<:shiho:987028341070639104>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935468356914520074)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")    
        #mmj
        elif payload.message_id==987021144072785972:
            #實乃裡
            if str(payload.emoji)=="<:minori:987028435048235028>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935468725837131787)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #遙
            elif str(payload.emoji)=="<:haruka:987028424910585858>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935468572543692831)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #愛莉
            elif str(payload.emoji)=="<:airi:987028414043148338>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935468465886748752)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #娜
            elif str(payload.emoji)=="<:shizuku:987028444669939802>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935468988165664768)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")    
        #vbs
        elif payload.message_id==987021518225674281:
            #心羽
            if str(payload.emoji)=="<:kohane:987028484138348564>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935469243338723348)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #杏
            elif str(payload.emoji)=="<:an:987028473723899924>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935469378651177001)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #彰人
            elif str(payload.emoji)=="<:akito:987028463171018782>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935469637834002462)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #東彌
            elif str(payload.emoji)=="<:touya:987028494414413884>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935469510796902430)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")      
        #wxs
        elif payload.message_id==987021770970251334:
            #司
            if str(payload.emoji)=="<:tsukasa:987028551054266438>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935469727130734604)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #emu
            elif str(payload.emoji)=="<:emu:987028517449519115>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935469961042886726)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #nene
            elif str(payload.emoji)=="<:nene:987028527188680704>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935470204543176736)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #類
            elif str(payload.emoji)=="<:rui:987028539960328202>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935469819539619851)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")     
        #25
        elif payload.message_id==987021895687872582:
            #奏
            if str(payload.emoji)=="<:kanade:987028367440216154>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935470316581441546)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #真冬
            elif str(payload.emoji)=="<:mafuyu:987028376973877248>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935470460030824488)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #繪名
            elif str(payload.emoji)=="<:ena:987028358074351656>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935470594798026832)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #瑞希
            elif str(payload.emoji)=="<:mizuki:987028387988119623>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935470816768966706)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")  
        #其他 
        elif payload.message_id==988489517721866270:
            #boy
            if str(payload.emoji)=="♂️":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(962179014955507822)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")  
            #girl
            elif str(payload.emoji)=="♀️":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(962179082806771772)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組") 
            #evennot
            elif str(payload.emoji)=="<:evennot:988809449114325022>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(971790087652257823)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")    
            #youngboy    
            elif str(payload.emoji)=="<:youngboy:988811608509800458>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(974986953688776724)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")     
            #loli
            elif str(payload.emoji)=="<:unknown:969509611805753364>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(974985767019495474)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
            #getmsg
            elif str(payload.emoji)=="<:ghosthug:940529537530351626>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(976712882085564436)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
        elif payload.message_id==987020281233162362:
            #v #ln #mmj #vbs #ws #25 #boy #all
            role=["935470974554476544","935471090921263125","935471275831357490","935471644430987285","935471998908399676","935472212641714176","935472361417887774","935472448122531840"]            
            for i in role:
                if i in str(payload.member.roles):
                    print("yes")
                    guild=self.bot.get_guild(payload.guild_id)
                    user=guild.get_member(payload.user_id)
                    role=guild.get_role(int(i))
                    await user.remove_roles(role)                
                    channel=self.bot.get_channel(977121281361182750)
                    await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #vs
            if str(payload.emoji)=="<:vituralsinger:987627314605080576>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935470974554476544)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
                channe2=self.bot.get_channel(978292320984260648)
                message=await channe2.fetch_message(987020281233162362)
                await message.remove_reaction("<:vituralsinger:987627314605080576>",payload.member)
            #ln
            elif str(payload.emoji)=="<:ln:987627341117272104>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935471090921263125)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
                channe2=self.bot.get_channel(978292320984260648)
                message=await channe2.fetch_message(987020281233162362)
                await message.remove_reaction("<:ln:987627341117272104>",payload.member)
            #mmj
            elif str(payload.emoji)=="<:mmj:987627409379565579>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935471275831357490)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
                channe2=self.bot.get_channel(978292320984260648)
                message=await channe2.fetch_message(987020281233162362)
                await message.remove_reaction("<:mmj:987627409379565579>",payload.member)
            #vbs
            elif str(payload.emoji)=="<:vbs:987633106842419220>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935471644430987285)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
                channe2=self.bot.get_channel(978292320984260648)
                message=await channe2.fetch_message(987020281233162362)
                await message.remove_reaction("<:vbs:987633106842419220>",payload.member)
            #ws
            elif str(payload.emoji)=="<:ws:987627490057003029>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935471998908399676)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
                channe2=self.bot.get_channel(978292320984260648)
                message=await channe2.fetch_message(987020281233162362)
                await message.remove_reaction("<:ws:987627490057003029>",payload.member)
            #25
            elif str(payload.emoji)=="<:25:987627522634153994>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935472212641714176)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
                channe2=self.bot.get_channel(978292320984260648)
                message=await channe2.fetch_message(987020281233162362)
                await message.remove_reaction("<:25:987627522634153994>",payload.member)
            #boy
            elif str(payload.emoji)=="<:boys:987651954048127006>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935472361417887774)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
                channe2=self.bot.get_channel(978292320984260648)
                message=await channe2.fetch_message(987020281233162362)
                await message.remove_reaction("<:boys:987651954048127006>",payload.member)
            #all
            elif str(payload.emoji)=="<:all:989930102253043742>":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(935472448122531840)
                await payload.member.add_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{payload.member.mention} 已獲得 `{role}` 身分組")
                channe2=self.bot.get_channel(978292320984260648)
                message=await channe2.fetch_message(987020281233162362)
                await message.remove_reaction("<:all:989930102253043742>",payload.member)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        #vitual signer
        if payload.message_id==987020543708499968:
            #miku
            if str(payload.emoji)=="<:miku:987022984898297857>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935466934001090570)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #rin
            elif str(payload.emoji)=="<:rin:987025131903791144>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935467469726953602)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #ren
            elif str(payload.emoji)=="<:ren:987025143215845427>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935467354102591499)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #ruka
            elif str(payload.emoji)=="<:ruka:987025158197895229>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935467601377779712)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #meiko
            elif str(payload.emoji)=="<:meiko:987025174475980801>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935467709028765696)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #kaito
            elif str(payload.emoji)=="<:kaito:987025184450035732>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935467817019518977)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
        #ln
        elif payload.message_id==987020793579978812:
            #一歌
            if str(payload.emoji)=="<:ichika:987028320153653319>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935468138621968454)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #咲希
            elif str(payload.emoji)=="<:saki:987028330098360340>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935467982644207646)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #穗波
            elif str(payload.emoji)=="<:honami:987028311064580156>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935468241638277212)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #志步
            elif str(payload.emoji)=="<:shiho:987028341070639104>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935468356914520074)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")    
        #mmj
        elif payload.message_id==987021144072785972:
            #實乃裡
            if str(payload.emoji)=="<:minori:987028435048235028>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935468725837131787)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #遙
            elif str(payload.emoji)=="<:haruka:987028424910585858>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935468572543692831)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #愛莉
            elif str(payload.emoji)=="<:airi:987028414043148338>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935468465886748752)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #娜
            elif str(payload.emoji)=="<:shizuku:987028444669939802>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935468988165664768)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")    
        #vbs
        elif payload.message_id==987021518225674281:
            #心羽
            if str(payload.emoji)=="<:kohane:987028484138348564>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935469243338723348)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #杏
            elif str(payload.emoji)=="<:an:987028473723899924>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935469378651177001)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #彰人
            elif str(payload.emoji)=="<:akito:987028463171018782>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935469637834002462)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #東彌
            elif str(payload.emoji)=="<:touya:987028494414413884>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935469510796902430)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")      
        #wxs
        elif payload.message_id==987021770970251334:
            #司
            if str(payload.emoji)=="<:tsukasa:987028551054266438>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935469727130734604)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #emu
            elif str(payload.emoji)=="<:emu:987028517449519115>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935469961042886726)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #nene
            elif str(payload.emoji)=="<:nene:987028527188680704>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935470204543176736)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #類
            elif str(payload.emoji)=="<:rui:987028539960328202>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935469819539619851)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")     
        #25
        elif payload.message_id==987021895687872582:
            #奏
            if str(payload.emoji)=="<:kanade:987028367440216154>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935470316581441546)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #真冬
            elif str(payload.emoji)=="<:mafuyu:987028376973877248>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935470460030824488)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #繪名
            elif str(payload.emoji)=="<:ena:987028358074351656>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935470594798026832)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #瑞希
            elif str(payload.emoji)=="<:mizuki:987028387988119623>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(935470816768966706)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")   
        #其他 
        elif payload.message_id==988489517721866270:
            #boy
            if str(payload.emoji)=="♂️":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(962179014955507822)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")  
            #girl
            elif str(payload.emoji)=="♀️":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(962179082806771772)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組") 
            #evennot
            elif str(payload.emoji)=="<:evennot:988809449114325022>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(971790087652257823)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")    
            #youngboy    
            elif str(payload.emoji)=="<:youngboy:988811608509800458>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(974986953688776724)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")     
            #loli
            elif str(payload.emoji)=="<:unknown:969509611805753364>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(974985767019495474)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")
            #getmsg
            elif str(payload.emoji)=="<:ghosthug:940529537530351626>":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(976712882085564436)
                await user.remove_roles(role)
                channel=self.bot.get_channel(977121281361182750)
                await channel.send(f"{user.mention} 已移除 `{role}` 身分組")


def setup(bot):
    bot.add_cog(reaction(bot))
