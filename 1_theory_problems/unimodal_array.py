__author__ = 'bell'


def max_of_unimodal_array(a):
    """
        You are a given a unimodal array of n distinct elements,
        meaning that its entries are in increasing order up
        until its maximum element, after which its elements are
        in decreasing order.

        Give an algorithm to compute the maximum element that runs
        in O(log n) time.

        :param a: unimodal array
    """
    return 0


def generate_unimodal_array():
    from random import randint

    final_array = []
    total_length = randint(99999, 999999)
    max_number = randint(0, 999999)

    left_array_length = randint(1, total_length - 1)
    right_array_length = (total_length - 1) - left_array_length

    left_part = set()
    for i in xrange(left_array_length):
        left_part.add(randint(-500000, max_number - 1))

    left_array = sorted(list(left_part))
    final_array.extend(left_array)
    final_array.append(max_number)

    right_part = set()
    for i in xrange(right_array_length):
        right_part.add(randint(-500000, max_number - 1))

    right_array = sorted(list(right_part))
    final_array.extend(right_array[::-1])

    assert max_number == max(final_array)

    return max_number, final_array

if __name__ == '__main__':
    maximum, unimodal_array = generate_unimodal_array()
    from util.timeit import timeit

    @timeit
    def run():
        result = max_of_unimodal_array(unimodal_array)

        if maximum == result:
            import os
            __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
            with open(os.path.join(__location__, 'Error.txt'), 'w') as f:
                f.write('max: %i\nlen: %i\n' % (maximum, len(unimodal_array)))
                for item in unimodal_array:
                    f.write("%s\n" % item)

    run()
