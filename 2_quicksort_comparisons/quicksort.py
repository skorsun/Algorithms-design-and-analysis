__author__ = 'bell'

array = [3, 8, 2, 5, 1, 4, 7, 6]


def partition(a, l, r):
    i = l + 1
    pvt = a[l]
    for j in xrange(l + 1, r + 1):
        if a[j] < pvt:
            if j != i:
                a[j], a[i] = a[i], a[j]
            i += 1
    if l != i - 1:
        a[l], a[i - 1] = a[i - 1], a[l]
    return a, i - 1

print partition(array, 0, 7)  # ([1, 2, 3, 5, 8, 4, 7, 6], 2)