#!/usr/bin/env python

import random

MAX = int(input("The max number of sticks that can be taken per round: "))

total = int(input("How many sticks would you want this game starts with: "))

valid_choice = range(1, MAX + 1)

def validate(n):
    if n in valid_choice:
        return True
    else:
        print("Incorrect choose! Valid number should be: {}".format((valid_choice)))
        return False

def cal_AI_taken(human_taken):
    return MAX + 1 - human_taken

# Main
remaining = total

while remaining > 0:
    human_takes = int(input("How many sticks would you take: "))
    while validate(human_takes) == False:
        human_takes = int(input("How many sticks would you take: "))
    remaining -= human_takes
    if remaining == 1:
        print("Human WIN!!!")
        exit(0)
    AI_taken = cal_AI_taken(human_takes)
    remaining -= AI_taken
    print("AI took {:d} after you took {:d} and there're {:d} sticks remaining".format(AI_taken, human_takes, remaining))
    if remaining == 1:
        print("AI WIN!!!")
        exit(0)

