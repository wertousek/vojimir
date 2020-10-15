import zlib
import smaz

def encrypt(text_to_encrypt, encryption_base):
	digits = []
	for i in range(48,48 + encryption_base):
		try:
			digits.append(bytes(chr(i),"utf-8").decode("utf-8"))
		except UnicodeEncodeError:
			pass
	text = smaz.compress(str(text_to_encrypt))
	if text == b"":
		text = zlib.compress(bytes(text_to_encrypt, encoding="utf-8"))
	textInts = [i for i in text]
	textNum = ""
	result = -1
	remainder = -1
	cipher = """"""
	for i in textInts:
		m = str(i)
		for _ in range(3-len(m)):
			m = f"0{m}"
		textNum = f"{textNum}{m}"

	try:
		result = int(textNum)
	except:
		result = 0
	while result != 0:
		remainder = result % len(digits)
		result = result // len(digits)
		cipher = f"{digits[remainder]}{cipher}"
	return cipher


def decrypt(text_to_decrypt, encryption_base):
	digits = []
	for i in range(48,48 + encryption_base):
		digits.append(bytes(chr(i),"utf-8").decode("utf-8"))
	cipher = text_to_decrypt
	num = 0
	power = len(cipher)-1
	text = ""
	for c in cipher:#[2:-1]:
		num += (digits.index(c) * (len(digits) ** power))
		power -= 1
	for i in range(3-(len(str(num))%3) if len(str(num))%3 != 0 else 0):
		num = f"0{num}"
	num = str(num)
	n = 3
	nums = [int(num[i:i+n]) for i in range(0, len(num), n)]
	try:
		texto = smaz.decompress(bytes(nums))
	except:
		texto = zlib.decompress(bytes(nums)).decode("utf-8")
	return texto