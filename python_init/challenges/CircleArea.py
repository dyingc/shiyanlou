#!/usr/bin/env python3

from math import pow, pi

def circlArea(radium):
    area = pi * pow(radium, 2)
    return area

r = float(input("Please input the radium of the circl: "))
area = circlArea(r)
print("The area of the circl with radium {:0.2f} is {:.10f}".format(r, area))