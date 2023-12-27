class Super:
    def method(self):
        print('in Super.methond')


class Sub(Super):
    def method(self):
        print('starting Sub.method')
        Super.method(self)
        print('ending Sub.method')


if __name__ == '__main__':
    x = Sub()
    x.method()
