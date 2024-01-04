# PROYECTO
from random import randint

number = randint(1, 101)
numbers = list(range(1, 101))

userName = input('Username: ')
print(f"Welcome {userName}, do you have 8 guesses to guess the number I'm thinking of?")

guesses = 1

while guesses < 9:
    tried = int(input('Enter a number (between 1 and 100): '))
    if tried in numbers:
        if tried > number:
            print("My number is shorter")
        elif tried < number:
            print("My number is taller")
        elif tried == number:
            print(f"You are a winner! Tried: nro {guesses}")
            break
    else:
        print(f"Enter a valid caracter, tried: nro {guesses}")
    guesses += 1
else:
    print(f"You don't have more intentos. The secret number is: {number} ")
