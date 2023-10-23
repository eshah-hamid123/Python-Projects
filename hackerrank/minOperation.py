def num_operations(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        elif ((n - 1) / 2 % 2) == 0 or (n - 1) / 2 == 1:
            n -= 1
        else:
            n += 1
        count += 1
    return count


n = int(input())
operation_count = []
for i in range(n):
    num = int(input())
    operation_count.append(num_operations(num))

for count in operation_count:
    print(count)





