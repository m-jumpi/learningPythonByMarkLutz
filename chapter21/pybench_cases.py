import sys
from .pybench import runner
from chapter19 import sumtree


pythons = [
    (1, '/usr/local/bin/python3.11'),
    (0, '/usr/local/bin/python3.9'),
    (0, '/usr/local/bin/pypy')
]

stmts = [
    (0, 0, "[x ** 2 for x in range(1000)]"),
    (0, 0, "res=[]\nfor x in range(1000): res.append(x ** 2)"),
    (0, 0, "listif3(map(lambda x: x ** 2, range(1000)))"),
    (0, 0, "list(x ** 2 for x in range(1000))"),
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),
    (0, 0, "s = '?'\nfor i in range(10000): s += '?'"),
]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None

x=runner(stmts, pythons, tracecmd)

y=sumtree.sumtree([1, 2, 3])
