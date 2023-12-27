class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)


@tracer
def spam(a, b, c):
    return a + b + c


def tracer1(func):
    def oncall(*args):
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)

    oncall.calls = 0
    return oncall


class C:
    @tracer1
    def spam(self, a, b, c): return a + b + c


def count1(aClass):
    aClass.numInstances = 10
    return aClass


@count1
def spam1(): pass


if __name__ == '__main__':
    # print(spam(1, 2, 3))
    # print(spam('a', 'b', 'c'))
    # print(spam(4, 5, 6))
    # x = C()
    # print(x.spam(1, 2, 3))
    # print(x.spam('a', 'b', 'c'))
    print(spam1.numInstances)
