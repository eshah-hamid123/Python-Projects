temp = 'Zero'
while True:
    enter = input('> ').lower()
    if enter == 'help':
        print('Start - to start the car.\n Stop - to stop the car.\nQuit - to quit the game.')
    elif enter == 'start':
        if enter == temp:
            print('Car already started')
        else:
            print('Car started - ready to go.')
    elif enter == 'stop':
        if enter == temp:
            print('Car already stopped')
        else:
            print('Car stopped.')
    elif enter == 'quit':
        break
    else:
        print("i dont understand")
    temp = enter[:]


