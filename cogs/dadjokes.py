from discord.ext import commands
import re
import random
from setup import contains_link

class DadJokes(commands.Cog):
	"""
	From the makers of DadBot (not really), I present to you, DadJokes (wait, why would the makers make a thing they already made? ykw? This was cringe, ngl).
	You might ask, Where are the commands of this category? Well you see, there aren't any. This Cog purely consists of on_message listener.
	Also, How did you even find this Category?
	"""
	def __init__(self, client):
		self.client = client
	
	@commands.Cog.listener()
	async def on_message(self,msg):
		if not msg.author.bot and len(msg.content)!=0 and msg.content[0]!='=' and msg.channel.permissions_for(msg.channel.guild.me).send_messages and not contains_link(msg.content) and True not in [str(msg.content).startswith(p) for p in self.client.command_prefix]:
			dadl = re.match("(.*\s)?(im|i'm|i am)\s(.*)", msg.content, re.IGNORECASE) #type: ignore
			if random.choice((True,True)) and self.client.user != msg.author and dadl and len(dadl.group(3))<20:
				myname=msg.guild.me.nick if msg.guild.me.nick else self.client.user.name
				if dadl.group(3).lower() in ("dad","daddy","father","god"):
					await msg.reply(f"Hi {msg.author.mention}, you are not {dadl.group(3)}")
				elif dadl.group(3).lower() == 'joe':
					await msg.reply(random.choice(seq=("Who's Joe?","Holy s**t guys he's joe biden","Hi Joe",f"Joe mama hahahaha ({random.choice(seq=('I have commited multiple felonies in 1999','I have severe mental health issues','Wake Up, W̴aͥ̓k̖͓͎eͦ ̱̮U̡̜pͬ̌̑, Ẁ͈a̲ͣ͢k̵̛̟͔̋͑ͬ̍͘ͅḙ͂̉ ̛̩͇̗͕͚̫ͤͨ͂̕͢Ù̷̵p̸̞̝̫, W̖̙̱ͭ҉̻̻͐̎͋̑ą̗̱̠̃̍ͭ̈k͇̣̫̓̅͊͊͋ͣͬͨ͟','Please help me'))})")))
				elif dadl.group(3).lower() in (myname.lower(),"betman","betman bot", "betmanbot"):
					await msg.reply(f"No ***in deep voice***, {dadl.group(2)} {dadl.group(3)}")
				else:
					await msg.reply(f"Hi '{dadl.group(3)}', {dadl.group(2)} {myname}")
			elif msg.content=='69':
				await msg.reply(random.choice(('Nice','Reddit-Moment')))
			elif msg.content in (f'<@{self.client.user.id}>', f'<@!{self.client.user.id}>'):
				await msg.reply(f"My prefix is {', '.join(f'`{item}`' for item in self.client.command_prefix)}")
			else:
				pass

async def setup(client):
    await client.add_cog(DadJokes(client))
    print("DadJokes Cog Loaded")

async def teardown(client):
    print("DadJokes Cog Unoaded")