from random import randint
import time


class Task:
    def __init__(self, deadline, fine):
        self.deadline = deadline
        self.fine = fine


class UnionFind:
    def __init__(self, n):
        self.arr = list(range(n))
        self.ranks = [0 for i in range(n)]

    def find(self, x):
        x -= 1
        a = []

        while self.arr[x] != x:
            a.append(x)
            x = self.arr[x]

        for i in a:
            self.arr[i] = x
        
        return x

    def union(self, g1, g2):
        if self.ranks[g1] > self.ranks[g2]:
            self.arr[g2] = g1
        else:
            self.arr[g1] = g2

        if self.ranks[g1] == self.ranks[g2]:
            self.ranks[g2] += 1


def simple_solution(taskSortedArr):
    n = len(taskSortedArr)
    result = [None for i in range(n)]
    ptr_last = n - 1
    f = 0

    for i in range(n):
        dl = taskSortedArr[i].deadline - 1
        if result[dl] is None:
            result[dl] = taskSortedArr[i]
        else:
            while dl != -1:
                if result[dl] is None:
                    result[dl] = taskSortedArr[i]
                    break
                dl -= 1

            if dl == -1:
                f += taskSortedArr[i].fine
                while result[ptr_last] is not None:
                    ptr_last -= 1
                result[ptr_last] = taskSortedArr[i]

    return result, f


def uf_solution(taskSortedArr):
    n = len(taskSortedArr)
    uf = UnionFind(n)
    d = {}
    num_d = {}
    result = [None for i in range(n)]
    ptr_last = n - 1
    f = 0

    for i in range(n):
        num_d[taskSortedArr[i]] = i
        d[uf.find(i)] = -1

    for i in range(n):
        dl = taskSortedArr[i].deadline - 1

        if result[dl] is None:
            result[dl] = taskSortedArr[i]
            d[uf.find(i)] = dl - 1

        else:
            if d[uf.find(num_d[result[dl]])] == -1:
                f += taskSortedArr[i].fine
                if result[ptr_last] is not None:
                    ptr_last = d[uf.find(num_d[result[ptr_last]])]

                result[ptr_last] = taskSortedArr[i]
                dl = ptr_last

                if result[ptr_last - 1] is not None:
                    ptr_last = d[uf.find(num_d[result[ptr_last - 1]])]
                else:
                    ptr_last -= 1
            else:
                dl = d[uf.find(num_d[result[dl]])]
                result[dl] = taskSortedArr[i]

        if dl + 1 != n and result[dl + 1] is not None:
            uf.union(uf.find(i), uf.find(num_d[result[dl + 1]]))
            d[uf.find(i)] = dl - 1

        if dl - 1 != -1 and result[dl - 1] is not None:
            m = d[uf.find(num_d[result[dl - 1]])]
            uf.union(uf.find(i), uf.find(num_d[result[dl - 1]]))
            d[uf.find(i)] = m

    return result, f


# TEST FROM PRESENTATION
arr = [Task(1, 6), Task(4, 5), Task(2, 4), Task(4, 3), Task(1, 2)]

arr1, f = uf_solution(arr)
for i in range(len(arr1)):
    print(arr1[i].fine, end=" ")
print("  ", f)

arr2, f = simple_solution(arr)
for i in range(len(arr2)):
    print(arr2[i].fine, end=" ")
print("  ", f, "\n")

# BIG TEST WITH RANDOM
print("---test-on-big-data---")
fines = []
tasks = []

N = 10 ** 5

for i in range(N):
    fines.append(randint(1, 1000))

fines.sort(reverse=True)

for i in range(N):
    tasks.append(Task(randint(2, N - 1), fines[i]))

tasks2 = tasks.copy()

start = time.time()
arr1, f1 = simple_solution(tasks)
finish = time.time()

print("Simple solution time:", finish - start)

start = time.time()
arr2, f2 = uf_solution(tasks)
finish = time.time()

print("Cool solution time:", finish - start)

assert f1 == f2, "Oh..."

print("\nALL TESTS PASSED :D")
