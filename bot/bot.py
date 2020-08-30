import os

from discord.ext import commands


class SuggestionsBot(commands.Bot):
    def __init__(self, prefix: str) -> commands.Bot:
        super().__init__(command_prefix=commands.when_mentioned_or(prefix))

    def load_cogs(self):
        for cog in os.listdir('bot/cogs/'):
            if cog.endswith('.py'):
                self.load_extension(f"bot.cogs.{cog[:-3]}")

    async def on_ready(self):
        print(f"We're ready! Connected to {len(self.guilds)} guilds and "
              f"{len(self.users)} users! "
              f"Connected as {self.user.name}#{self.user.discriminator}")
        self.load_cogs()
