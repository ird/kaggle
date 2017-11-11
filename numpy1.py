import numpy as np


def main():
    # use np.zeros() to create a np array full of zeros
    A = np.zeros(5, "int64")
    print(inspect(A))
    B = np.zeros((4, 5), "complex")
    print(inspect(B))
    # or pass a sequence to np.array()
    C = np.array([1.5, 3, 3, 6])
    D = np.array((1.5, 3, 3, 6))
    print(inspect(C))
    print(inspect(D))
    # reshape does what it sounds like:
    E = np.empty(16).reshape(4, 4)
    print(E)
    print(E.itemsize)
    print(E != 0)
    # dot product defn
    F = np.array([1, 2, 3])
    G = np.array([[1], [2], [3]])
    print(F.dot(G))
    print(my_dot(F, G))


def my_dot(a, b):
    # TODO
    pass


def inspect(n):
    # r = "Contents of <" + hex(id(n)) + "> " + str(n) + " \n"
    # r += "Type of <" + hex(id(n)) + "> " + str(type(n)) + "\n"
    # r += "Data type of <" + hex(id(n)) + "> " + str(n.dtype) + "\n"
    r = ""
    characteristics = {'\nContents of': str(n),
                       'Type of': str(type(n)),
                       'Data type of': str(n.dtype)}
    for item in characteristics:
        r += "{} {}: {}\n".format(item, hex(id(n)), characteristics[item])
    return r


if __name__ == "__main__":
    main()
