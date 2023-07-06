from os import environ
from dotenv import load_dotenv

class Config:
    #### Get Token ####
    load_dotenv()
    Token: str = environ['ESPTOKEN']

class DataBase:
    load_dotenv()
    dbName: str = environ['DBNAME']