import time


def timer(func, *args):
    start = time.time()
    for i in range(*args):
        func(*args)
    return time.time() - start