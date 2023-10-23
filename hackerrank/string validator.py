s = input()

ans = False
for i in range(0, len(s)):
    if s[i].isalnum():
        ans = True
        break

print(ans)

ans = False
for i in range(0, len(s)):
    if s[i].isalpha():
        ans = True
        break

print(ans)

ans = False
for i in range(0, len(s)):
    if s[i].isdigit():
        ans = True
        break

print(ans)

ans = False
for i in range(0, len(s)):
    if s[i].islower():
        ans = True
        break

print(ans)

ans = False
for i in range(0, len(s)):
    if s[i].isupper():
        ans = True
        break

print(ans)