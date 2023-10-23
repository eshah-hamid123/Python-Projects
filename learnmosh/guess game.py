number = 49
while True:
    guess = int(input('Enter the number: '))
    if guess > number:
        print('Enter small number try again')
    elif guess < number:
        print('Enter large number try again')
    elif guess == number:
        print("You guessed it right")
        break