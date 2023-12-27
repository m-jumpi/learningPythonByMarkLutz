class tester:
    def __init__(self, start):
        self.state = start

    def nested(self, label):
        print(label, self.state)
        self.state += 1

class tester1:
    def __init__(self, start):
        self.state=start
    def __call__(self, label):
        print(label, self.state)
        self.state+=1