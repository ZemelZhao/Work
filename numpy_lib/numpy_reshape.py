import numpy as np
import timeit
a = np.arange(12)
b = a.reshape(3, 4)


t1 = timeit.Timer("import numpy;a = numpy.arange(1000002, dtype=numpy.float64);")
t2 = timeit.Timer("import numpy;a = numpy.arange(1000002, dtype=numpy.float64);b = a.reshape((3, -1))")


print(t2.timeit(2) - t1.timeit(2))
print(b)
