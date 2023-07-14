from DiscBot import EDBot
from DiscBot.config import Config

def main():
    bot = EDBot
    EDBot.load_extension()
    EDBot.run(Config.Token)

if __name__ == '__main__':
    main()