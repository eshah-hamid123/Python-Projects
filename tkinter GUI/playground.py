def add(*arg):
    sum = 0
    for n in arg:
        sum += n
    return sum


print(add(4, 5, 9, 2))


def calculate(n, **kwargs):
    #for key, value in kwargs.items():
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


print(calculate(2, add=3, multiply=5))
