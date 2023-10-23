str = input()
words = str.split(' ')
max_word = max(words, key=len)
encrypted_words = []
j = 0
for word in words:
    encrypter_word = ''
    for i in range(len(word)):
        asci = (ord(word[i]) + ord(max_word[j]) - 2 * 64) % 26
        j += 1
        if j == len(max_word):
            j = 0
        encrypter_word += chr(asci + 64)
    encrypted_words.append(encrypter_word)

print(' '.join(encrypted_words))