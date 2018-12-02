# Python in 100 Pages - v2
# Randall Shane, PhD

import sys


def say_hello():
    name = input('Tell me your name... ')
    print('\n')
    print('Hello %s!' % name)
    print('You are running ', sys.version)
    print('Enjoy!')
    print('\n')



if __name__ == '__main__':
    say_hello()
