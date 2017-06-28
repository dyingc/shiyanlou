print(divmod(100, 7))

volume = [(x, y, z) for x in range(1, 4) for y in range(1, 4) for z in range(1, 4) if x != y != z]

print(volume)

print(str(type(volume)) + ", size = " + str(len(volume)))

