volume = [(x, y, z) for x in range(1, 5) for y in range(3, 7) for z in range(2, 6) if x != y != z]
print(volume)
print(str(type(volume)) + ": " + str(len(volume)))

for v in volume:
    print(str(type(v)) + ": " + str(len(v)))
    a, b, c = v
    print(a)
    print(b)
    print(c)
    print(type(a))
    print("================")

print(volume[0] in volume)