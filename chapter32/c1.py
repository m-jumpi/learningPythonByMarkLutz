class A:
    def __init__(self):
        print('A.__init__')


class B(A):
    def __init__(self):
        print('B.__init__')
        super().__init__()


class C(A):
    def __init__(self):
        print('C.__init__')
        super().__init__()


class D(B, C): pass


if __name__ == '__main__':
    x = B()
    print('\n')
    x = C()
    print('\n')
    x = D()
    print(D.__mro__)
