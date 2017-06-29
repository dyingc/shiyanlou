#!/usr/bin/env python3

a = [23, 45, 1, -3434, 43624356, 234, 1]
print(a)
a.remove(1)
print(a)
a.insert(2, 1)
print(a)
print(a.reverse())
print(a)
a.sort()
print(a)
del a[-1]
print(a)
a.append(3)
print(a)
a.extend([5, 7])
print(a)

i, b = 0, []


while i < len(a):
    b.append(a[i])
    i += 1

while len(a) > 0:
    print(a.pop())

print()

while len(b) > 0:
    inx = 5
    if inx > len(b) - 1:
        inx = len(b) - 1
    print(b.pop(inx))