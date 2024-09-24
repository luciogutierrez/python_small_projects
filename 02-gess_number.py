from random import randint

lower_num, higher_number = 1, 10
random_number : int = randint(lower_num, higher_number)
print(f'Guess the number in the range from {lower_num} to {higher_number}')

while True:
    try: 
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number.')
        continue

    if user_guess > random_number:
        print('The number is lower')
    elif user_guess< random_number:
        print('the number is higher')
    else:
        print('You guessed it')
        break