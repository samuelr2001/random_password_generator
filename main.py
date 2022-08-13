import random

latters = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789_!@#$%¨&*(){^}'
latters_lower = latters.lower()


while True:
    char_number = int(input('how many characters? '))
    passwords = int(input('how many different passwords? '))

    for x in range(0, passwords):
        passwords_slot = ""
        for x in range(0, char_number):
            characters = random.choice(latters) #picks random characters from latters var.
            passwords_slot = passwords_slot + characters
            #print(characters)
        print(f' the generated password is "{passwords_slot}"')
