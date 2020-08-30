from discord.ext import commands

class Suggestions(commands.Cog):
    def __init__(self, bot) -> commands.Cog:
        self.bot = bot

    @commands.command()
    async def sayd(self, ctx, *, content) -> None:
        try:
            await ctx.message.delete()
        except Exception as e:
            await ctx.send("Couldn't delete that message!")
            print(e)
            return

        await ctx.send(content)


def setup(bot):
    bot.add_cog(Suggestions(bot))
