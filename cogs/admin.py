from discord.ext import commands

class Admin(commands.Cog):
    "Administrative Commands."
    def __init__(self, client):
        self.client = client
    @commands.command(aliases=["add"])
    @commands.is_owner()
    async def load(self, ctx, *, module: str):
        """Loads an Extension.

        Parameters
        ----------
        module: str
            The name of the module."""
        await self.client.load_extension(module)
        await ctx.send(f"{module} Cog Loaded Sucessfully!")

    @commands.command(aliases=["remove"])
    @commands.is_owner()
    async def unload(self, ctx, *, module: str):
        """UnLoads an Extension.

        Parameters
        ----------
        module: str
            The name of the module."""
        await self.client.unload_extension(module)
        await ctx.send(f"{module} Cog Unloaded Sucessfully!")

    @commands.command(aliases=["b"])
    @commands.is_owner()
    async def reload(self, ctx, *, module: str):
        """Reloads an Extension.

        Parameters
        ----------
        module: str
            The name of the module."""
        await self.client.reload_extension(module)
        await ctx.send(f"{module} Cog Reloaded Sucessfully!")
        

async def setup(client):
    await client.add_cog(Admin(client))
    print("Admin Cog Loaded")

async def teardown(client):
    print("Admin Cog Unloaded")
    