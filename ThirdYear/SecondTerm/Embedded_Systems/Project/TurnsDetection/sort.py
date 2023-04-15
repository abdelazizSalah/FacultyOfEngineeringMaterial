import numpy as np
import functools


def compare(item1, item2):
    if item1[0] < item2[0]:
        return -1
    elif item1[0] > item2[0]:
        return 1
    else:
        if item1[1] < item2[1]:
            return -1
        elif item1[1] > item2[1]:
            return 1
        else:
            return 0


array = np.array([
    [1, 2, 3, 4],
    [2, 2, 3, 4],
    [3, 2, 3, 4],
    [3, 1, 3, 4],
    [3, -1, 3, 4],
])
sortedArr = sorted(array, key=functools.cmp_to_key(compare))
print(sortedArr)
