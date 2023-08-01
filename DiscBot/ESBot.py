import asyncio
from typing import Optional
import discord
from discord.ext import commands
from .DiscViews import AreaSelectView
from .config import Config
from .EskomSePush import ESP_API_Client


class EskomSeBot(commands.Bot):
    """Takes discord member input and sends loadshedding times
    """

    def __init__(self, intents, command_prefix):
        super().__init__(intents=intents, command_prefix=command_prefix)

    async def on_ready(self):
        """Prints logged in bot information.
        """
        print("Logged in as a bot {0.user}".format(self))

    async def on_message(self, message: discord.Message):
        """Processes any commands given to the bot.

        Parameters
        ----------
        message : discord.Message
            Message sent by discod member. Can be command with or without arguments.
        """
        
        print('#')
        await self.process_commands(message)

    def load_extension(self):
        asyncio.run(super().load_extension('DiscBot.modules.utils'))

EDBot = EskomSeBot(intents=Config.botIntents, command_prefix=Config.comPrefix)

#### Commands ####
@EDBot.command()
async def join(ctx: commands.context, args = None):
    """Command to add discord member to list of loadshedding affected users.

    Parameters
    ----------
    ctx : commands.context
    args : _type_, optional
    """
    
    espclient = ESP_API_Client()
    areas = await espclient.getAllAreas()
    selectView = AreaSelectView(area=areas, espclient=espclient, timeout=60)
    await ctx.send("Choose and Area", view=selectView)

@EDBot.command()
async def loadshedding(ctx: commands.context):
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