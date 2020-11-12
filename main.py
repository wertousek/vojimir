import discord
from random import choice
import os
import datetime
import bdbf
import datetime
import database
import json
import asyncio

token = os.environ.get('TOKEN', None)


client = bdbf.Client(commandPrefix = "-", embedFooter = {"text": "Powered by wertousek","icon_url":"https://cdn.discordapp.com/avatars/436131686640648195/d72e4885e1d21bca46bd245bb00c4687.png"})
guild = client.get_guild(710900407639081002)

with open ("sprostySlovnik.json","r") as sprostySlovnik:
	sprostaSlova = json.loads(sprostySlovnik.read())

class GetOutOfLoop(Exception):
	pass

@client.event # event decorator/wrapper
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
	
	try:
		if message.channel.guild.id not in (436132782725660672,):
			if "guild" in dir(message.channel):
				msgLog = [datetime.datetime.utcnow().isoformat(), str(message.author), str(message.author.id),str(message.channel.guild), str(message.channel.guild.id), str(message.channel), str(message.channel.id), message.content, str(message.id)]
			else:
				msgLog = [datetime.datetime.utcnow().isoformat(), str(message.author), str(message.author.id),"", "", str(message.channel), str(message.channel.id), message.content, str(message.id)]

			try:
				database.messageLog.append_row(msgLog)
			except:
				pass
	except:
		pass
	"""await spamProtection(message, choice([f"{message.author.mention} nespamuj!",f"{message.author.mention} Mohli bys psát trochu méně. nikoho to tu nezajímá, jak spamuješ",f"{message.author.mention}už nic nepiš! bolí mě z toho hlava!"]), 5)"""

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

	if type(message.channel) == discord.DMChannel:
		if message.author.id == 436131686640648195:
			try:
				msgTextSplit = message.content.split(" ",1)
				channel = await client.fetch_channel(int(msgTextSplit[0]))
				await channel.send(msgTextSplit[1])
			except Exception as e:
				await message.channel.send(e)
				raise e

	#print(sprostaSlova)
	b = False
	for slovo in message.content.lower().split(" "):
		for sSlovo in sprostaSlova["sprostaSlova"]:
			if sSlovo in slovo:
				try:
					for nSslovo in sprostaSlova["neSprostaSlova"]:
						if nSslovo in slovo:
							b = False
							print(slovo, nSslovo, sSlovo)
							raise GetOutOfLoop
					b = True
				except GetOutOfLoop:
					pass
	if b and "Soukupe mlč" not in message.content:
		await message.channel.send(choice([f"{message.author.mention} Zklidni slovník kamaráde",f"Hej! {message.author.mention} Tohle slovo bys měl co nejdříve odstranit ze svého slovníku!",f"Hej! Hej! Hej! {message.author.mention} Nikdo tady na ty tvoje sprosťárny neni zvědavej!" ]),delete_after=20)

	if message.author.id != 436131686640648195 and message.channel.guild.id == 436132782725660672 and message.content == "!rank":
                await asyncio.sleep(1)
                await message.channel.send("Amatér")
		
@client.command("randomKlub")
async def randomKlub(message):
	"""napíše náhodný klub z aktualizace Jaro20 do hry [CSM](https://www.csmweb.net/)"""
	with open("teams20.txt","r") as teams:
		team = choice(teams.read().split("\n"))
	await message.channel.send(team)
	
@client.command("randomKlub18")
async def randomKlub18(message):
	"""napíše náhodný klub z aktualizace Podzim18 do hry [CSM](https://www.csmweb.net/)"""
	with open("teams.txt","r") as teams:
		team = choice(teams.read().split("\n"))
	await message.channel.send(team)
	
@client.command("randomklub")
async def randomKlub(message):
	with open("teams20.txt","r") as teams:
		team = choice(teams.read().split("\n"))
	await message.channel.send(team)
	
@client.command("randomklub18")
async def randomKlub18(message):
	with open("teams.txt","r") as teams:
		team = choice(teams.read().split("\n"))
	await message.channel.send(team)

@client.command("trh")
async def trh(message):
	"""napíše, po kterých kolech se aktualizuje trh"""
	await message.channel.send("Trh se aktualizuje po odehrání těchto kol:\nDomácí: 3, 8, 13, 18, 23, 28, 33, 38, 43\nSvětový: 5, 10, 15, 20, 25, 30, 35, 40, 45")
	
@client.command("prodej")
async def prodej(message, *attributes):
	"""**Použití**: `-prodej <cena hráče>` napíše, za kolik procent ceny hráč prodávat"""
	if len(attributes) == 0:
		await message.channel.send("Hráče se doporučuje prodávat za 80 až 90% jeho ceny")
	else:
		attributes = attributes[0]
		await message.channel.send(f"Hráče prodej za {int(int(attributes)*0.85)}£, {int(int(attributes)*0.8)}£ až {int(int(attributes)*0.9)}£")
			
@client.command("nejslabsi")
async def nejslabsi(message):
	"""napíše tabulku nejslabších týmů z každé ligy"""
	await message.channel.send("Hledáš nejslabší kluby? tak snad tohle pomůže https://media.discordapp.net/attachments/695395367092486144/721144888862703666/Nejvetsi_lemplove.PNG (tabulku vytvořil FluffyHero)")
							
@client.command("hostovani")
async def hostovani(message, *attributes):
	"""**Použití**: `-hostovani <cena hráče> <počet kol v sezoně> <počet kol na hostování>` např `-hostovani 300000 30 16`\n Napíše, kolik peněz si říct za hostování"""
	try:
		attributes = attributes[0]
		attributes = [i for i in map(int,attributes.split(" "))]
		await message.channel.send(f"Hráče posílej na hostování za {int(attributes[0]/3/attributes[1]*attributes[2])} £.")
	except:
		await message.channel.send("Tento příkaz se používá způsobem `-hostovani <cena hráče> <počet kol v sezoně> <počet kol na hostování>` např `-hostovani 300000 30 16` popřípadě to samé akorát místo hostování napsat host")

@client.command("host")
async def host(message, *attributes):
	try:
		attributes = attributes[0]
		attributes = [i for i in map(int,attributes.split(" "))]
		await message.channel.send(f"Hráče posílej na hostování za {int(attributes[0]/3/attributes[1]*attributes[2])} £.")
	except:
		await message.channel.send("Tento příkaz se používá způsobem `-hostovani <cena hráče> <počet kol v sezoně> <počet kol na hostování>` např `-hostovani 300000 30 16` popřípadě to samé akorát místo hostování napsat host")
client.run(token)
