class PrivateExc(Exception): pass


class Privacy:
    def __setattr__(self, key, value):
        if key in self.privates:
            raise PrivateExc(key, self)
        else:
            self.__dict__[key] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


if __name__ == '__main__':
    x = Test1()
    y = Test2()

    x.name = 'Bob'  # Works
    # y.name = 'Sue'      # Fails
    print(x.name)

    y.age = 30  # Works
    # x.age  = 40         # Fails
    print(y.age)
