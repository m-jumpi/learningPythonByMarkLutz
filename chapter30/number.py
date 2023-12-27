class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)


class Indexer:
    def __getitem__(self, index):
        return index ** 2


class Indexer1:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem: ', index)
        return self.data[index]


class Indexer2:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)


class IndexSetter:
    data = [5, 6, 7, 8, 9]

    def __setitem__(self, key, value):
        self.data[key] = value


class C:
    def __index__(self):
        return 255


class StepperIndex:
    def __getitem__(self, item):
        return self.data[item]


if __name__ == '__main__':
    # n1 = Number(10)
    # n2 = n1 - 1
    # print(n2.data)
    #
    # x1 = Indexer()
    # print(x1[2])
    # x2 = Indexer2()
    # print(x2[0], x2[1], x2[-1])
    # # print(x2[1:2], x2[1:], x2[:-1], x2[::2])
    # x2[2]
    # x2[1:2:2]
    # x=C()
    # print(x, hex(x), oct(x))
    d = StepperIndex()
    d.data = 'spam'
    for i in d:
        print(i, end=' ')
