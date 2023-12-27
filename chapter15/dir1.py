"""
Module documentation
"""
def dir1(x):
    """
    Dir1 function print attribute list
    :param x:
    :return:
    """
    for i in [a for a in dir(x) if not a.startswith('__')]:
        print(i)