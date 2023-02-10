import random

BIGGEST = 1000
answer = random.randint(1, 1000)
guess = int(input('Guess a number between 1 - 1000: '))

while guess:
    if guess > answer:
        print('Too high! Try Again ')
    elif guess < answer:
        print('Too low! Try Again ')
    elif guess == answer:
        print('Correct!')
        break
    guess = int(input('Guess Again: '))

