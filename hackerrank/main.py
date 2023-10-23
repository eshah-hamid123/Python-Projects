n = int(input())
arr = map(int, input().split())

max = 0
runner_up = 0

for element in list(arr):
    # print(f'{element} {max}')
    if element > max:
        runner_up = max
        max = element
    if element == max:
        pass
    elif element > runner_up:
        runner_up = element
print(runner_up)
