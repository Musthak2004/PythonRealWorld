import random

guess = ''

# First guess
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()  # convert input to lowercase

# Random toss
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == 1:
    toss = 'heads'
else:
    toss = 'tails'

# Check first guess
if guess == toss:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input().lower()  # second guess
    if guess == toss:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
