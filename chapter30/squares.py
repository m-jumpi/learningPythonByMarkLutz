class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


if __name__ == '__main__':
    s = Squares(1, 10)
    print(list(s))
    s1 = Squares(10, 20)
    for i in s1:
        print(i, end=' ')
