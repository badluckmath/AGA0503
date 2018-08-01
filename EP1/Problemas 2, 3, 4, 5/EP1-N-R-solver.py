# Esse programa encontrei na internet #

import math
import numpy as np
import matplotlib.pyplot as plt

def derivative(f, x, h):
      return (f(x+h) - f(x-h)) / (2.0*h)  # might want to return a small non-zero if ==0

def quadratic(x):
    return x**2 - 2    # just a function to show it works

def solve(f, x0, h):
    lastX = x0
    nextX = lastX + 10* h  # "different than lastX so loop starts OK
    i = 0
    while (abs(lastX - nextX) > h):  # this is how you terminate the loop - note use of abs()
        newY = f(nextX)                     # just for debug... see what happens
        print (i, "f(", nextX, ") = ", newY, )     # print out progress... again just debug
        lastX = nextX
        nextX = lastX - newY / derivative(f, lastX, h)  # update estimate using N-R
        i = i + 1
    return nextX

xFound = solve(quadratic, 2, 0.0001)    # call the solver
print ("solution: x = ", xFound)        # print the result
