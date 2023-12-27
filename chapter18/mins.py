def min1(*args):
    res = args[0]
    for arg in args:
        if arg < res:
            res = arg
    return res


def min2(first, *args):
    for arg in args:
        if arg < first:
            first = arg
    return first


def min3(*args):
    res = list(args)
    res.sort()
    return res[0]
