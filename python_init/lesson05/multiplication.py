#!/usr/bin/env python3

m, n, i, j = 10, 10, 1, 1

print('#' * (n * 4 + 4))

while i <= m:
    while j <= n:
        print("{:4d}".format(i*j), end='')
        j += 1
    print()
    i += 1
    j = 1

print('#' * (n * 4 + 4))
