import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
import random
from setup import contains_link

class Fun(commands.Cog):
    """Make the bot say whatever you want to or make it reply to a message you can edit later on. Yeah this is funnnnnn.
Oh and also, There's 8Ball."""
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True)
    async def say(self, ctx, *, msg:str):
        """Says the Text.

        Parameters
        ----------
        msg: str
            The message you want me to send.

        """
        if contains_link(msg):
            await ctx.reply("nah fam, won't let you send links")
        else:
            await ctx.send(msg)

    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True)
    async def reply(self, ctx, *, msg:str):
        """Repeats the Text.

        Parameters
        ----------
        msg: str
            The message you want me to reply.

        """
        if contains_link(msg):
            await ctx.reply("nah fam, won't let you send links", self.client)
        else:
            await ctx.reply(msg)
    
    @commands.hybrid_command(name='8ball')
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    #@discord.app_commands.describe(question="Question")
    async def _8ball(self, ctx, *, question:str):#=commands.Parameter(description="A yes/no question")
        """Ask a Yes or No question and get a response.

        Parameters
        ----------
        question: str
            A Yes/No type of Question.
        """
        if question==None:
            await ctx.reply("You must include a question")
        else:
            "Ask a Question and get an answer. Can't be more simple."
            answers = ('As I see it, yes.', 'Ask again later.',
                    'Better not tell you now.', 'Cannot predict now.',
                    'Concentrate and ask again.', 'Don’t count on it.',
                    'It is certain.', 'It is decidedly so.', 'Most likely.',
                    'My reply is no.', 'My sources say no.',
                    'Outlook not so good.', 'Outlook good.',
                    'Reply hazy, try again.', 'Signs point to yes.',
                    'Very doubtful.', 'Without a doubt.', 'Yes.',
                    'Yes – definitely.', 'You may rely on it.')
            emb = discord.Embed(
                description=f"Question: {question}\nAnswer: {random.choice(answers)}",
                color=discord.Colour.blurple())
            emb.set_author(name=f"Hold it Everyone! {ctx.author.name} just asked a Question",icon_url=ctx.author.display_avatar.url)
            emb.timestamp = datetime.now()
            if not contains_link(question):
                await ctx.send(embed=emb)
            else:
                await ctx.send("Nah fam, can't let you post links")
async def setup(client):
    await client.add_cog(Fun(client))
    print("Fun Cog Loaded")

async def teardown(client):
    print("Fun Cog Unloaded")