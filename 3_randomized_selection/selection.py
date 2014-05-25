__author__ = 'bell'

from random import randint


def choose_pivot(a, l, r):
    rand = randint(l, r)
    a[l], a[rand] = a[rand], a[l]


def partition(a, l, r):
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


def rselect(a, l, r, i):
    if r - l < 1:
        return a[l]
    choose_pivot(a, l, r)
    border = partition(a, l, r)
    #print border, a
    if border == i:
        return a[border]
    elif border > i:
        return rselect(a, l, border - 1, i)
    else:  # border < i
        # the only difference with algorithm from lecture: i is not changed
        # cause border is evaluated globally (from 0 to len(nums) - 1) on
        # every iteration
        return rselect(a, border + 1, r, i)


if __name__ == '__main__':
    import os
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    nums = [int(line.strip()) for line in open(os.path.join(__location__, 'TestData.txt'))]

    from util.timeit import timeit

    @timeit
    def run():
        i = randint(0, len(nums) - 1)
        result = rselect(nums, 0, len(nums) - 1, i)
        assert result == sorted(nums)[i]
    run()