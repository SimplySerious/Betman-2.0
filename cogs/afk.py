import discord
from discord.ext import commands
#from replit import db #since the bot is hosted on replit, data is stored in repl's database
from time import time
from setup import contains_link

#following two lines are for debugging only
db={}
db["afkdict"]={}

class AFK(commands.Cog):
    """AFK related commands."""
    def __init__(self, client):
        self.client = client
        try:
            self.afkdict=db["afkdata"]
            en='\n'
        except:
            print("imported a new database")
            self.afkdict={}
            db["afkdata"]=self.afkdict

    def afksave(self):#copies data from memory to storage
        db["afkdata"] = self.afkdict
    
    @commands.Cog.listener()
    async def on_message(self,msg:discord.Message):
        if not msg.author.bot and len(msg.content)!=0 and msg.content[0]!='=' and msg.channel.permissions_for(msg.channel.guild.me).send_messages and True not in [str(msg.content).startswith(p) for p in self.client.command_prefix]:
            for ping in msg.mentions:#alerting users that the pinged guy is afk
                if str(ping.id) in self.afkdict:
                    await msg.channel.send(f"{ping.mention} is AFK: {self.afkdict[str(ping.id)][0]}; <t:{self.afkdict[str(ping.id)][1]}:R>",delete_after=10)
            if str(msg.author.id) in self.afkdict:#removing an afk
                del self.afkdict[str(msg.author.id)]
                self.afksave()
                await msg.reply("Hey, you. You're finally awake. Anyways, i removed your AFK",delete_after=10)
                
                try:
                    if msg.author.display_name[:5]=="[AFK]" and msg.guild.me.guild_permissions.manage_nicknames:
                        if msg.author.nick[5:]==msg.author.name:
                            await msg.author.edit(nick=None)
                        else:
                            await msg.author.edit(nick=msg.author.nick[5:])
                except Exception as error:
                    pass #add log

    @commands.hybrid_command()
    @commands.bot_has_permissions(send_messages=True)
    async def afk(self,ctx,*, msg='AFK'):
        """Sets Your AFK. These AFKs apply to every Mutual Server.

        Parameters
        ----------
        msg: str
            The reason for your AFK."""
        
        if len(msg)<=256:
            if contains_link(msg):
                await ctx.reply("nah fam, cant let you post links")
            else:
                await ctx.reply(f"I set your AFK: {msg}")
                if str(ctx.author.id) in self.afkdict:
                    self.afkdict[str(ctx.author.id)][0]=msg
                else:
                    self.afkdict[str(ctx.author.id)]=[msg,int(time()),ctx.guild.id,0]
                    
                self.afksave()
                try:
                    if ctx.author.display_name[:5]!="[AFK]" and ctx.guild.me.guild_permissions.manage_nicknames:
                        await ctx.author.edit(nick=f"[AFK]{ctx.author.display_name}")
                except Exception as error:
                    pass #add log
        else:
            await ctx.reply("Sorry, you message exceeds 256 characters. Maybe try to shorten out your feelings.")

    '''@commands.command()
    @commands.has_role(725660115998343178)
    @commands.bot_has_permissions(send_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def hybrid_command(self,ctx,*, user:discord.Member=None):
        'Removes a Person\'s AFK manually.'
        if str(user.id) in self.afkdict:#removing an afk
            del self.afkdict[str(user.id)]
            self.afksave()
            try:
                if user.display_name[:5]=="[AFK]":#removing [AFK] from stuck nicknames if by chance the bot resets
                    if user.display_name[5:]==user.name:
                        await user.edit(nick=None)
                    else:
                        await user.edit(nick=user.display_name[5:])
            except:pass
            await ctx.reply(f"AFK removed from {user.mention} sucessfully")
            
        elif user==None:
            await ctx.reply("Please Specify a User")
        else:
            await ctx.reply("No such User exists in the Database")'''

async def setup(client):
    await client.add_cog(AFK(client))
    print("AFK Cog Loaded")

async def teardown(client):
    print("AFK Cog Unoaded")