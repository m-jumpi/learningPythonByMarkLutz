from listinstance import ListInstance
from listinherited import ListInherited


class Super:
    def __init__(self):
        self.data1 = 'spam'

    def ham(self):
        pass


class Sub(Super, ListInherited):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):
        pass


if __name__ == '__main__':
    X = Sub()
    print(X)
