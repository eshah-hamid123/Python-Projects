try:
    file = open("file.txt")
    dict = {"name": "Eisha"}
    print(dict['age'])

except FileNotFoundError:
    file = open("file.txt", 'w')

except KeyError as message:
    print(f'The key {message} does not exist.')

else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File is closed")