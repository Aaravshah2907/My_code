import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "voldemort.py" or file == 'key.key' or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

with open("key.key","rb") as thekey:
	secretkey = thekey.read()

secretphrase = 'password'

user_phrase = input("Enter the secretphase")

if user_phrase == secretphrase:
	for file in files:
		with open(file, 'rb') as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, 'wb') as thefile:
			thefile.write(contents_decrypted)

	print("Files are decrypted Successfully")
else:
	print("Wrong phrase")

