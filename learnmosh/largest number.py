numbers = [10 , 20 , 15 , 30 , 11]
largest = 0
for i in numbers: #here i is 10 , 20 and so on not 0, 1
    if largest < i:
        largest = i
print(f'Largest number in the list is {largest}.')
