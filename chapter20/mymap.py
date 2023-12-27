def customap(func, *seq):
    res = []
    for arg in zip(*seq):
        res.append(func(*arg))
    return res


def mymap(func, *seq):
    return (func(*arg) for arg in zip(*seq))


def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    res = []
    while all(seqs):
        res.append(tuple(s.pop(0) for s in seqs))
    return res


def myzip1(*seqs):
    seqs = [list(s) for s in seqs]
    while all(seqs):
        yield (tuple(s.pop(0) for s in seqs))


def mymapPad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    res = []
    while any(seqs):
        res.append(tuple((s.pop(0) if s else pad) for s in seqs))
    return res


def myzip2(*seqs):
    minlen = min(len(s) for s in seqs)
    return [tuple(s[i] for s in seqs) for i in range(minlen)]


def mymapPad1(*seqs, pad=None):
    maxlen = max(len(s) for s in seqs)
    return [tuple((s[i] if len(s) > i else pad) for s in seqs) for i in range(maxlen)]


def mymapPad2(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]


def myzip3(*seqs):
    iters = list(map(iter, seqs))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)


s1 = 'abc'
s2 = (1, 2, 3)

list(myzip3(s1, s2))
