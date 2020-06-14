import numpy as np
import operator

def concat(x):
    return lambda y: np.hstack((x, y))

def matmul(x):
    return lambda y: np.matmul(x, y)

def _index(i):
    return lambda j: lambda x: x[i, j]

def unsafeCoerce(x):
    return x

def _init(m):
    return lambda n: lambda s: lambda a: print(m, n, s, a) or np.full((m, n), a, dtype=s)

def show_mat(x):
    return str(x)