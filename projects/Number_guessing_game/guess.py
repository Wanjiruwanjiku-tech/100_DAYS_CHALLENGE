# Build a Number guessing game in which the user selects a range.
# some random number will ne selected by the system
#  and the useer has to guess the integer in the minimum number og guesses.

import random as r
import time

def guess_number():
    print('Hello, Welcome to NTN`s Number Guessing Game')
    time.sleep(2)
    print('Please Input your Name to Move Forwad')
    name = input('Name: ')
    time.sleep(1)
    print('Hi {}, Let us continue...'.format(name))
    print('I am thinking of a Number between 50 and 100. Can you guess it?')
    
    number = r.randint(50, 100)
    guess = None
    count = 0
    number_of_guesses = 5
    while guess != number:
        guess = int(input('Make a Guess: '))
        count += 1
        number_of_guesses -= 1

        if number_of_guesses == 0 and guess != number:
            print('Sorry, You have exhausted your number of guesses. The number was: {}'.format(number))
            break
        elif number_of_guesses == 0 and guess == number:
            print('Congratulations :) {} You have guessed it right!!'.format(name))
            break
        else:
            print('You have {} guesses left'.format(number_of_guesses))

        if guess < number:
            print('Hi {} Your guess is too low, Please Try again'.format(name))
            time.sleep(2)
            

        elif guess > number:
            print('Hi {} Your guess is too high, Please Try again.'.format(name))
            time.sleep(2)

guess_number()