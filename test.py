import numpy

a = [[1, 2, 3, 4],
     [1, 2, 3, 4],
     [6, 7, 3, 4],
     [1, 2, 3, 4]]

a = numpy.array(a)
a[0, 0] += a[1, 2] * a[0, 1]
print(a[:2, :2])
