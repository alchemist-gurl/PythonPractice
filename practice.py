#name = input("Give me your name: ")
#print("Your name is " + name)

#age = int(input("How old are you: "))
#print("You are " + str(age) + " years old")

import random
import string

characters = string.ascii_letters, string.digits, string.punctuation
passlen = int(input("how many characters would you like your password?: "))
password =  "".join(random.choices(str(characters), k=passlen))
print("Your password is: " + password)