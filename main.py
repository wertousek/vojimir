import discord
import botFunctions
from botFunctions import embed, command
from random import choice
import os
import datetime

token = os.environ.get('TOKEN', None)

client = discord.Client()
guild = client.get_guild(710900407639081002)

botFunctions.commandPrefix = "-"

spamValue = 5

last10messages = {}


@client.event # event decorator/wrapper
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
	if message.channel not in last10messages:
		last10messages[message.channel] = []
	if not message.author.bot
		last10messages[message.channel].append({"author": message.author, "time": message.created_at, "content": message.content})
	if len(last10messages[message.channel]) > spamValue:
		del last10messages[message.channel][0]
	a = 0
	for message in last10messages[message.channel]:
		if message["author"] == message.author:
			a += 1
		else:
			break
	if (a >= spamValue and message.created_at - last10messages[message.channel][-2]["time"] < datetime.timedelta(seconds = 60)) or last10messages[message.channel][-2]["content"] == message.content:
		await message.channel.send(f"{message.author.mention} nespamuj!")

	if "kedy" in message.content.lower() and "aktualizacia" in message.content.lower():
		await message.channel.send("Nauč sa písať diakritiku ty bezcitné hovado")

	for i in [["kdy","bude","aktualizace"],["kdy","vyjde","aktualizace"]["kdy","update"],["jak","je","na","tom","aktualizace"]]:
		b = 0
		for j in i:
			if j in message.content.lower():
				b += 1
		if b == len(i):
			await message.channel.send(choice(["Kdo ví","Nikdo neví","Bude až bude","Někdy vyjde, neboj"]))

	for i in [["kedy","vyjde","aktualizácia"],["kedy","bude","aktualizácia"]["kedy","update"],["kedy","updatu"]]:
		b = 0
		for j in i:
			if j in message.content.lower():
				b += 1
		if b == len(i):
			await message.channel.send(choice(["Ani boh nevie","Neboj bude","Zistíš až vyjde"]))
	
	commandos, attributes = command(message.content)

	if "help" == commandos:
		e = embed("Help for Vojimír", fields=[
				{
					"name": "`-help`",
					"value": "napíše tohle",
					"inline": True
				},
				{
					"name": "`-randomKlub`",
					"value": "napíše náhodný klub ze hry [CSM](https://www.csmweb.net/)",
					"inline": True
				},
				{
					"name": "`-trh`",
					"value": "napíše, po kterých kolech se aktualizuje trh",
					"inline": True
				},
				{
					"name": "`-prodej`",
					"value": "napíše, za kolik procent ceny hráč prodávat",
					"inline": True
				},
				{
					"name": "`hostovani`",
					"value": "**Použití**: `-hostovani <cena hráče> <počet kol v sezoně> <počet kol na hostování>` např `-hostovani 300000 30 16`\n Řekne ti za kolik máš hostovat hráče",
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
	if "trh" == commandos:
		await message.channel.send("Domácí trh se aktualizuje po těchto kolech: 3,5,8,10,13,15,18,20,23,25,28,30,33,35,38,40,43,45, s tím, že každé kolo dělitelné pěti se nejspíše aktualizuje i světový trh")
	if "prodej" == commandos:
		await message.channel.send("Hráče se doporučuje prodávat za 80 až 90% jeho ceny")

	if "hostovani" == commandos:
		attributes = [i for i in map(int,attributes.split(" "))]
		await message.channel.send(f"Hráče hostuj za {attributes[0]/3/attributes[1]*attributes[2]} £.")

client.run(token)
