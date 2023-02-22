## Project On Random Password Generator in Python 

## Imported Library ##

import string
import random

# Typing the password length you want

length = int(input("Enter The password length You Wish For: "))

print('''Choose the character set for password from these :
		1. Digits
		2. Letters
		3. Special characters	
		4. Exit''')

character_List = ""

# Getting the character set for password

### Conditional loop

while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		
		# Adding the letters to possible characters
		character_List += string.ascii_letters
	elif(choice == 2):
		
		# Adding the digits to possible characters
		character_List += string.digits
	elif(choice == 3):
		
		# Adding the special characters to possible
		# characters
		character_List += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(length):

	# Picking a random character from our
	# character list
	randomchar = random.choice(character_List)
	
	# appending a random character to password
	password.append(randomchar)

# printing password as a string
print("The random password is " + "".join(password))

### The Code is ended, Thank You CodeClause ####