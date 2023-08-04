import asyncio
from typing import Optional
import discord
from discord.ext import commands
from .config import Config


class EskomSeBot(commands.Bot):
    """Takes discord member input and sends loadshedding times.
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

        if message.author != self.user:
            print('#')
            print('User message being processed.')
            print('#')

            if message.channel.name != Config.textChannel:
                await message.reply("Please enter commands in {}".format(Config.textChannel))
                await message.delete()
                return
            
            await self.process_commands(message)

    def load_extension(self):
        asyncio.run(super().load_extension('DiscBot.cogs.cogs'))

EDBot = EskomSeBot(intents=Config.botIntents, command_prefix=Config.comPrefix)