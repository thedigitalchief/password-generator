import string
import random


#characters elements to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
	#length of password from the user
	length = int(input("Enter password length: "))

	#asking for user inputs
	alphabets_count = int(input("Enter alphabets count in password: "))
	digits_count = int(input("Enter digits count in password: "))
	special_characters_count = int(
		input("Enter special characters count in password: "))

	characters_count = alphabets_count + digits_count + special_characters_count

	#checking if total length with characters sum count, prints "not valid" if the sum of char > length
	if characters_count > length:
		print("Invalid. Characters total count is greater than the password length.")
		return

	#initializing password
	pw = []

	#picking random alphabet letters
	for i in range(alphabets_count):
		pw.append(random.choice(alphabets))

	#picking random digits
	for i in range(digits_count):
		pw.append(random.choice(digits))

	#picking random special characters
	for i in range(special_characters_count):
		pw.append(random.choice(special_characters))

	#if total character count < password length: add random characters to make it equal to the length
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			pw.append(random.choice(characters))

	#shuffling the resulting generated password
	random.shuffle(pw)

	#converting list to string and printing the list
	print("".join(pw))


generate_random_password()
