import time

def decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function


@decorator_function
def say_hello():
    print("Hello")


def say_bye():
    print("Bye")


res_fun = decorator_function(say_bye)
res_fun()


say_hello()
