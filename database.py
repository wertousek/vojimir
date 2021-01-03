import botFunctions
import os
from oauth2client.service_account import ServiceAccountCredentials
import gspread

key = os.environ.get("encryptionKey", 0)


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

with open("vojimirCredentials-encrypted.nottxt", "rb") as f:
	with open("vojimir-creds-decrypted.wsecret", "w") as f2:
		try:
			encryptionKey = int(os.environ.get("encryptionKey",0))
			fr = f.read()
			f2.write(botFunctions.decrypt(fr.decode("utf-8"), encryptionKey))
		except Exception as e:
			print(e)

# with open("vojimirCredentials-encrypted.nottxt", "wb") as f:
# 	with open("vojimir_credentials.wsecret", "r") as f2:
# 		#print(f2.read())
# 		fr = f2.read()
# 		encrypted = botFunctions.encrypt(fr,key)
# 		#print(encrypted)
# 		f.write(bytes(botFunctions.encrypt(fr,key),"utf-8"))

try:
	creds = ServiceAccountCredentials.from_json_keyfile_name("vojimir-creds-decrypted.wsecret", scope)
except:
	creds = ServiceAccountCredentials.from_json_keyfile_name("vojimir_credentials.wsecret", scope)

sheetClient = gspread.authorize(creds)

#print(sheetClient.open("TheBotDB").worksheets())

messageLog = sheetClient.open("VojimirLog").worksheet("Message Log")
commandStates = sheetClient.open("VojimirLog").worksheet("Command Channels")

#print(messageLog.append_row(["Ahoj","Jak","se","máš","?"]))
