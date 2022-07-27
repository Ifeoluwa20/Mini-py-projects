print('Welcome to quiz game')

play = input('Do you want to play? ')
score = 0

if play.lower() == 'yes':
    print('Nice, lets play')
else:
    quit()

firstquestion = input('What year did Nigeria gain independence? ')

if firstquestion == '1960':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


firstquestion = input('What RAM stand for? ')

if firstquestion.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


firstquestion = input('How many Balon D\'or does Ronaldo have? ')

if firstquestion == '5':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


firstquestion = input('What continent is Nigeria in? ')

if firstquestion.lower() == 'africa':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


firstquestion = input('Who owns twitter? ')
if firstquestion.lower() == 'elon musk':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('You got ' + str((score/5)* 100) + '%')