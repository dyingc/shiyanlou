#!/usr/bin/env python3

from math import pow

x = float(input("Input the x: "))

def factorial(n):
    result, i = 1, 0
    while i < n:
        result *= i + 1
        i += 1
    return result

result, i= 0, 0

while True:
    term = pow(x, i) / factorial(i)
    result0 = result + term
    i += 1
    term_ratio = term / result0
    if term_ratio < 1 / 1000000000000000 and i > 500:
        break
    result = result0

print("The result of e^{:.2f}, with Times = {:d} is: {:.20f}".format(x, i, result))