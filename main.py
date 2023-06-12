from typing import Any, Optional, Type
import discord
from discord import app_commands
from discord.ext import commands
import os

class Client(commands.Bot):
    def __init__(self):
        intent = discord.Intents.all()
        intent.members = True
        super().__init__(command_prefix=('B ','b '),
            case_insensitive=True,
            intents=intent,
            help_command=commands.DefaultHelpCommand(no_category='Help'),
            allowed_mentions=discord.AllowedMentions(everyone=False,roles=False)
        )
    async def on_ready(self):
        print(f'{client.user} has connected to Discord')
    
    async def setup_hook(self):
        for f in os.listdir("Betman2.0/cogs"):
            if f.endswith(".py"):
                await client.load_extension("cogs." + f[:-3])
        scmds = await self.tree.sync()
        self.strip_after_prefix=True
        print(f"{len(scmds)} slash commands loaded")
        for cmd in scmds:
            print(cmd.name,end=', ')
        print()

client = Client()
client.run("Your-Token-Here")
