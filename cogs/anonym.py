import discord, os
from discord import app_commands
from discord.ext import commands

SEND_CHANNEL_ID = int(os.getenv("SEND_CHANNEL_ID")) if os.getenv("SEND_CHANNEL_ID") else None
POST_CHANNEL_ID = int(os.getenv("POST_CHANNEL_ID")) if os.getenv("POST_CHANNEL_ID") else None

class AnonymCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="send", description="Sends an anonymous message (works only in the dedicated channel)")
    @app_commands.describe(message="Text of the message you want to send anonymously")
    @app_commands.checks.cooldown(rate=1, per=5.0, key=lambda i: i.user.id)
    async def send_anonym(self, interaction: discord.Interaction, message: str):
        
        if not SEND_CHANNEL_ID or not POST_CHANNEL_ID:
            await interaction.response.send_message(
                "❌ Bot is not properly configured. Missing SEND_CHANNEL_ID or POST_CHANNEL_ID in .env.", 
                ephemeral=True
            )
            return

        if interaction.channel_id != SEND_CHANNEL_ID:
            source_channel = self.bot.get_channel(SEND_CHANNEL_ID)
            mention_text = source_channel.mention if source_channel else "unknown channel"
            await interaction.response.send_message(
                f"🛑 You can't send it here! Anonymous messages can only be written in the channel. {mention_text}.", 
                ephemeral=True
            )
            return

        target_channel = self.bot.get_channel(POST_CHANNEL_ID)
        if not target_channel:
            await interaction.response.send_message(
                "❌ Target channel does not exist or bot cannot see it. Please check POST_CHANNEL_ID in .env.", 
                ephemeral=True
            )
            return

        await interaction.response.send_message("🔒 Your message has been safely and anonymously sent.", ephemeral=True)


        embed = discord.Embed(
            title="🤫 Anonymous confession",
            description=message,
            color=discord.Color.dark_purple()
        )
        embed.set_footer(text="Identity of the author is hidden!")

        await target_channel.send(embed=embed)

    @send_anonym.error
    async def send_anonym_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(
                f"🛑 Slow down! You can send another anonymous message at {error.retry_after:.1f} seconds.", 
                ephemeral=True
            )
        else:
            raise error

async def setup(bot):
    await bot.add_cog(AnonymCog(bot))
