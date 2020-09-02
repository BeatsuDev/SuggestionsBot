from discord.ext import commands

class AdministrationCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.shell = False

		app_info = await bot.application_info()
		self.bot_owner = app_info.owner


	@commands.command()
	@commands.bot_owner()
	@commands.is_dm()
	async def shell(self, ctx) -> None:
		"""Toggles a shell sorta - Basically to evaluate python expressions"""
		discord.Embed(title="Activated shell", colour=0x0f0)
		discord.Embed(title="De-activated shell", colour=0xf00)
		self.shell = True if not self.shell else False
		await ctx.send("Shell activated.") if self.shell else await ctx.send("Shell de-activated.")

	@commands.Cog.listener()
	async def on_message(self, msg) -> None:
		if not self.shell: return
		if msg.channel.type.private and msg.author == self.bot_owner:
			eval(msg.content)


def setup(bot):
	bot.add_cog(AdministrationCog(bot))