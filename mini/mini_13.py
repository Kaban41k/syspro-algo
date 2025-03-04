from random import randint


def partition(arr):
    pivot = randint(0, len(arr) - 1)
    size = len(arr)

    i = 1
    j = 1

    arr[0], arr[pivot] = arr[pivot], arr[0]
    pivot = arr[0]

    while j < size:
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

        j += 1

    arr[0], arr[i - 1] = arr[i - 1], arr[0]

    return arr, i - 1


def kth(arr, k):
    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        if k >= 1:
            return max(arr[0], arr[1])
        return min(arr[0], arr[1])

    arr, p = partition(arr)

    if p + 1 == k:
        return arr[p]
    elif p + 1 > k:
        return kth(arr[:p], k)
    else:
        return kth(arr[p:], k - p)


def main_oil_pipeline(oil_coords):
    n = len(oil_coords)
    arr = []
    for i in range(n):
        arr.append(oil_coords[i][1])

    if n % 2:
        return kth(arr, (n + 1) // 2)
    else:
        return (kth(arr, n // 2) + kth(arr, n // 2 + 1)) / 2


assert main_oil_pipeline([[0, 1], [23, 3], [0, 2]]) == 2, "Wrong answer"
assert main_oil_pipeline([[0, 1], [23, 3], [0, 2], [219, 4]]) == 2.5, "Wrong answer"

print("ALL TESTS PASSED :D")