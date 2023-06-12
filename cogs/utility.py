from typing import Optional
import discord
from discord.ext import commands
from discord import app_commands
from time import time
from datetime import datetime

ctime=int(time())

class Utility(commands.Cog):
    """
    Utility related Commands.
    """
    def __init__(self,client):
        self.client=client
    
    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True)
    async def ping(self,ctx):
        """Shows my Ping... That's it."""
        await ctx.send(f"Pong! `{round(self.client.latency * 1000)}ms`")

    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True)
    async def uptime(self,ctx):
        """Shows how long i've been online for."""
        await ctx.send(f"I am up and running since <t:{ctime}:R>")
    
    @commands.hybrid_command(aliases=["Link"])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def invite(self, ctx):
        """Returns My Invite Links."""
        emb = discord.Embed(colour=discord.Colour.green())
        emb.add_field(
            name="Invite Links",
            value=
            """[Add me](https://discord.com/api/oauth2/authorize?client_id=817740081972510740&permissions=2218126400&scope=bot)
            [Support Server](https://discord.gg/ea3wBuwXPF)""")

        emb.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
        emb.timestamp = datetime.now()
        await ctx.reply(embed=emb)
    
    @commands.hybrid_command(name="avatar", aliases=['av', 'pfp', 'image'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def avatar(self, ctx, *,member: discord.Member=None): #not using converters to bypass warnings
        """Shows User's Avatar.
        
        Parameters
        ----------
        member : str, optional
            A Server Member."""
        if member==None: member=ctx.author
        emb = discord.Embed(
            colour=discord.Colour.blurple(),
            title="oww I definitely don't know what this link does :point_down: ",
            description=f"[Click me!]({member.display_avatar.url})")
        emb.set_author(name=f"{member.name}'s avatar", icon_url=member.display_avatar.url)
        emb.set_image(url=member.display_avatar.url)
        emb.set_footer(text=f"Requested by {ctx.author}",
                    icon_url=ctx.author.avatar.url)
        emb.timestamp = datetime.now()
        await ctx.send(embed=emb)

    @commands.hybrid_command(aliases=['userinfo'])
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def user(self, ctx, member: discord.Member=lambda ctx:ctx.author):
        """Shows User's Info.
        
        Parameters
        ----------
        member : str, optional
            A Server Member."""
        date_format = "%a, %d %b %Y %I:%M %p"
        emb = discord.Embed(color=ctx.author.color, description=member.mention,colour=discord.Color.blurple())
        emb.set_author(name=f"{member.name}'s info", icon_url=member.display_avatar.url)
        emb.set_thumbnail(url=member.display_avatar.url)
        emb.add_field(name="Created At",
                      value=member.created_at.strftime(date_format),
                      inline=True)
        if not isinstance(ctx.channel, discord.DMChannel) and member.roles != 1:
            emb.add_field(name="Joined At",
                          value=member.joined_at.strftime(date_format),# type: ignore
                          inline=True)
            text = ' '.join([r.mention for r in member.roles][:0:-1])
            if text == '':
                text = "None"
            if len(text) > 1024:
                text = f"Value beyond character limit ({len(text)}/1024)"
            emb.add_field(name=f"Roles [{len(member.roles)-1}]",
                          value=text,
                          inline=False)
        if not isinstance(ctx.channel, discord.DMChannel):
            text = ', '.join([
                p[0].replace('_', ' ').title() for p in member.guild_permissions
                if p[1]
            ])
            if text == '':
                text = "None"
            emb.add_field(name="Permissions", value=text)
        emb.set_footer(text=f"Requested by {ctx.author}",
                       icon_url=ctx.author.avatar.url)
        emb.timestamp = datetime.now()
        await ctx.send(embed=emb)
    
    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True,attach_files=True)
    async def patchnotes(self,ctx):
        """Stay updated with the latest changes in the bot."""
        await ctx.send(f"""`Patch Notes for {self.client.user.name}, My second bot
Contains every change. Only continue if you are Super Bored`""",
    file=discord.File("Betman2.0/patchnotes.txt"))

    @commands.hybrid_command(with_app_command=False)
    @commands.is_owner()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def servers(self, ctx):
        """Shows every Server i'm in, in a .txt file."""
        message=await ctx.author.send("Please Wait...")
        with open ("Guilds.txt",'w') as guild_file:
            i=0
            for guild in self.client.guilds:
                i+=1
                guild_file.write(f"[{guild.id}] {guild.name}\n")
        await message.edit(content=f"Total Servers = {i}",attachments=[discord.File("Guilds.txt")])

    @commands.hybrid_command(with_app_command=False, aliases=["Servers2"])
    @commands.is_owner()
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def serversembed(self, ctx):
        """Shows every Server i'm in, in a nice Embed."""
        message=await ctx.author.send("Please Wait...")
        emb = discord.Embed(colour=discord.Colour.blue())
        emb.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
        i=0
        for guild in self.client.guilds:
            i+=1
            emb.add_field(name=guild.name, value=guild.id)
        await message.edit(content=f"Total Servers = {i}",embeds=[emb])

async def setup(client):
    await client.add_cog(Utility(client))
    client.help_command.cog=Utility(client)
    print("Utility Cog Loaded")

async def teardown(client):
    client.help_command.cog=None
    print("Utility Cog Unloaded")