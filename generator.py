import itertools as it
import random
import pyperclip 


#elements to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

#a more efficient method
characters = {
    "Uppercases": ['ABCDEFGHIJKLMNOPQRSTUVWXYZ'],
    "Lowercases": ['abcdefghijklmnopqyrstuvwxyz'],
    "Numbers": ['0123456789'],
    "Symbols": ['!@#$&*?_-'],
}


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

    #initializing pw
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

    if characters_count < length:
   		random.shuffle(characters)


generate_random_password()

