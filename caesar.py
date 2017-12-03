# Created by	:	Khachatryan Tigran
# Contact		:	xachatryan@protonmail.com
# Language		:	Python3

# December 03 / 2017
# Thank you for downloading :)

import sys

# Start class Caesar..
class Caesar:
	def libary():
		libarray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
		return libarray

	def newlibary(key):
		key = int(key)
		orglib = Caesar.libary()

		lib = orglib[key:]
		lib += orglib[:key]

		i = 0
		reversecity = {}
		city = {}

		while i < len(orglib):
			city[lib[i]] = orglib[i]
			reversecity[orglib[i]] = lib[i]
			i += 1

		return reversecity,city

	def encrypt(string, key):
		key = int(key)
		string = string.lower()
		lib = Caesar.newlibary(key)[0]
		
		lensymbols = len(string)
		stack = ""
		i = 0

		while i < lensymbols:
			stack += lib.get(string[i], string[i])
			i += 1

		cryptstring = stack
		return cryptstring

	def decrypt(crpstring, key):
		key = int(key)
		crpstring = crpstring.lower()
		lib = Caesar.newlibary(key)[1]
		
		lensymbols = len(crpstring)
		stack = ""
		i = 0

		while i < lensymbols:
			stack += lib.get(crpstring[i], crpstring[i])
			i += 1

		cryptstring = stack
		return cryptstring
# End class.

# Configuration printing..
testingInput = False
if len(sys.argv) == 5:
	if len(sys.argv[2]) > 1:
		if sys.argv[3] == "-k" or sys.argv[3] == "--key":
			if int(sys.argv[4]) > 0 and int(sys.argv[4]) < len(Caesar.libary()):
				if sys.argv[1] == "-e" or sys.argv[1] == "--encrypt":
					testingInput = "enc"
				elif sys.argv[1] == "-d" or sys.argv[1] == "--decrypt":
					testingInput = "dcr"
elif len(sys.argv) == 2:
	if sys.argv[1] == "-h" or sys.argv[1] == "--help":
		testingInput = "hlp"
# End configuration printing.

# Printing result..
if testingInput == "enc":
	result = "[+] Success encryption..\n" + Caesar.encrypt(sys.argv[2], int(sys.argv[4]))
elif testingInput == "dcr":
	result = "[+] Success decryption..\n" + Caesar.decrypt(sys.argv[2], int(sys.argv[4]))
elif testingInput == "hlp":
	result = '''
	[Caesar crypter / decrypter]
	===================================================
	-h or --help		|	For helping

	-e or --encrypt		|	For encryption
	-d or --decrypt		|	For decryption

	-k or --key		|	Input key (only number > 1)

	[Examples]
	===================================================
	caesar.py -e string -k 4		|	Result:	wxvmrk
	caesar.py -d wxvmrk -k 4		|	Result:	string

	caesar.py -e "This is text" -k 4	|	Result:	xlmw mw xibx
	caesar.py -d "xlmw mw xibx" -k 4	|	Result:	this is text


	If you have a questions send me - xachatryan@protonmail.com
	Thank you for downloading :)
	'''
else:
	result = "[-] Syntax error. Please reading manual (-h or --help)."

print(result)
# End printing result.

# Thank you for reading my code :)
