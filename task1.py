def hello(fn):
    def wrapper(x, y):
        print("hello world")
        return fn(x, y)
    return wrapper

def add(x, y):
    '''This is a very complicated function :)'''
    return x + y

decorated = hello(add)
print(decorated(3, 5))