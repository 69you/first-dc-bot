import discord
from discord.ext import commands
import datetime
from core.classes import cog_all


class user(cog_all):
    @commands.command(aliases=["uinfo"])
    async def userinfo(self,ctx,user:discord.Member=None):
        if user==None:
            user=ctx.author
        embed=discord.Embed(title="使用者訊息", description=" ", color=0xfd12ca)
        embed.set_author(name="人工智障取得的資料", icon_url="https://cdn.discordapp.com/emojis/990679568153190430.gif?size=4096")  
        #embed.set_image(url="https://media.discordapp.net/attachments/977142865836802059/1000298935719575632/undefined_-_Imgur.gif")
        icon=user.avatar_url_as(format="png")
        embed.set_thumbnail(url=f"{icon}")   
        embed.add_field(name="`使用者名稱`",value=f"{user.name}#{user.discriminator}",inline=True)
        if user.nick==None:
            embed.add_field(name="`伺服器暱稱`",value="無設定暱稱",inline=True)
        else:
            embed.add_field(name="`伺服器暱稱`",value=f"{user.nick}",inline=True)
        embed.add_field(name="`使用者id`",value=f"{user.id}",inline=True)   
        embed.add_field(name="`使用者帳號色彩`",value=f"{user.color}",inline=True)
        ctime=str(user.created_at)
        embed.add_field(name="`創建帳號時間`",value=f"{ctime[:-7]}",inline=True)
        jtime=str(user.joined_at) 
        embed.add_field(name="`加入伺服器時間`",value=f"{jtime[:-7]}",inline=True)  
        memper=user.guild_permissions
        per=[] 
        perlist=""
        if user==ctx.guild.owner:
            per.append("`群主`")
        if memper.administrator==True:
            per.append("`管理員`")
        if memper.manage_guild==True:
            per.append("`管理伺服器`")
        if memper.manage_roles==True:
            per.append("`管理身分組`")
        if memper.manage_channels==True:
            per.append("`管理頻道`")
        if memper.manage_messages==True:
            per.append("`管理訊息`")
        if memper.manage_emojis==True:
            per.append("`管理表情符號`")
        if memper.manage_nicknames==True:
            per.append("`管理暱稱`")
        if memper.manage_webhooks==True:
            per.append("`管理 webhooks`")
        if memper.mute_members==True:
            per.append("`禁言成員`")
        if memper.kick_members==True:
            per.append("`踢除成員`")
        if memper.ban_members==True:
            per.append("`停權成員`")
        if memper.move_members==True:
            per.append("`移動成員`")
        if memper.create_instant_invite==True:
            per.append("`生成邀請連結`")
        if memper.mention_everyone==True:
            per.append("`提及@everyone`")
        if len(per)==0:
            perlist+="無"
        else:  
            for i in range(0,len(per)):     
                if((i+1)%5==0):
                    perlist+=f"{per[i]}\n"
                else:
                    perlist+=f"{per[i]}**   **"
        embed.add_field(name="此成員的特殊權限",value=f"{perlist}",inline=False)   
        role=[]
        rolelist=""
        for i in range(len(user.roles)-1,0,-1):
            role.append(user.roles[i].mention)  
        if len(role)==0:
            rolelist+="無"
        else:
            for i in range(0,len(role)):
                if((i+1)%4==0):
                    rolelist+=f"{role[i]}\n"
                else:
                    rolelist+=f"{role[i]}**  **"
        embed.add_field(name="使用者身分組",value=f"{rolelist}",inline=True)
        time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
        embed.set_footer(text=f"資料取得時間: {time}")
        await ctx.send(embed=embed)


