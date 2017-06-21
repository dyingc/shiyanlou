#!/usr/bin/env python3

col=int(input("How many columns you would like the triangle be: "))
#col = 5
i = col
length = col + 1

while i > 0:
    print(" " * (col - i), end="*" * i + "\n")
    i -= 1
