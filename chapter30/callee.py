class Callee:
    def __call__(self, *args, **kwargs):
        print('Called', args, kwargs)

class C:
    def __call__(self, *args, d=6, **kwargs):
        print('Called', args, kwargs, d)

class Callback:
    def __init__(self, color):               # Function + state information
        self.color = color
    def __call__(self):                      # Support calls with no arguments
        print('turn', self.color)

class Callback1:
    def __init__(self, color):               # Class with state information
        self.color = color
    def changeColor(self):                   # A normal named method
        print('turn', self.color)

if __name__ == '__main__':
    c = Callee()
    c(1, 2, 3)
    c1=C()
    c1(1,2, d=7)
