'''This project aims to create a password generator application using Python,
   allowing users to specify the length and complexity of the password.'''

import random
import string

length = int(input("Write the length of your password:"))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(characters, k=length))

print("Your pasword is:", password)

