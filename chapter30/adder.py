class Adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


class addrepr(Adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data


class addstr(Adder):
    def __str__(self):
        return '[Value: %s]' % self.data

    def __repr__(self):
        return 'addboth(%s)' % self.data


class Printer:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


if __name__ == '__main__':
    objs = [Printer(2), Printer(3)]
    for obj in objs: print(obj)
    print(objs)
