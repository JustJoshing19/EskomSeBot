import discord
from discord import utils
from discord import Guild, TextChannel
from discord.ext import commands

class CustomHelpCommand(commands.HelpCommand):
    pass

class LoadsheddingCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context, args):
        await ctx.send(args)

    @commands.Cog.listener()
    async def on_guild_join(self, guild: Guild):
        await guild.create_text_channel('bot-channel')
        
        for channel in guild.text_channels:
            if channel.name == 'bot-channel':   # TODO change to custom bot channel name, update to only post in this channel
                await channel.send("Hello")

async def setup(bot: commands.Bot):
    await bot.add_cog(LoadsheddingCommands(bot))