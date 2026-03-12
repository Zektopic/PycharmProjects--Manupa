#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
	result = []

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result.append(chr((ord(char) + s-65) % 26 + 65))

		# Encrypt lowercase characters
		else:
			result.append(chr((ord(char) + s - 97) % 26 + 97))

	return "".join(result)

#check the above function
if __name__ == "__main__":
	text = input()
	s = 12
	print(encrypt(text,s))
