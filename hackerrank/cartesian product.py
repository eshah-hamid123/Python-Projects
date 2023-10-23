from itertools import product

string1 = input()
string2 = input()
splittedString1 = string1.split(' ')
splittedString2 = string2.split(' ')

set1 = []
set2 = []
for num in splittedString1:
    set1.append(int(num))

for num in splittedString2:
    set2.append(int(num))

ans = list(product(set1, set2))
for a in ans:
    print(a, end=' ')





