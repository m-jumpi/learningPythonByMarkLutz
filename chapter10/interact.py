#! /usr/local/bin/python3.11
while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    try:
        print(float(reply) ** 2)
    except:
        print('Bad input\n', '#' * 10)
print('Bye')
