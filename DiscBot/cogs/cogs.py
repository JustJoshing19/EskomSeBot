from typing import Optional

import discord
from discord import Guild, TextChannel
from discord.ext import commands

from DiscBot.config import Config
from DiscBot.DiscViews import AreaSelectView
from DiscBot.EskomSePush  import ESP_API_Client

class CustomHelpCommand(commands.HelpCommand):
    pass

class LoadsheddingCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send('Pong!')

    @commands.command()
    async def echo(self, ctx: commands.Context, *args):
        """Echos anything typed after the command back to the user.

        Parameters
        ----------
        ctx : commands.Context
        """
        echo = ""
        for a in args:
            echo = echo + a + " "
        await ctx.send(echo.strip())

    @commands.command()
    async def join(self, ctx: commands.context, args = None):
        """Command to add discord member to list of loadshedding affected users.

        Parameters
        ----------
        ctx : commands.context
        args : _type_, optional
        """
        
        espclient = ESP_API_Client()
        areas = await espclient.getAllAreas()
        selectView = AreaSelectView(area=areas, espclient=espclient, timeout=None)
        await ctx.send("Choose and Area", view=selectView)

    @commands.command()
    async def loadshedding(self, ctx: commands.context):
        """Gets loadshedding times for all discord members on the watchlist.

        Parameters
        ----------
        ctx : commands.context
        """
        espclient = ESP_API_Client()
        times: dict = espclient.getLoadsheddingTimes()
        messages:str = ''
        
        for name, period in times.items():
            messages = '{:>20}{}: {} to {}\n'.format(messages, name, period[0], period[1])
        
        print(messages)
        await ctx.send(messages)

    @commands.Cog.listener()
    async def on_guild_join(self, guild: Guild):
        """Creates a new text channel when added to a new server.

        Parameters
        ----------
        guild : Guild
            The guild the bot joined when event was triggered.
        """
        await guild.create_text_channel(Config.textChannel)
        
        for channel in guild.text_channels:
            if channel.name == Config.textChannel:  # TODO change to custom bot channel name, update to only post in this channel
                await channel.send("Hello")

async def setup(bot: commands.Bot):
    await bot.add_cog(LoadsheddingCommands(bot))