from random import randint


def karatsuba_multiplication(n, m):
    if m == 0 or n == 0:
        return 0

    n_l = len(str(n))
    m_l = len(str(m))

    if n_l < m_l:
        n_l, m_l = m_l, n_l

    if n_l == m_l == 1:
        return n * m

    mask = 10 ** ((max(n_l, m_l) + 1) // 2)

    a = n // mask
    b = n % mask
    c = m // mask
    d = m % mask

    x1 = karatsuba_multiplication(a, c)
    x2 = karatsuba_multiplication(b, d)
    x3 = karatsuba_multiplication(a + b, c + d)
    x4 = x3 - x2 - x1
    return x1 * 10 ** (n_l + n_l % 2) + x2 + x4 * mask

assert karatsuba_multiplication(1234, 5678) == 7006652, "Wrong answer"
assert karatsuba_multiplication(20, 140) == 2800 == karatsuba_multiplication(20, 140), "Wrong answer"
assert karatsuba_multiplication(2, 100000000) == 200000000, "Wrong answer"
assert karatsuba_multiplication(14000, 18) == 252000, "Wrong answer"
assert karatsuba_multiplication(12345, 54) == 666630, "Wrong answer"

for i in range(1000):
    a = randint(1, 10**12)
    b = randint(1, 10**12)
    assert karatsuba_multiplication(a, b) == a * b, "Wrong answer"

print("ALL TESTS PASSED :D")