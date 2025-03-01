from random import randint


def get_digit(x, i):
    return x // 10 ** i % 10


def counting_digit_sort(arr, dig_i):
    n = len(arr)
    res = [0 for _ in range(n)]
    c = {}

    for i in range(10):
        c[i] = 0

    for i in range(n):
        c[get_digit(arr[i], dig_i)] += 1

    for i in range(1, 10):
        c[i] += c[i - 1]

    for i in range(n - 1, -1, -1):
        res[c[get_digit(arr[i], dig_i)] - 1] = arr[i]
        c[get_digit(arr[i], dig_i)] -= 1

    return res


def LSD_radix_sort(arr):
    n = len(arr)
    m = 0
    for i in range(n):
        m = max(m, len(str(arr[i])))

    for i in range(m):
        arr = counting_digit_sort(arr, i)

    return arr


# tests
TESTS_COUNT = 10 ** 3
for i in range(TESTS_COUNT):
    if i % (TESTS_COUNT // 100) == 0:
        print(f"\rTesting... {i // (TESTS_COUNT // 100)}%", end="", flush=True)

    arr = [randint(0, 10 ** 6) for i in range(10 ** 3)]

    arr_sorted = LSD_radix_sort(arr)
    arr.sort()

    assert arr_sorted == arr, "Wrong answer"

print("\rDone!")
print("ALL TESTS PASSED :D")
