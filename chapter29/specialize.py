class Super:
    def method(self):
        print('in Super.methond')

    def delegate(self):
        self.action()

    def action(self):
        raise NotImplementedError('action must be specified!')


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('staring in Extender.method')
        Super.method(self)
        print('ending in Extender.method')


class Provider(Super):
    def action(self):
        print('in Provider.action')


class Super1:
    def delegate(self):
        self.action()

    def delegate1(self):
        self.action1()

    def action(self):
        assert False, 'action must be defined!'

    def action1(self):
        raise NotImplementedError('action must be defined!')


class Sub1(Super):
    def action(self):
        print('action in Sub1.action')


from abc import ABCMeta, abstractmethod


class Super2(metaclass=ABCMeta):
    def delegate(self):
        self.method()

    @abstractmethod
    def method(self):
        pass
class Sub2(Super2):
    def method(self):
        print('action in Sub2.method')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider..')
    x = Provider()
    x.action()
    y = Sub2()
    y.delegate()
