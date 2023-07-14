import discord
from discord.ext import commands

class CustomHelpCommand(commands.HelpCommand):
    pass

class LoadsheddingCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context, args):
        await ctx.send(args)

async def setup(bot: commands.Bot):
    await bot.add_cog(LoadsheddingCommands(bot))