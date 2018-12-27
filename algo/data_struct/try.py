import random
import math
from linked_list import LinkedListSingly


def hash_function(key):
    num_slot = 529
    A = (math.sqrt(5) - 1) / 2
    b = math.modf(key*A)[0]
    return int(num_slot*b)

res = []
for i in range(400):
    temp = hash_function(i)
    if temp in res:
        print(i, res.index(temp))
    res.append(temp)


