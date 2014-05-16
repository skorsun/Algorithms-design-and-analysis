__author__ = 'bell'

comparisons = 9999


def choose_pivot(a, l, r):
    # pass  # nothing to do - first element 162085
    # a[l], a[r] = a[r], a[l]  # last element 164123
    m = ((r - l) / 2) + l  # middle index 138382
    # I got stuck on this line above until understood that
    # (r - l) / 2 is not the same as (r + l) / 2. Oh god..
    if m == r or m == l:  #
        return
    num2idx = {
        a[l]: l,
        a[m]: m,
        a[r]: r
    }
    assert len({a[l], a[m], a[r]}) == 3
    median = sorted([a[l], a[m], a[r]])[1]
    median_index = num2idx[median]
    if median_index != l:
        a[l], a[median_index] = a[median_index], a[l]


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


def quicksort(a, l, r):
    if r - l < 1:
        return
    global comparisons
    choose_pivot(a, l, r)
    border = partition(a, l, r)
    left_comparisons = ((border - 1) - l)
    right_comparisons = r - (border + 1)
    if left_comparisons > 0:
        comparisons += left_comparisons
    if right_comparisons > 0:
        comparisons += right_comparisons
    quicksort(a, l, border - 1)
    quicksort(a, border + 1, r)


if __name__ == '__main__':
    import os
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    nums = [int(line.strip()) for line in open(os.path.join(__location__, 'QuickSort.txt'))]

    from util.timeit import timeit

    @timeit
    def run():
        quicksort(nums, 0, len(nums) - 1)
        assert nums == sorted(nums)
        print comparisons
    run()