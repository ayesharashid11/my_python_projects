from email import generator
import random 
print ('Hello! welcome to password generator')
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghikjlmnoqrpstuvwxzy0987654321,./@#$%^&*?><'
number = input('entre number of passwords to generate: ')
number = int(number)
length= input('entre lenght of your passwords to generate: ')
length = int(length)
print ('/nHERE are your passwords/n')

for pws in range (number):
    passwords = ''
    for c in range (length):
        passwords += random.choice(chars)
    print(passwords)    