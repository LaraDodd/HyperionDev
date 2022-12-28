import random

integers = []

for i in range(10):
    integers.append(random.randint(0,51))

integers.sort()

for i in integers:
    print(i)

