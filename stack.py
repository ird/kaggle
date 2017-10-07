import numpy as np
from timeit import Timer


def pure_python():
    X = range(1000)
    Y = range(1000)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    return len(Z)


def np_version():
    X = np.arange(1000)
    Y = np.arange(1000)
    Z = X + Y
    return len(Z)


def benchmark(fname1, fname2):
    timer1 = Timer(fname1 + "()", "from __main__ import " + fname1)
    timer2 = Timer(fname2 + "()", "from __main__ import " + fname2)
    return timer1.timeit(1) / timer2.timeit(1)


def reverse_rows(m):
    M = m.copy()
    y, _ = np.shape(M)
    for i in range(y):
        M[i] = M[i][::-1]
    return M


def reverse_cols(m):
    M = m.copy()
    _, x = np.shape(M)
    for i in range(x):
        M[:, i] = M[:, i][::-1]
    return M


def main():
    a = np.array([2, 2, 2, 2])
    b = np.array([4, 4, 4, 4])
    c = np.stack((a, b))  # has to be a sequence of arrays!
    d = np.stack((b, a), axis=-1)
    print(c)
    print(d)
    # np arrays vs python arrays
    print(benchmark("pure_python", "np_version"))
    # exercise 5&6 - numpy (python-course.eu)
    # reverse the rows and cols of a multidimensional array
    m = np.arange(28).reshape(4, 7)
    print(m)
    print(reverse_rows(m))
    print(reverse_cols(m))
    return


if __name__ == '__main__':
    main()
