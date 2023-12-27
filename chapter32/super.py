class C:
    def act(self):
        print('spam')


class E(C):
    def method(self):
        proxy = super()
        print(proxy)
        proxy.act()


class F:
    def __getitem__(self, ix):
        print('F index')


class D(F):
    def __getitem__(self, ix):
        print('D index')
        F.__getitem__(self, ix)
        super().__getitem__(ix)
        super()[ix]


if __name__ == '__main__':
    X = D()
    X[99]
