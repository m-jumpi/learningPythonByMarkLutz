import sys, chapter21.timer2

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
    ((total, result)) = chapter21.timer2.bestoftotal(test, _reps1=5, _reps=1000)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, total, result[0], result[-1]))