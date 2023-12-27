def sumtree(l):
    result = 0
    for x in l:
        if not isinstance(x, list):
            result += x
        else:
            result += sumtree(x)
    return result


def sumtree1(l):
    tot = 0
    items = list(l)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot


def sumtree2(l):
    tot = 0
    items = list(l)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front


l = [1, [2, [3, 4], 5], 6, [7, 8]]
sumtree2(l)
