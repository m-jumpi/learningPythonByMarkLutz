import sys, time

timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(reps, func, *args, **kargs):
    """
    Total time to run func() reps time
    :return: (total time, last result)
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*args, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(reps, func, *args, **kargs):
    """
    Quickest func() among reps run
    :return: (best run, last result)
    """
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*args, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(reps1, reps2, func, *args, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 of func))
    """
    return bestof(reps1, total, reps2, func, *args, **kargs)