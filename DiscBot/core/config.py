from os import environ
from dotenv import load_dotenv
from discord import Intents

class Config:
    #### Get Token ####
    load_dotenv()
    Token: str = environ['TOKEN']
    
    #### Set Intents ####
    botIntents: Intents = Intents.default()
    botIntents.message_content = True

    #### Set Command Prefix ####
    comPrefix: str = "!"