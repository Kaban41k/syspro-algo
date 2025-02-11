from mesonbuild.mintro import print_results


def column_division(n, m):
    result = 0
    n = str(n)
    ptr = 1
    x = int(n[0])

    while ptr < len(n):
        if x < m:
            x = x * 10 + int(n[ptr])
            ptr += 1
            result *= 10
        while x >= m:
            result += 1
            x -= m

    return result

assert column_division(19822, 22) == 901, "Wrong answer"
assert column_division(22, 22) == 1, "Wrong answer"
assert column_division(1023000, 1023) == 1000, "Wrong answer"
assert column_division(16, 2) == 8, "Wrong answer"

print("ALL TESTS PASSED :D")
