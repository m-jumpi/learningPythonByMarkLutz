def tracer(func, *args, **kargs):
    print('Calling: ', func.__name__)
    return func(*args, **kargs)


def func(*args):
    return sum(args)

def func1(**kargs):
    return kargs


print(tracer(func, *(1, 2, 3, 4, 5)))
print(tracer(func1, a=1, b=1))

