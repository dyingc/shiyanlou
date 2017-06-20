#!/usr/bin/env python3

num=(int(input("How many items would you like: ")))

first, second, i = 0, 1, 1

print("The {:d}-item-Fibonacci-List is: ".format(num))

sum = first + second
print("{:d}".format(sum), end=', ')

while i < num:
    sum = first + second
    i += 1
    print("{:d}".format(sum), end=', ')
    first, second = second, sum


