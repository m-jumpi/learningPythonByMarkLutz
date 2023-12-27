import time, sys

timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(func, *args, **kargs):
    _reps = kargs.pop('_reps', 1000)
    replist = list(range(_reps))
    start = timer()
    for i in replist:
        ret = func(*args, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(func, *args, **kargs):
    _reps = kargs.pop('_reps', 5)
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*args, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)


def bestoftotal(func, *args, **kargs):
    _reps1 = kargs.pop('_reps1', 5)
    return min(total(func, *args, **kargs) for i in range(_reps1))
