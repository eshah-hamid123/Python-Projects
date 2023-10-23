from collections import Counter

# user input
noOfShoes = int(input())
shoeSizeInput = input()
noOfCustomers = int(input())
shoeSize = []
price = []
for i in range(noOfCustomers):
    temp = input()
    shoeSize.append(int(temp.split(' ')[0]))
    price.append(int(temp.split(' ')[1]))

# counting shoes of specific size
shoeSizeList = list(map(int, shoeSizeInput.split(' ')))
counterDict = dict(Counter(shoeSizeList))

money = 0
for i in range(noOfCustomers):
    if shoeSize[i] in counterDict and counterDict[shoeSize[i]] > 0:
        money += price[i]
        counterDict[shoeSize[i]] -= 1

print(money)



