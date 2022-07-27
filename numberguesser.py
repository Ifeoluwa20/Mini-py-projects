import random

top_of_range = input('Type a number ')

guesses = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Please type a number greater than 0')
else:
    print('Please type a number instead')
    quit()

random_number = random.randint(0, top_of_range)


while True:
    guesses += 1
    user_guess = input('Guess a number ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number instead ')
        continue

    if user_guess == random_number:
        print('You guessed correctly')
        break
    elif user_guess > random_number:
        print('You guessed above the number')
    else:
        print('You guessed below the number')

print("You got it in", guesses, "guesses")

