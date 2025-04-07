import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Replies with bot latency")
    async def ping(self, interaction: Interaction):
        latency = int(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! My ping is {latency} ms.")

def setup(bot):
    bot.add_cog(Util(bot))