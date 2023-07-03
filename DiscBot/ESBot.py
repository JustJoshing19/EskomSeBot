import discord
from discord.ext import commands
from .core import Config
from .EskomSePush import ESP_API_Client


class EskomSeBot(commands.Bot):
    def __init__(self, intents, command_prefix):
        super().__init__(intents=intents, command_prefix=command_prefix)

    async def on_ready(self):
        print("Logged in as a bot {0.user}".format(self))

    async def on_message(self, message: discord.Message):
        print('#')
        await self.process_commands(message)

EDBot = EskomSeBot(intents=Config.botIntents, command_prefix=Config.comPrefix)

#### Commands ####
@EDBot.command()
async def join(ctx: commands.context):
    author: discord.Member = ctx.author
    print(author.name)

@EDBot.command()
async def loadshedding(ctx: commands.context):
    espclient = ESP_API_Client()
    times: dict = espclient.getLoadsheddingTimes()
    messages:str = ''
    
    for name, period in times.items():
        messages = '{}{}: {} to {}\n'.format(messages, name, period[0], period[1])
    
    print(messages)
    await ctx.send(messages)