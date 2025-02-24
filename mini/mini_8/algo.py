import numpy as np


def mat_merge(a, b, c, d):
    n = a.shape[0]
    res = np.zeros((n * 2, n * 2))

    res[:n, :n] = a
    res[:n, n:] = b
    res[n:, :n] = c
    res[n:, n:] = d

    return res


def std_mult(x, y):
    n = x.shape[0]
    res = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            for l in range(n):
                res[i, j] += x[i, l] * y[l, j]

    return res


def r8_mult(x, y):
    n = x.shape[0]
    mid = n // 2

    if n < 16:
        return std_mult(x, y)

    a = np.array(x[:mid, :mid])
    b = np.array(x[:mid, mid:])
    c = np.array(x[mid:, :mid])
    d = np.array(x[mid:, mid:])

    e = np.array(y[:mid, :mid])
    f = np.array(y[:mid, mid:])
    g = np.array(y[mid:, :mid])
    h = np.array(y[mid:, mid:])

    n = n // 2

    res = np.zeros((n * 2, n * 2))

    res[:n, :n] = r8_mult(a, e) + r8_mult(b, g)
    res[:n, n:] = r8_mult(a, f) + r8_mult(b, h)
    res[n:, :n] = r8_mult(c, e) + r8_mult(d, g)
    res[n:, n:] = r8_mult(c, f) + r8_mult(d, h)

    return res


def strassen_mult(x, y):
    n = x.shape[0]
    mid = n // 2

    if n == 1:
        return [[x[0][0] * y[0][0]]]

    a = np.array(x[:mid, :mid])
    b = np.array(x[:mid, mid:])
    c = np.array(x[mid:, :mid])
    d = np.array(x[mid:, mid:])

    e = np.array(y[:mid, :mid])
    f = np.array(y[:mid, mid:])
    g = np.array(y[mid:, :mid])
    h = np.array(y[mid:, mid:])

    p1 = r8_mult(a, f - h)
    p2 = r8_mult(a + b, h)
    p3 = r8_mult(c + d, e)
    p4 = r8_mult(d, g - e)
    p5 = r8_mult(a + d, e + h)
    p6 = r8_mult(b - d, g + h)
    p7 = r8_mult(a - c, e + f)

    n = n // 2

    res = np.zeros((n * 2, n * 2))

    res[:n, :n] = p5 + p4 - p2 + p6
    res[:n, n:] = p1 + p2
    res[n:, :n] = p3 + p4
    res[n:, n:] = p1 + p5 - p3 - p7

    return res
