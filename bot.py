import discord, os, asyncio, logging
from discord.ext import commands
from dotenv import load_dotenv
from rich.console import Console

class AnonBot(commands.Bot):
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("DISCORD_TOKEN")
        self.test_guild_id = int(os.getenv("GUILD_ID")) if os.getenv("GUILD_ID") else None
        
        gateway_log = logging.getLogger("discord.gateway")
        client_log = logging.getLogger("discord.client")
        commands_log = logging.getLogger("discord.ext.commands")
        gateway_log.setLevel(logging.CRITICAL)
        client_log.setLevel(logging.CRITICAL)
        commands_log.setLevel(logging.CRITICAL)

        intents = discord.Intents.default()
        super().__init__(command_prefix=".", intents=intents)
    
    async def setup_hook(self):
        console = Console()
        
        console.print("[bold purple]==================================================[/]")
        console.print("⚡ [bold magenta]STARTING ANONBOT CORE SYSTEM[/] ⚡")
        console.print("[bold purple]==================================================[/]")
        print()
        
        with console.status("[bold purple]Initializing system internals...", spinner="dots") as status:
            await asyncio.sleep(1.5)
            status.update("[bold cyan]Cleaning environment variables...")
            await asyncio.sleep(0.8)

        console.print("[bold green]✔ System internals ready![/]")
        print()

        console.print("[bold white][+] Loading modules (Cogs)...[/]")
        cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
        
        for filename in os.listdir(cogs_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                cog_name = filename[:-3]
                try:
                    await self.load_extension(f"cogs.{cog_name}")
                    console.print(f"   [bold green]↳[/] [green]Loaded extension:[/] [bold cyan]{cog_name}[/]")
                except Exception as e:
                    console.print(f"   [bold red]↳[/] [red]Failed to load:[/] [bold yellow]{cog_name}[/] -> [dim]{e}[/]")
                    
        if self.test_guild_id:
            console.print(f"\n[bold white][+] Deploying commands to guild ID:[/] [bold yellow]{self.test_guild_id}[/]")
            guild = discord.Object(id=self.test_guild_id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            
            print()
            console.print("[bold purple]==================================================[/]")
            console.print("✨ [bold green]ALL SLASH COMMANDS SYNCHRONIZED AND READY![/] ✨")
            console.print("[bold purple]==================================================[/]")
            print()
        else:
            console.print("\n[bold red]❌ Error: GUILD_ID environment variable not set in .env[/]")

    async def on_ready(self):
        console = Console()
        console.print(f"🤖 [bold green]Logged in as:[/] [bold white]{self.user}[/] [dim](ID: {self.user.id})[/]")
        console.print("[bold purple]--------------------------------------------------[/]")

    def start_bot(self):
        """Pomocná metoda pro bezpečné spuštění bota zvenčí třídy."""
        console = Console()
        if not self.token:
            console.print("[bold red]❌ Error: DISCORD_TOKEN environment variable not set in .env[/]")
        else:
            self.run(self.token)

if __name__ == "__main__":
    bot = AnonBot()
    bot.start_bot()
