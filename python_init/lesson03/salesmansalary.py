#!/usr/bin/env python3

sold_num = int(input("How many cameras are sold: "))
price = float(input("The price of the camera: "))

salary = 1500.00
salary += (sold_num) * 200 + 0.02 * price

print("There were {:d} cameras sold with price: {:.2f}. The salary should be {:.2f}".format(sold_num, price, salary))
