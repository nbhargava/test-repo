#!/usr/bin/env python
'''
This example demonstrates a simple use of pycallgraph.
'''
from banana import Banana
from person import Person


def main():
    person = Person()
    for a in xrange(10):
        person.add_banana(Banana())
    person.eat_bananas()

def b():
    print('yo')

def a():
    b()

if __name__ == '__main__':
    main()
    a()
