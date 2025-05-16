from random import randint

ALF = "0123456789"
ALF_N = len(ALF)


def get_digit(x, i):
    if len(x) - i - 1 < 0:
        return ALF[0]
    else:
        return x[len(x) - i - 1]


def counting_digit_sort(arr, dig_i):
    n = len(arr)
    res = [0 for _ in range(n)]
    c = {}

    for i in range(ALF_N):
        c[ALF[i]] = 0

    for i in range(n):
        c[get_digit(arr[i], dig_i)] += 1

    for i in range(1, ALF_N):
        c[ALF[i]] += c[ALF[i - 1]]

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


if ALF == "0123456789":
    # tests
    TESTS_COUNT = 10 ** 3
    for i in range(TESTS_COUNT):
        if i % (TESTS_COUNT // 100) == 0:
            print(f"\rTesting... {i // (TESTS_COUNT // 100)}%", end="", flush=True)

        arr = [randint(0, 10 ** 6) for i in range(10 ** 3)]

        arr_sorted = LSD_radix_sort(list(map(str, arr)))
        arr.sort()
        arr = list(map(str, arr))

        assert arr_sorted == arr, "Wrong answer"

    print("\rALL TESTS PASSED :D")
else:
    n = randint(2, 7)
    l = randint(2, 7)

    # random test
    arr = ["" for i in range(n)]

    for i in range(n):
        for j in range(l):
            arr[i] += ALF[randint(0, ALF_N - 1)]

    print(arr)
    print(LSD_radix_sort(arr))
