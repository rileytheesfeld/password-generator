# Password Generator Project

import random

print('Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+[{]}|;:",<.>/?1234567890'

number = input('How many passwords would you like to generate?')
number = int(number)

# Prompt user for password length, enforcing a minimum length of 8 characters
while True:
    length = input('How long would you like your password(s) to be? (Min 8 characters) ')
    length = int(length)
    
    if length < 8:
        print("Password length cannot be less than 8 characters. Please enter a valid length.")
    else:
        break

print('\nhere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
