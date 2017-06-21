#!/usr/bin/env python3

while True:
    num = int(input("Please input a positive integer: "))
    if num == 0:
        print("Thank you for your use! Exit.")
        exit(0)
    elif num < 0:
        continue
    else:
        result = pow(num, 2)
        print("Squre of positive integer: {:d} = {:d}.".format(num, result))