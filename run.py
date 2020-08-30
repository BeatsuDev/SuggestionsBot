import os

from bot.bot import SuggestionsBot

if __name__ == '__main__':
    bot = SuggestionsBot(os.environ.get("PREFIX", "srz!"))
    bot.run(os.environ.get('TOKEN', '<-insertTokenHereIfNotSetInEnvironment->'))
