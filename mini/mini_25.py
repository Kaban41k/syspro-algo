import math
from random import randint


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


class HashFunc:
    def __init__(self, n):
        self.n = n
        self.a = [randint(0, n - 1), randint(0, n - 1), randint(0, n - 1), randint(0, n - 1)]

    def h(self, x):
        result = 0
        for i in range(4):
            result += x[i] * self.a[i]

        result %= self.n
        return result


class BloomFilter:
    def __init__(self, n, p):
        bits_n = int(-(n * math.log(p, math.exp(1))) / 0.480) + 1

        while not is_prime(bits_n):
            bits_n += 1

        self.arr = [False for i in range(bits_n)]
        self.hk = int(bits_n / n * 0.693) + 1
        self.hf = []
        for i in range(self.hk):
            self.hf.append(HashFunc(bits_n))

        print(self.hk, bits_n)

    def insert(self, ip):
        for i in range(self.hk):
            self.arr[self.hf[i].h(ip)] = True

    def lookup(self, ip):
        for i in range(self.hk):
            if not self.arr[self.hf[i].h(ip)]:
                return False
        return True


IP_N = 100
ERROR_P = 0.01

b = BloomFilter(IP_N, ERROR_P)

arr = []

for i in range(IP_N):
    ip = (randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))

    b.insert(ip)
    if ip not in arr:
        arr.append(ip)


# --- TEST ---

k = 0
t = 0

for i in range(10 ** 5):
    ip = (randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))

    if (ip in arr) == b.lookup(ip):
        t += 1
    k += 1

print(t / k)
