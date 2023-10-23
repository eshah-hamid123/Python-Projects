str_input = input()
splitted_values = str_input.split()
print(splitted_values)
rows = splitted_values[0]
cols = splitted_values[1]

cols = int(input())

loopCount = int(rows / 2)
charStr = '.|.'
dashCount = int((cols - 3) / 2)
j = 1

WCount = int((cols - 7) / 2)

for i in range(loopCount):
    print((dashCount * '-') + (j * charStr) + (dashCount * '-'))
    dashCount -= 3
    j += 2

print((WCount * '-') + 'WELCOME' + (WCount * '-'))


for i in range(loopCount):
    dashCount += 3
    j -= 2
    print((dashCount * '-') + (j * charStr) + (dashCount * '-'))




