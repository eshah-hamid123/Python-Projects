output_vals = []
while True:
    user_input = input()
    if len(user_input) == 1:
        break
    n = user_input.split(' ')
    arr = list(map(int, user_input.split(' ')[1:]))

    floor = 0
    time = 0

    for flr in arr:
        diff = abs(floor - flr)
        if flr > floor:
            time += diff * 6
        elif flr < floor:
            time += diff * 4
        time += 5
        floor = flr
    output_vals.append(time)

print(*output_vals, sep='\n')

