import discord
from random import choice
import os
import datetime
import bdbf
from bdbf import embed, command, spamProtection

token = os.environ.get('TOKEN', None)

client = discord.Client()
guild = client.get_guild(710900407639081002)

bdbf.commandPrefix = "-"
bdbf.embedFooter = {
                "text": "Powered by wertousek",
                "icon_url": "https://cdn.discordapp.com/avatars/436131686640648195/d72e4885e1d21bca46bd245bb00c4687.png"
                }

@client.event # event decorator/wrapper
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
	await spamProtection(message, choice([f"{message.author.mention} nespamuj!",f"{message.author.mention} Mohli bys psát trochu méně. nikoho to tu nezajímá, jak spamuješ",f"{message.author.mention}už nic nepiš! bolí mě z toho hlava!"]), 5)

	"""if "kedy" in message.content.lower() and "aktualizacia" in message.content.lower():
		await message.channel.send("Nauč sa písať diakritiku ty bezcitné hovado")

	for i in [["kdy","bude","aktualizace"],["kdy","vyjde","aktualizace"],["kdy","update"],["jak","je","na","tom","aktualizace"]]:
		b = 0
		for j in i:
			if j in message.content.lower():
				b += 1
		if b == len(i):
			await message.channel.send(choice(["Kdo ví","Nikdo neví","Bude až bude","Někdy vyjde, neboj"]))

	for i in [["kedy","vyjde","aktualizácia"],["kedy","bude","aktualizácia"],["kedy","update"],["kedy","updatu"]]:
		b = 0
		for j in i:
			if j in message.content.lower():
				b += 1
		if b == len(i):
			await message.channel.send(choice(["Ani boh nevie","Neboj bude","Zistíš až vyjde"]))"""
	for i in [["čůrák"],["prdel"],["kurva"],["kunda"]]:
		b = 0
		for j in i:
			if j in message.content.lower():
				b += 1
		if b == len(i):
			await message.channel.send(choice([f"{message.author.mention} Sklidni slovník kamaráde"]))
	
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
					"value": "napíše náhodný klub z aktualizace Jaro20 do hry [CSM](https://www.csmweb.net/)",
					"inline": True
				},
				{
					"name": "`-randomKlub18`",
					"value": "napíše náhodný klub z aktualizace Podzim18 do hry [CSM](https://www.csmweb.net/)",
					"inline": True
				},
				{
					"name": "`-trh`",
					"value": "napíše, po kterých kolech se aktualizuje trh",
					"inline": True
				},
				{
					"name": "`-prodej`",
					"value": "**Použití**: `-prodej <cena hráče>` napíše, za kolik procent ceny hráč prodávat",
					"inline": True
				},
				{
					"name": "`-hostovani` nebo `-host`",
					"value": "**Použití**: `-hostovani <cena hráče> <počet kol v sezoně> <počet kol na hostování>` např `-hostovani 300000 30 16`\n Napíše, kolik peněz si říct za hostování",
					"inline": True 
				},
				{
					"name": "`-nejslabsi`",
					"value": "napíše tabulku nejslabších týmů z každé ligy",
					"inline": True 
				}
				]
			)
		await message.channel.send(embed=e)

	if "randomKlub" == commandos:
		with open("teams20.txt","r") as teams:
			team = choice(teams.read().split("\n"))
			print(team)
			await message.channel.send(team)
	if "randomKlub18" == commandos:
		with open ("teams.txt","r") as teams:
			team = choice(teams.read().split("\n"))
			print(team)
			await message.channel.send(team)
	if "randomklub" == commandos:
		with open("teams20.txt","r") as teams:
			team = choice(teams.read().split("\n"))
			print(team)
			await message.channel.send(team)
	if "randomklub18" == commandos:
		with open ("teams.txt","r") as teams:
			team = choice(teams.read().split("\n"))
			print(team)
			await message.channel.send(team)
	if "trh" == commandos:
		await message.channel.send("Domácí trh se aktualizuje po těchto kolech: 3,5,8,10,13,15,18,20,23,25,28,30,33,35,38,40,43,45, s tím, že každé kolo dělitelné pěti se nejspíše aktualizuje i světový trh")
	if "prodej" == commandos:
		if attributes == None:
			await message.channel.send("Hráče se doporučuje prodávat za 80 až 90% jeho ceny")
		else:
			await message.channel.send(f"Hráče prodej za {int(int(attributes)*0.85)}£, {int(int(attributes)*0.8)}£ až {int(int(attributes)*0.9)}£")
	if "nejslabsi" == commandos:
		await message.channel.send("Hledáš nejslabší kluby? tak snad tohle pomůže https://media.discordapp.net/attachments/695395367092486144/721144888862703666/Nejvetsi_lemplove.PNG")

	if commandos in ("hostovani","host"):
		try:
			attributes = [i for i in map(int,attributes.split(" "))]
			await message.channel.send(f"Hráče posílej na hostování za {int(attributes[0]/3/attributes[1]*attributes[2])} £.")
		except:
			await message.channel.send("Tento příkaz se používá způsobem `-hostovani <cena hráče> <počet kol v sezoně> <počet kol na hostování>` např `-hostovani 300000 30 16` popřípadě to samé akorát místo hostování napsat host")

client.run(token)
