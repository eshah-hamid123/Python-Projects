height = int(input('Enter height: '))
width = int(input('Enter width: '))
print('* ' * width)
for i in range(height - 2):
    print('*' + ' ' * ( 2 * width - 3) + '*')
print('* ' * width)