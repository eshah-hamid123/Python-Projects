def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def calculate (fun , n1,n2):
    return fun(n1,n2)


result = calculate(add, 2, 4)
print(result)


# def outer_function():
#     print("Iam outer")
#
#
#     def inner_function():
#         print("Iam inner")
#
#     inner_function()
#
#
# outer_function()


def outer_function():
    print("Iam outer")


    def inner_function():
        print("Iam inner")

    return inner_function


res = outer_function()
res()

