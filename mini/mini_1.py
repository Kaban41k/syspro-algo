def column_division(n, m):
    result = 0
    ptr = len(str(n)) - len(str(m))

    while ptr >= 0:
        if n // 10 ** ptr < m:
            ptr -= 1
            continue

        result += 10 ** ptr
        n -= m * 10 ** ptr

    return result


assert column_division(19822, 22) == 901, "Wrong answer"
assert column_division(22, 22) == 1, "Wrong answer"
assert column_division(1023000, 1023) == 1000, "Wrong answer"
assert column_division(16, 2) == 8, "Wrong answer"

print("ALL TESTS PASSED :D")
