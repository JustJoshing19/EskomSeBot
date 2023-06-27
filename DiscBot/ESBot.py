import discord
from discord.ext import commands
from DiscBot.core import Config

class EskomSeBot(commands.Bot):
    async def on_ready(self):
        print("Logged in as a bot {0.user}".format(self))

    async def on_message(self, message: discord.Message):
        print('#')
        await self.process_commands(message)

EDBot = EskomSeBot(intents=Config.botIntents, command_prefix=Config.comPrefix)

#### Commands ####
@EDBot.command()
async def ping(ctx):
    await ctx.send('Pong!')