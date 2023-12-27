import builtins


def makeopen(id):
    original = builtins.open

    def custom(*pargs, **kwargs):
        print('Custom open call %r' % id, pargs, kwargs)
        return original(*pargs, **kwargs)

    builtins.open = custom


class makeopen:
    def __init__(self, id):
        self.id = id
        self.original = builtins.open
        builtins.open = self

    def __call__(self, *args, **kwargs):
        print('Custom open call %r' % self.id, args, kwargs)
        return self.original(*args, **kwargs)
