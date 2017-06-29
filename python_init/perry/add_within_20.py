import random

adding_nums = [(x, y) for x in range(1, 10) for y in range(1, 10) if x + y >= 5 and x + y <= 18]

minus_nums = [(x, y) for x in range(1, 20) for y in range(1, 20) if x - y >= 0]

while True:
    (x, y) = adding_nums[int(random.uniform(0, len(adding_nums)))]
    while True:
        sum = int(input("{:d} + {:d} = ".format(x, y)))
        if sum == x + y:
            break
        else:
            print("No no no! Try again!".format(x, y))
    (x1, y1) = minus_nums[int(random.uniform(0, len(minus_nums)))]
    while True:
        diff = int(input("{:d} - {:d} = ".format(x1, y1)))
        if diff == x1 - y1:
            break
        else:
            print("No no no! Try again!".format(x1, y1))
