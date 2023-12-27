class C(object):
    data='spam'
    def __getattr__(self, name):
        print('getattr: ', name)
        return getattr(self.data, name)
    def __getitem__(self, item):
        print('getitem: ', str(item))
        return self.data[item]
    def __add__(self, other):
        print('add: ', other)
        return getattr(self.data, '__add__')(other)