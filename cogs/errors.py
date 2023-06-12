import discord
from discord.ext import commands
from datetime import datetime
import random
from setup import contains_link

class Errors(commands.Cog):
    """Error Handlers"""
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx:commands.Context,error):
        if isinstance(error,commands.CommandNotFound):
            await ctx.reply(f"🚫 Command `{ctx.invoked_with}` is not found")
        elif isinstance(error,commands.MissingRequiredArgument):
            await ctx.reply(f"""🚫 Missing Argument(s) in `{ctx.invoked_with}`: `{error.param}`
use `{ctx.prefix}help {ctx.invoked_with}` for more information on how to use the command""")#\n{ctx.send_help(str(ctx.command))}
        elif isinstance(error,commands.BadArgument):
            await ctx.reply(f"""🚫 Invalid Argument(s) Passed in `{ctx.invoked_with}`: {', '.join(error.args)}.
use `{ctx.prefix}help {ctx.invoked_with}` for more information on how to use the command""")
        elif isinstance(error,commands.BotMissingPermissions):
            if 'send_messages' not in error.missing_permissions:
                await ctx.reply(f"🚫 I lack the permission(s) `{', '.join(error.missing_permissions)}` to execute the command: ")
        else:
            raise error

async def setup(client):
    await client.add_cog(Errors(client))
    print("Errors Cog Loaded")

async def teardown(client):
    print("Errors Cog Unloaded")