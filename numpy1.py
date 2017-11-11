import numpy as np


def main():
    # use np.zeros() to create a np array full of zeros
    A = np.zeros(5, "int64")
    print(A)
    print(inspect(A))
    B = np.zeros((4, 5), "complex")
    print(B)
    print(inspect(B))


def inspect(n):
    r = "Type of <" + hex(id(n)) + "> " + str(type(n)) + "\n"
    r += "Data type of <" + hex(id(n)) + "> " + str(n.dtype) + "\n"
    return r


if __name__ == "__main__":
    main()
