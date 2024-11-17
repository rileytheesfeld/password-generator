# Password Generator Project

import random

print('Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+[{]}|\;:",<.>/?1234567890'

number = input('How many passwords would you like to generate?')
number = int(number)

length = input('How long would you like your password(s) to be?')
length = int(length)

print('\nhere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)