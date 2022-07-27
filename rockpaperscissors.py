import random

user_wins = 0
computer_wins = 0
draw = 0

option = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Enter Rock, Paper or Scissors. Enter 'Q' to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in option:
        print('Enter either Rock, Paper or Scissors')
        continue
    

    rand_num = random.randint(0, 2)
    comp_choice = option[rand_num]

    print('Computer picked ' + comp_choice + '.')

    if user_input == 'rock' and comp_choice == 'scissors':
        print('You won!')
        user_wins += 1
    
    elif user_input == 'paper' and comp_choice == 'rock':
        print('You won!')
        user_wins += 1

    elif user_input == 'scissors' and comp_choice == 'paper':
        print('You won!')
        user_wins += 1

    elif user_input == 'rock' and comp_choice == 'rock':
        print('Draw')
        draw += 1

    elif user_input == 'paper' and comp_choice == 'paper':
        print('Draw')
        draw +=1
    
    elif user_input == 'scissors' and comp_choice == 'scissors':
        print('Draw')
        draw +=1
    
    
    else:
        print('You lost.')
        computer_wins += 1

print('You won', user_wins, 'times')
print('Computer won', computer_wins, 'times')
print('There was', draw, 'draws')

if user_wins > computer_wins:
    print("\nYou Won")
elif computer_wins > user_wins:
    print('\nComputer Won')
else:
    print('\nNo winner')

print('\nGoodbye!!!')

