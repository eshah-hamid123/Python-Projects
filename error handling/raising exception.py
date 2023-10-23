height = int(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human height should be over 3 minutes.')

bmi = weight / height ** 2
print(bmi)