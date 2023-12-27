class prop:
    def getage(self):
        return 40

    def setage(self, val):
        print('set age: %s' % val)
        self._age = val

    age = property(getage, setage, None, None)


class operators:
    def __getattr__(self, name):  # On undefined reference
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):  # On all assignments
        print('set: %s %s' % (name, value))
        if name == 'age':
            self.__dict__['age'] = value  # Or object.__setattr__()
        else:
            self.__dict__[name] = value


class AgeDesc:
    def __get__(self, instance, owner):
        return 40

    def __set__(self, instance, value):
        instance._age = value


class desciptors:
    age = AgeDesc()


if __name__ == '__main__':
    # x = prop()
    # print(x.age)
    # x.age = 42
    # print(x.age)
    #
    # y = operators()
    # print(y.age)
    # y.age = 42
    # print(y.age)
    x=desciptors()
    print(x.age)
    x.age=42
    print(x.age)
    print(x._age)
