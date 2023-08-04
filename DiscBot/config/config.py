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
    comPrefix: str = environ["PREFIX"]
    
    #### Set Text-Channel ####
    textChannel:str = environ['TCHANNEL']

    #### Get Token ####
    load_dotenv()
    ESPToken: str = environ['ESPTOKEN']

class DataBase:
    load_dotenv()
    dbName: str = environ['DBNAME']