from classtools import AttrDisplay


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # def __repr__(self):
    #     return '[%s:, %s, %s, %s]' % (self.__class__.__name__, self.name, self.job, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    # self-test code
    bob = Person('Bob Gilbert')
    sue = Person('Sue', 'dev', 10000)
    tom = Manager('Tom Jones', pay=10000)

    print('--All Three--')
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)
