name = input('Enter your name: ')
length = len(name)
if length < 3:
    print('Name should be of minimum 3 characters')
elif length > 50:
    print('Name should be of maximum 50 characters')
else:
    print('Name looks good')