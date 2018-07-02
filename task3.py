from time import time

def timeit(fn):
    def wrapper(x, y):
        start = time()
        result = fn(x, y)
        elapsed = time() - start
        print(f"Elapsed: {elapsed:.4e}s")

        return result
    return wrapper

@timeit
def add(x, y):
    '''This is a very complicated function :)'''
    return x + y

print(add(3, 5))