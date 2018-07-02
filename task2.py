def hello(fn):
    def wrapper(x, y):
        print("hello world")
        return fn(x, y)
    return wrapper

@hello
def add(x, y):
    '''This is a very complicated function :)'''
    return x + y

print(add(3, 5))