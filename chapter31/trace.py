class Wrapper:
    def __init__(self, object):
        self.wrapped=object
    def __getattr__(self, item):
        print('Trace: ' + item)
        return getattr(self.wrapped, item)
    def __str__(self):
        return '__srt__ is running'