number = int(input('Enter number: '))

# initialize variables
number_copy = number
sumDigit = 0
length = 0
rightLen = 0
leftLen = 0
sumPerfect = 0
# compute sum of digits


while number_copy != 0:
    length += 1
    sumDigit += (number_copy % 10)
    number_copy = int(number_copy /10)

number_copy = number
# compute sumdigit - 1
sumDec = sumDigit - 1
# print(sumDec)
# check prime number
isNPRime = True
for i in range(2, sumDec):
    if sumDec % i == 0:
        isNPRime = False
        break


if not isNPRime:
    print('Serious')

else:
    if length == 1:
        print('Serious')
    else:
        halfLength = int(length/ 2)
        for i in range(halfLength):
            rightLen += number_copy % 10
            number_copy = int(number_copy / 10)

        if sumDigit % 2 != 0:
            number_copy = int(number_copy / 10)

        for i in range(halfLength):
            leftLen += number_copy % 10
            number_copy = int(number_copy / 10)

        diff = rightLen - leftLen
        diff = abs(diff)

        # check perfect
        for i in range(1, int(diff / 2) + 1):
            if diff % i == 0:
                sumPerfect += i

        if diff == sumPerfect:
            print('Funny')
        else:
            print('Serious')







