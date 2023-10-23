def validator(s, func):
    ans = False
    for i in range(0, len(s)):
        if s[i].func:
            ans = True
            break
    return ans


# functions = {
#     1: islower
# }
res = validator('qa2', func='qa2'.islower)
print(res)