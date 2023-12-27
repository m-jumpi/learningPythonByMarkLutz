class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val

class Commuter5:
    def __init__(self, val):
        self.val=val
    def __add__(self, other):
        print('add ', end='')
        if isinstance(other, Commuter5):
            other=other.val
        return Commuter5(self.val+other)
    def __radd__(self, other):
        print('radd ', end='')
        return Commuter5(other + self.val)
    def __str__(self):
        return '<Commuter5: %s>' % self.val

if __name__ == '__main__':
    x = Commuter5(88)
    y = Commuter5(99)
    print(x + 10)
    print(10 + y)
    z = x + y
    # print(z)
    # print(z + 10)
    print(x+y)
