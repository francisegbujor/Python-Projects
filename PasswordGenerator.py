import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*().,?0123456789'

number = input('Input amount of passwords to generate: ')
number = int(number)

length = input('Input password length: ')
length = int(length)

print('\nPasswords List: ')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
