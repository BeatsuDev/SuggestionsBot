import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx) -> None:
        """Shows a help message"""
        embed = discord.Embed(colour=0xff0)
        for cmd in self.bot.commands:
            embed.add_field(name=cmd.name,
                            value=f"{cmd.brief}\n\nUsage: {cmd.usage}",
                            inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCog(bot))
