#!/usr/bin/env python3

number = int(input("Please input an integer: "))

threshold=100
if number < threshold:
    print("The input number {:d} is less than {:d}!".format(number, threshold))
elif number <= 2 * threshold:
    print("The input number {:d} is no less than {:d} but no lager than {:d} as well".format(number, threshold, 2 * threshold))
else:
    print("The input number {:d} is lager than {:d}!".format(number, 2 * threshold))