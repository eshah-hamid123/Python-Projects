N = int(input())
command_list = []
no_list = [3, 2]
for _ in range(N):
    command = input().split()
    command_list.append(command)

for command in command_list:
    if command[0] == 'print':
        print(no_list)
    elif command[0] == 'sort':
        no_list.sort()
    elif command[0] == 'reverse':
        no_list.reverse()
    elif command[0] == 'pop':
        no_list.pop(-1)
    elif command[0] == 'insert':
        index = int(command[1])
        e = int(command[2])
        no_list.insert(index, e)
    elif command[0] == 'remove':
        e = int(command[1])
        no_list.remove(e)
    elif command[0] == 'append':
        e = int(command[1])
        no_list.append(e)




