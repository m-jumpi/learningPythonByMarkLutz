def mysum(l):
    if not l:
        return 0
    else:
        return l[0] + mysum(l[1:])


x = mysum([1, 2, 3, 4, 5])
print(x)


def mysum1(l):
    return 0 if not l else l[0] + mysum1(l[1:])


def mysum2(l):
    first, *rest = l
    return first if not rest else first + mysum2(rest)


def mysum3(l):
    if not l: return 0
    return nonempty(l)


def nonempty(l):
    return l[0] + mysum3(l[1:])

