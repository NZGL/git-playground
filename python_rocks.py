#!/usr/bin/env python

# a comment
import this


def byitself(number):
    """ A simple function that does very little"""
    return number * number * number


myvar = 10

for num in range(myvar):
    print "The current number is %s" % num
    if num == 9:
        print "The last number is %s, python counts from 0!" % num
    else:
        print "In case you care %s^%s is %s" % (num, num, byitself(num))
