multiline = ''' 
hey 
today is first day learning python.
it is such a lovely experience.
'''
print(multiline)
print(multiline[6:17])
print('---------------------')
print(multiline[7:])
print('---------------------')
print(multiline[:6])
print('---------------------')
course = 'Python'
another = course[:] #another is copy of course
print(course)
#uppercase letters
print (multiline.upper())
print('---------------------')
print('Letter A is found first at index ')
print (multiline.find('a'))
print('---------------------')
print('Word today is found first at index ')
print (multiline.find('today'))
print('---------------------')
print (multiline.replace('today' , 'tomorrow'))
print ('is' in multiline)