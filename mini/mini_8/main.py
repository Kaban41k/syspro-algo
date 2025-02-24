from table import format_table, mat_generator
import numpy as np
import algo
import datetime


benchmarks = []
algos = ["standard", "r8", "strassen"]
results = []

s = 3
for i in range(s, 11):
    print(f"start {str(2**i)}x{str(2**i)}")
    benchmarks.append(f"{str(2**i)}x{str(2**i)}")
    results.append([])

    a = np.random.randint(0, 10**9, size=(2**i, 2**i), dtype='int64')
    b = np.random.randint(0, 10**9, size=(2**i, 2**i), dtype='int64')

    start = datetime.datetime.now()
    algo.std_mult(a, b)
    finish = datetime.datetime.now()
    results[i - s].append(str(finish - start))
    print(f"std Done, ", end="")

    start = datetime.datetime.now()
    algo.r8_mult(a, b)
    finish = datetime.datetime.now()
    results[i - s].append(str(finish - start))
    print(f"r8 Done, ", end="")

    start = datetime.datetime.now()
    algo.strassen_mult(a, b)
    finish = datetime.datetime.now()
    results[i - s].append(str(finish - start))
    print(f"strassen Done")

    start = datetime.datetime.now()
    np.matmul(a, b)
    finish = datetime.datetime.now()
    print(str(finish - start))

    print(f"{str(2**i)}x{str(2**i)} Done")
    print(results[i - s])

format_table(benchmarks, algos, results)
