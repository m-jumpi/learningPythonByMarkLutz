import pprint


def trace(X, label='', end='\n'):
    print(label, pprint.pformat(X), end)


def filterdictvals(D, V):
    """
    dict D with entries for value V removed.
    filterdictvals(dict(a=1, b=2, c=1), 1) => {'b': 2}
    """
    return {k: v2 for (k, v2) in D.items() if v2 != V}


def invertdict(D):
    """
    dict D with values changed to keys (grouped by values).
    Values must all be hashable to work as dict/set keys.
    invertdict(dict(a=1, b=2, c=1)) => {1: ['a', 'c'], 2: ['b']}
    """

    def keysof(V):
        return sorted(K for K in D.keys() if D[K] == V)

    return {V: keysof(V) for V in set(D.values())}


def dflr(cls):
    """
    Classic depth-first left-to-right order of class tree at cls.
    Cycles not possible: Python disallows on __bases__ changes.
    """
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here


def inheritance(instance):
    """
    Inheritance order sequence: new-style (MRO) or classic (DFLR)
    """
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)


def mapattr(instance, withobject=False, bysource=False):
    """
    dict with keys giving all inherited attributes of instance,
    with values giving the object that each is inherited from.
    withobject: False=remove object built-in class attributes.
    bysource:   True=group result by objects instead of attributes.
    Supports classes with slots that preclude __dict__ in instances.
    """
    attr2obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance):
        for obj in inherits:
            if hasattr(obj, '__dict__') and attr in obj.__dict__:
                attr2obj[attr] = obj
                break
    # for k, v in attr2obj.items():
    #     print('(key: %s --> value: %s)' % (k, v))
    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else invertdict(attr2obj)


if __name__ == '__main__':
    print('New-style classes in 2.X, new-style in 3.X')


    class A:    attr1 = 1


    class B(A): attr2 = 2


    class C(A): attr1 = 3


    class D(B, C): pass


    I = D()
    print('Py=>%s' % I.attr1)
    trace(inheritance(I), 'INH\n')
    trace(mapattr(I), 'ATTRS\n')
    trace(mapattr(I, bysource=True), 'OBJS\n')
