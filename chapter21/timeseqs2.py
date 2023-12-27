import sys, chapter21.timer

reps = 10000
replist = list(range(reps))


def forLoop():
    res = []
    for x in replist:
        res.append(x + 10)
    return res


def listComp():
    return [x + 10 for x in replist]


def mapCall():
    return list(map(lambda x: x + 10, replist))


def genExpr():
    return list(x + 10 for x in replist)


def genFunc():
    def gen():
        for x in replist:
            yield x + 10

    return list(gen())


print(sys.version)

for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = chapter21.timer.bestoftotal(5, 10000, test)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1]))
