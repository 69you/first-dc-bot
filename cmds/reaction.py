from os import remove
import discord
from discord.ext import commands
from core.classes import cog_all

class reaction(cog_all):
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        #噴子
        if payload.message_id==1000648991488364706:
            #miku
            if str(payload.emoji)=="✅":
                guild=self.bot.get_guild(payload.guild_id)
                role=guild.get_role(1000479626759520366)
                await payload.member.add_roles(role)
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        #噴子
        if payload.message_id==1000648991488364706:
            if str(payload.emoji)=="✅":
                guild=self.bot.get_guild(payload.guild_id)
                user=guild.get_member(payload.user_id)
                role=guild.get_role(1000479626759520366)
                await user.remove_roles(role)


def setup(bot):
    bot.add_cog(reaction(bot))