class server(cog_all):
    @commands.command(aliases=["sinfo"])
    async def serverinfo(self,ctx):
        guild=ctx.guild
        if guild.banner_url=="":
            embed=discord.Embed(title="伺服器訊息", description=" ", color=0xfd12ca)
        else:
            banner=guild.banner_url_as(format="png")
            embed=discord.Embed(title="伺服器訊息",url=f"{banner}", description=" ", color=0xfd12ca)
        embed.set_author(name="人工智障取得的資料", icon_url="https://cdn.discordapp.com/emojis/990679568153190430.gif?size=4096")
        #embed.set_image(url="https://media.discordapp.net/attachments/977142865836802059/1000298935719575632/undefined_-_Imgur.gif")
        icon=guild.icon_url_as(format="png")
        embed.set_thumbnail(url=f"{icon}")
        embed.add_field(name="`伺服器名稱`", value=f"{guild.name}", inline=True)
        embed.add_field(name="`伺服器擁有者`", value=f"{guild.owner.mention}", inline=True)
        time=str(guild.created_at)
        embed.add_field(name="`伺服器創建時間`", value=f"{time[:-7]}", inline=True)
        member=0
        for i in guild.members:
            if i.bot==False:
                member+=1
        embed.add_field(name=" `伺服器人數`", value=f"{member}", inline=True)
        bot=0
        for i in guild.members:
            if i.bot==True:
                bot+=1        
        embed.add_field(name="`機器人數量`", value=f"{bot}", inline=True)
        embed.add_field(name="** ** ", value="** ** ", inline=True)
        online=0
        idle=0
        dnd=0
        offline=0
        for i in ctx.guild.members:
            if str(i.status)=="online":
                online+=1
            elif str(i.status)=="idle":
                idle+=1
            elif str(i.status)=="dnd" or str(i.status)=="do_not_disturb":
                dnd+=1
            elif str(i.status)=="offline":
                offline+=1
        embed.add_field(name=f"``上線人數:``",value=f"{online}",inline=True)
        embed.add_field(name=f"``閒置人數:``",value=f"{idle}",inline=True)
        embed.add_field(name=f"``勿擾人數:``",value=f"{dnd}",inline=True)
        categories=0
        for i in guild.categories:
            categories+=1
        embed.add_field(name="`類別數量`", value=f"{categories}", inline=True)
        cha=0
        for i in guild.text_channels:
            cha+=1
        embed.add_field(name="`文字頻道數量`", value=f"{cha}", inline=True)
        vcha=0
        for i in guild.voice_channels:
            vcha+=1
        embed.add_field(name="`語音頻道數量`", value=f"{vcha}", inline=True)
        role=0
        for i in guild.roles:
            role+=1
        embed.add_field(name="`身分組數量`", value=f"{role}", inline=True)
        toprole=guild.roles[-1]
        embed.add_field(name="`最高身分組`", value=f"{toprole.mention}", inline=True)       
        emoji=0
        for i in guild.emojis:
            emoji+=1
        embed.add_field(name="`表情符號數量`", value=f"{emoji}", inline=True)
        embed.add_field(name="`伺服器加成等級`", value=f"{guild.premium_tier}", inline=True)
        embed.add_field(name="`伺服器加成數量`", value=f"{guild.premium_subscription_count}", inline=True)
        boost=""
        for i in guild.premium_subscribers:
            boost+=i.mention+"** **" 
        if boost=="":     
            embed.add_field(name="`伺服器加成人員`", value=f"無", inline=True)
        else:
            embed.add_field(name="`伺服器加成人員`", value=f"{boost}", inline=True)   
        #ttcount=0
        #for i in ctx.guild.text_channels:
            #for j in await i.pins():
                #ttcount+=1
        #embed.add_field(name="``伺服器總釘選訊息:``",value=f"{ttcount}",inline=True)        
        a=str(bool(guild.large))      
        if a=="False": 
            large="否"
        elif a=="True": 
            large="是"
        embed.add_field(name="`是否屬於大型伺服器`", value=f"{large}", inline=True)
        if guild.mfa_level==0: 
            twofa="否"
        elif guild.mfa_level==0: 
            twofa="是"
        embed.add_field(name="`是否需要開啟2fa認證`", value=f"{twofa}", inline=True)
        time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y /%m /%d  %H :%M :%S")
        embed.set_footer(text=f"資料取得時間: {time}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(user(bot))
    bot.add_cog(server(bot))