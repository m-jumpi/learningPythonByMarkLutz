class Accesscontrol:
    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__[key] = value + 10
        else:
            raise AttributeError(key + ' not allowed')


if __name__ == '__main__':
    x = Accesscontrol()
    x.age = 1
    print(x.age)
    # x.name = 'name'
