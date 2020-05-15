import discord
import botFunctions
from botFunctions import embed, command
from random import choice

token = "NzEwOTAwNDA3NjM5MDgxMDAy.Xr7X-g.FGREwoYd_W8wf_ZPno74xqmSjFA" #os.environ.get('TOKEN', None)

client = discord.Client()
guild = client.get_guild(710900407639081002)

botFunctions.commandPrefix = "-"

spamValue = 5

last10messagesAuthors = {}


@client.event # event decorator/wrapper
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
	if message.channel not in last10messagesAuthors:
		last10messagesAuthors[message.channel] = []
	last10messagesAuthors[message.channel].append(message.author)
	if len(last10messagesAuthors[message.channel]) > spamValue:
		del last10messagesAuthors[message.channel][0]
	a = 0
	for author in last10messagesAuthors[message.channel]:
		if author == message.author:
			a += 1
		else:
			break
	if a >= spamValue and message.author.name != "Vojimír":
		await message.channel.send(f"{message.author.mention} nespamuj!")

	if "kdy" in message.content.lower() and "aktualizace" in message.content.lower():
		await message.channel.send("Kdo ví")
	
	commandos, attributes = command(message.content)

	if "help" == commandos:
		e = embed("Help for Vojimír", fields=[
				{
					"name": "`~help`",
					"value": "returns this",
					"inline": True
				},
				{
					"name": "`~randomKlub`",
					"value": "returns a random team from [CSM](https://www.csmweb.net/)",
					"inline": True
				}
				]
			)
		await message.channel.send(embed=e)

	if "randomKlub" == commandos:
		with open("teams.txt","r") as teams:
			team = choice(teams.read().split("\n"))
			print(team)
			await message.channel.send(team)

client.run(token)