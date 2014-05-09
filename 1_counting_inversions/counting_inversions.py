__author__ = 'bell'

import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
nums = [int(line.strip()) for line in open(os.path.join(__location__, 'IntegerArray.txt'))]


def sort_and_count(a, n):
    if n == 1:
        return a, 0
    else:
        (b, x) = sort_and_count(a[:n/2], n/2)
        (c, y) = sort_and_count(a[n/2:], n - n/2)
        (d, z) = merge_and_count_split_inv(b, c, n)
        return d, x + y + z


def merge_and_count_split_inv(b, c, n):
    d = []
    i = j = 0
    inv = 0
    for k in range(n):
        if j >= len(c) or (i < len(b) and b[i] < c[j]):
            d.append(b[i])
            i += 1
        else:
            d.append(c[j])
            j += 1
            inv += len(b) - i
    return d, inv

(sorted_array, inversions) = sort_and_count(nums, len(nums))
print inversions  # 2407905288


def brute_force(array):
    inv = 0
    for i in xrange(len(array) - 1):
        for j in xrange(i + 1, len(array)):
            if array[i] > array[j]:
                inv += 1
    return inv
