message = input("Enter your message:")
words = message.split()
emoji = {
    ':)' :'😊',
    ':(' :'😔'
}
output = ''
for i in words:
    output += emoji.get(i , i) + ' '
print(output)