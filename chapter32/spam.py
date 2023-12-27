class Spam:
    numInst = 0

    def __init__(self):
        Spam.numInst += 1

    def printNumInst(cls):
        print('Number of instances created: %s' % cls.numInst)

    printNumInst = classmethod(printNumInst)


if __name__ == '__main__':
    a = Spam()
    b = Spam()
    c = Spam()
    d = Spam()
    Spam.printNumInst()
    a.printNumInst()
