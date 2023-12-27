def maker(n):
    def action(x):
        return n ** x

    return maker


def f1():
    x = 88
    f2(x)


def f2(x):
    print(x)


f1()


def func():
    x = 99
    return lambda n: x ** n


f = func()
print(f(2))


def f3():
    def f4():
        nonlocal y
        y=10
    f4()
