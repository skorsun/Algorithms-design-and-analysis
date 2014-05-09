__author__ = 'bell'


def get_columns(matrix):
    return [list(i) for i in zip(*matrix)]


def multiply_quadratic_matrices(x, y, n):
    z = []

    for i, row in enumerate(x):
        z.append([])
        for column in get_columns(y):
            v = 0
            for k in range(n):
                v += row[k] * column[k]
            z[i].append(v)
    return z


fst_mtrx = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

snd_mtrx = [[7, 8, 9],
            [4, 5, 6],
            [1, 2, 3]]

result = multiply_quadratic_matrices(fst_mtrx, snd_mtrx, 3)
print result
