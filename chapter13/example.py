def match(x):
    if x == 11: return True


found = False
x = list(range(10))
while x and not found:
    if match(x[0]):
        print('11')
        found = True
    else:
        x = x[1:]
if not found:
    print('Not found')

while x:
    if match(x[0]):
        print('11')
        break
    x = x[1:]
else:
    print('Not found')

x = iter(range(1, 10))

while True:
    try:
        z = next(x)
        print(z)
    except:
        x=None
    if not x: break


def f(x,y):
    return x+y