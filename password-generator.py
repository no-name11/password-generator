import random
import string

print('this is a password genrator')
characters = int(input('enter the no. of characters you want in your password:- '))
password = ''
i = 0
a = string.punctuation
b = string.digits
c = string.ascii_lowercase
d = string.ascii_uppercase
string = str(a) + str(b) + str(c) + str(d)

#creating the four necessary characters
first_4 = random.choice(a) + random.choice(b) + random.choice(c) + random.choice(d)

#creating rest of the password
while i != characters-4:
	character = random.choice(string)
	password = password + str(character)
	i += 1

#comining the complete password
password = password + str(first_4)

#finishing password
password1 = list(password)
random.shuffle(password1)
print('\n your password is:-')
print(''.join(password1))
