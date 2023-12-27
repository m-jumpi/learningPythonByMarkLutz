var = 99


def local():
    var = 0


def glob1():
    global var
    var += 1


def glob2():
    var = 0
    import chapter17.thismod
    chapter17.thismod.var += 1


def glob3():
    var = 0
    import sys
    glob = sys.modules['chapter17.thismod']
    glob.var += 1

def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)