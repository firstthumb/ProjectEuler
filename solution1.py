#!/usr/bin/python

"""Multiples of 3 and 5"""
def solution1():
    return sum(x for x in xrange(1, 1000) if x % 3 == 0 or x % 5 == 0)

if __name__ == "__main__":
    print "Solution 1 : ", solution1()