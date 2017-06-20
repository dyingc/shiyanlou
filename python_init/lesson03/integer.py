#!/usr/bin/env python3
num=int(input("Please input an integer: "))
mon=num // 30
days=num % 30
print("Month: {}, Day: {}".format(mon, days))
divmod1=divmod(num, 30)
print("Month: {}, Day: {}".format(*divmod(num, 30)))
