#!/usr/bin/python

from itertools import takewhile, count

"""The sum of all even valued terms in Fibonacci < 4 million"""
def solution2():
    even_fibonacci = (x for x in fibonacci() if x % 2)
    return sum(takewhile(lambda x: x < 4e6, even_fibonacci))

"""fibonnacci serie"""
def fibonacci():
    x,y = 0,1
    while True:
        yield x
        x,y = y, x+y

if __name__ == "__main__":
    print "Solution 2 : ", solution2()