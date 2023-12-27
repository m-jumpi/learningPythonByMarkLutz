class C1:
    def meth1(self): self.__X = 88  # I assume X is mine

    def meth2(self): print(self.__X)


class C2:
    def metha(self): self.__X = 99  # Me too

    def methb(self): print(self.__X)


class C3(C1, C2):
    pass


class Eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1
        x(42)


class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):
        return arg1 + arg2

    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2
