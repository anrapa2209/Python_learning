i = 1
while i <= 5:
    print(i)
    i = i + 1
    # this increment is necessary otherwise i will be 1 forever resulting in an infinite while loop
print('Done')
print('')

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print('Done')

# Guessing game, secret number
secret_num = 9
guess_count = 0                           # assume this is the number of guesses made by user
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_num:
        print('You won!')
        break
else:
    print('Sorry, you failed')