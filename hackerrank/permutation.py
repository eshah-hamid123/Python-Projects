def minion_game(string):
    # your code goes here
    #Banana
    vowels = 'aeiouAEIOU'
    vowelCount = 0
    consCount = 0
    for i in range(len(string)):
        if string[i] in vowels:
            vowelCount += (len(string) - i)
        else:
            consCount += (len(string) - i)
    if consCount > vowelCount:
        print(f'Stuart {consCount}')
    else:
        print(f'Kevin {vowelCount}')



if __name__ == '__main__':
    s = input()
    minion_game(s)