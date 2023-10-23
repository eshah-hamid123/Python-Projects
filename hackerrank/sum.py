from itertools import combinations
n = int(input())
error_str = "error--sum too large or small"
outputs = []
for i in range(n):
    x, y = map(int, input().split())
    if y > 0 and y <= 45:
        for comb in combinations(range(1,10), x):
            if sum(comb) == y:
                outputs.append(comb)
    else:
        outputs.append(error_str)

for output in outputs:
    if 'error' in output:
        print(output)
    else:
        print(*output)
