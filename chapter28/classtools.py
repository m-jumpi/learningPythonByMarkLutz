class AttrDisplay:
    def _gatherAttr(self):
        attr = []
        for key in sorted(self.__dict__):
            attr.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attr)

    def __repr__(self):
        return '[%s, %s]' % (self.__class__.__name__, self._gatherAttr())


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2


    class SubTest(TopTest):
        pass


    x, y = TopTest(), SubTest()

    print(x)
    print(y)
