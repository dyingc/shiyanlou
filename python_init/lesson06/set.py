def disp(points):
    print(points)
    print(str(type(points)) + ", size = " + str(len(points)))

points1 = set((x, y, z) for x in range(1, 4) for y in range(1, 4) for z in range(1, 4) if x != y != z)

disp(points1)

points2 = set((x, y, z) for x in range(-1, 4) for y in range(-1, 4) for z in range(-1, 3) if x != y != z)

disp(points2)

points3 = points1 & points2 # intersection

disp(points3)

points4 = points1 | points2 # union

disp(points4)

points5 = points1 - points2 # difference

disp(points5)

points6 = points1 ^ points2 # symmetric difference

disp(points6)

while len(points3) > 0:
    print(points3.pop())

points3.add(points4.pop())

print(points3)