
import itertools as it
import random
import pyperclip 


#characters elements to generate password from
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

while True:
    try:
        n = int(input("\tLength of Password: "))
        break
    except ValueError:
        print(bcolors.FAIL + "Entered Value should be integer only")
        print("Restarting the program...")
        print(bcolors.OKBLUE + "")
        pass


def gen_pass(n):
    print(bcolors.OKGREEN + "Select Character type number from the list: ")

    arr = ["Numbers", "Uppercases", "Lowercases", "Symbols"]
   
    l1 = list(it.combinations(arr, 1))
    l2 = list(it.combinations(arr, 2))
    l3 = list(it.combinations(arr, 3))
    l4 = list(it.combinations(arr, 4))
    l = l1 + l2 + l3 + l4  # list of all the possible combinations of characters

	
    for i in range(len(l)):
        print("\t",i+1, " --- ", l[i])
    print(bcolors.OKBLUE + "")
	
     while True: #catches for loop
        c_type = int(input("Type any serial number from the above list of combinations: "))
        if c_type in range(1, 16):
            break
        else:
            print(bcolors.HEADER + "Serial number should be from 1 to 15...")
            print(bcolors.OKBLUE + "")        
		
    # pw generation 
    s_comb_l = [i for i in list(l[c_type - 1])] # selected character combination list
    print(s_comb_l)
    c_per_pass = n // len(s_comb_l)
    extra_c = n - (c_per_pass * len(s_comb_l))
    password_l = []
    all_char = []


    for i in range(0, len(s_comb_l)):
        x = s_comb_l[i]
        z = characters[x][0]
        l = [char for char in z]
        all_char.extend(l)
        c =  random.choices(l, k = c_per_pass)
        password_l.extend(c)
		
		
	
    #length of password from the user
    length = int(input("Enter password length: "))

ut("Enter password length: "))


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

