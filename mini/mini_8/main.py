from table import format_table, mat_generator
import numpy as np
import algo
import datetime

benchmarks = []
algos = ["standard", "r8", "strassen"]
results = []

REP_N = 10

START = 4
END = 9

for i in range(START, END):
    print(f"start {str(2 ** i)}x{str(2 ** i)}")
    benchmarks.append(f"{str(2 ** i)}x{str(2 ** i)}")
    results.append([])

    a = np.random.randint(0, 10 ** 9, size=(2 ** i, 2 ** i), dtype='int64')
    b = np.random.randint(0, 10 ** 9, size=(2 ** i, 2 ** i), dtype='int64')

    # ------------------------------------------------------------------------------
    res = []

    for j in range(REP_N):
        start = datetime.datetime.now()
        algo.std_mult(a, b)
        finish = datetime.datetime.now()
        res.append(int(finish.timestamp() * 10000 - start.timestamp() * 10000))

    sr = sum(res) / REP_N // 1 / 10000

    so = 0
    for j in res:
        so += (j - sr * 10000) ** 2
    so = (so / REP_N) ** 0.5
    so = so // 1 / 10000

    sg = 1
    for j in res:
        sg *= j
    sg = sg ** (1 / REP_N)
    sg = sg // 1 / 10000

    results[i - START].append(str(sr) + " " * (8 - len(str(sr))) + str(so) + " " * (8 - len(str(so))) + str(sg))
    print(f"std Done, ", end="")

    # ------------------------------------------------------------------------------
    res = []

    for j in range(REP_N):
        start = datetime.datetime.now()
        algo.r8_mult(a, b)
        finish = datetime.datetime.now()
        res.append(int(finish.timestamp() * 10000 - start.timestamp() * 10000))

    sr = sum(res) / REP_N // 1 / 10000

    so = 0
    for j in res:
        so += (j - sr * 10000) ** 2
    so = (so / REP_N) ** 0.5
    so = so // 1 / 10000

    sg = 1
    for j in res:
        sg *= j
    sg = sg ** (1 / REP_N)
    sg = sg // 1 / 10000

    results[i - START].append(str(sr) + " " * (8 - len(str(sr))) + str(so) + " " * (8 - len(str(so))) + str(sg))
    print(f"r8 Done, ", end="")

    # ------------------------------------------------------------------------------
    res = []

    for j in range(REP_N):
        start = datetime.datetime.now()
        algo.strassen_mult(a, b)
        finish = datetime.datetime.now()
        res.append(int(finish.timestamp() * 10000 - start.timestamp() * 10000))

    sr = sum(res) / REP_N // 1 / 10000

    so = 0
    for j in res:
        so += (j - sr * 10000) ** 2
    so = (so / REP_N) ** 0.5
    so = so // 1 / 10000

    sg = 1
    for j in res:
        sg *= j
    sg = sg ** (1 / REP_N)
    sg = sg // 1 / 10000

    results[i - START].append(str(sr) + " " * (8 - len(str(sr))) + str(so) + " " * (8 - len(str(so))) + str(sg))
    print(f"strassen Done")

    print(f"{str(2 ** i)}x{str(2 ** i)} Done")
    print("results:", results[i - START])
    print("-" * 15)

format_table(benchmarks, algos, results)
