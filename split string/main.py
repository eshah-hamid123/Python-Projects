with open("data.txt", mode = 'r' ) as intro_file:
    content = intro_file.read()

splitted_string = content.split(':')
pin = int(splitted_string[0])
acc_no = int(splitted_string[1])
print(f'Pin is {pin} Account number is {acc_no}')