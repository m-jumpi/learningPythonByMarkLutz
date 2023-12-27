x = 1


def nester():
    x = 2
    print(x)

    class C:
        x = 3
        print(x)

        def met1(self):
            print(x)
            print(self.x)

        def met2(self):
            x = 4
            print(x)
            self.x = 5
            print(self.x)

    I = C()
    I.met1()
    I.met2()


if __name__ == '__main__':
    print(x)
    nester()
