class Spam:
    numInst = 0

    def __init__(self):
        Spam.numInst += 1

    @classmethod
    def printNumInst(cls):
        print('Number of instances created: %s' % cls.numInst, cls, end='\n\n')


class Sub(Spam): pass


# def printNumInst(cls):
#     print('Extra stuff...', cls)
#     Spam.printNumInst()
#
# printNumInst = classmethod(printNumInst)

if __name__ == '__main__':
    x = Sub()
    y = Spam()
    x.printNumInst()
    Sub.printNumInst()
    y.printNumInst()
