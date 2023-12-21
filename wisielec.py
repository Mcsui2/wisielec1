import random
import math
words = ["samolot", "grzebien", "serce", "kran"]

x=random.choice(words)
print(x)
letters_guessed = []
print("guess a letter")
guesses = 6
guessed = False
print()
print('The word contains', len(x), 'leters.')
print(len(x) * '_')
while guessed == False and guesses > 0:
    print('masz ' + str(guesses) + ' prob')
    guess = input('enter a letter or a word')
    if guess in x:
        print('zgadles, graj dalej')
        guesses = guesses
    elif guess not in x:
        print('nie zgadle, graj dalej')
        guesses = guesses -1
        print(len(x) * '_')
    elif guesses == 0:
        print('przegrales')
    elif guess == x:
        print("wygrales")
    
     






                  