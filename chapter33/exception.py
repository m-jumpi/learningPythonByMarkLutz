def fetcher(obj, index):
    return obj[index]


class AlreadyGotOne(Exception):
    def __str__(self):
        return 'Some sheet happened'


def grail():
    raise AttributeError()


if __name__ == '__main__':
    # x = 'spam'
    # try:
    #     print(fetcher(x, 3))
    # except IndexError:
    #     print('got exception')
    #
    # try:
    #     raise IndexError
    # except IndexError:
    #     print('IndexError was raised')

    # assert False, 'Nobody expects the Spanish Inquisition!'

    try:
        grail()
    except AlreadyGotOne:
        print('AlreadyGotOne raised')
