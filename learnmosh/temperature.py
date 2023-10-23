print ('Enter temperature:')
temperature = input('')
temperature = int(temperature)
if temperature >= 30:
    print('It is a hot day')
elif temperature >= 20:
    print('It is a mild day')
else:
    print('It is a cold day')