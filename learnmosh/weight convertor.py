weight = input('Enter your weight: ')
unit = input('(L)bs or K(g): ')
if unit.upper() == 'L':
    weight = float(weight) / 2.2
    print(f'Weight is {int(weight)} kilos.')
else:
    weight = float(weight) * 2.2
    print(f'Weight is {int(weight)} pounds.')