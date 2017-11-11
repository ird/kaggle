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


def inspect(n):
    # r = "Contents of <" + hex(id(n)) + "> " + str(n) + " \n"
    # r += "Type of <" + hex(id(n)) + "> " + str(type(n)) + "\n"
    # r += "Data type of <" + hex(id(n)) + "> " + str(n.dtype) + "\n"
    r = ""
    characteristics = {'Contents of': str(n),
                       'Type of': str(type(n)),
                       'Data type of': str(n.dtype)}
    for item in characteristics:
        r += "{} {}: {}\n".format(item, hex(id(n)), characteristics[item])
    return r


if __name__ == "__main__":
    main()
