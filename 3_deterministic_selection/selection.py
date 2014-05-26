__author__ = 'bell'

from random import randint
from math import floor, ceil


def choose_pivot(a, l, r):
    middles = []
    # begin step 1
    for i in range(int(ceil((r - l + 1) / 5.0))):
        lwr = l + i * 5
        uppr = l + (i * 5) + 5
        if uppr > r + 1:
            uppr = r + 1
        lst = a[lwr:uppr]
        lst = sorted(lst)
        # begin step 2
        middles.append(lst[int(floor(len(lst) / 2.0))])
        # end step 2

    # begin step 3
    if len(middles) == 1:
        p = middles[0]
    else:
        p = dselect(middles, 0, len(middles) - 1, (len(middles) - 1) / 2)
    median_idx = a.index(p)
    a[l], a[median_idx] = a[median_idx], a[l]
    # end step 3


def partition(a, l, r):
    """
        as in quicksort and randomized selection
    """
    i = j = l + 1
    pvt = a[l]
    while j <= r:
        if a[j] < pvt:
            if j != i:
                a[j], a[i] = a[i], a[j]
            i += 1
        j += 1
    if l != i - 1:
        a[l], a[i - 1] = a[i - 1], a[l]
    return i - 1


def dselect(a, l, r, i):
    """
        as in randomized selection
    """
    if r - l < 1:
        return a[l]
    choose_pivot(a, l, r)
    border = partition(a, l, r)
    if border == i:
        return a[border]
    elif border > i:
        return dselect(a, l, border - 1, i)
    else:  # border < i
        # the only difference with algorithm from lecture: i is not changed
        # cause border is evaluated globally (from 0 to len(nums) - 1) on
        # every iteration
        return dselect(a, border + 1, r, i)


if __name__ == '__main__':
    import os
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    nums = [int(line.strip()) for line in open(os.path.join(__location__, 'TestData.txt'))]

    from util.timeit import timeit

    @timeit
    def run():
        i = randint(0, len(nums) - 1)
        result = dselect(nums, 0, len(nums) - 1, i)
        assert result == sorted(nums)[i]

    run()
