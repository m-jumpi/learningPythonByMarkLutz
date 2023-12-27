from chapter20.scramble import scramble, scramble2
def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res


args = 'denis', 'fenis', 'kenins'

intersect(*args)


def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)
    return res


def tracer(func, *items, flag=False):
    print(items)
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if flag: print(items)
        print(func(*items))

def tester(func, items, flag=False):
    for args in scramble(items):
        if flag: print(args)
        print(sorted(func(*args)))