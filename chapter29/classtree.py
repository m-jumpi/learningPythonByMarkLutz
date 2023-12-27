def classtree(cls, indent):
    print('.' * indent + cls.__name__)
    for superclass in cls.__bases__:
        classtree(superclass, indent + 3)


def instancetree(inst):
    print('Tree of  %s' % inst)
    classtree(inst.__class__, 3)


def selftest():
    class A: pass

    class B(A): pass

    class C(A): pass

    class D(B, C): pass

    class E: pass

    class F(D, E): pass
    I1=B()
    I2=F()
    instancetree(I1)
    instancetree(I2)


if __name__ == '__main__': selftest()
