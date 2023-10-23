size = int(input('Enter size: '))
j = 0
numbers = [ ]
for i in range(size):
    element = int(input())
    numbers.append(element)
print(numbers)
for i in numbers:
    count = numbers.count(i)
    if count > 1:
        numbers.remove(i)
print(numbers)