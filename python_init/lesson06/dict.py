import string

dict1 = {}

val = 1

for letter in string.ascii_lowercase[:26]:
    dict1[letter] = val
    val += 1

items = dict1.items()

print(str(type(items)))

i = 0

for (x, y) in items:
    i += 1
    print("{}: {:02d}".format(x, y), end="\t")
    if i % 5 == 0:
        print()