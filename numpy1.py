import numpy as np


def main():
    # use np.zeros() to create a np array full of zeros
    A = np.zeros(5, "int64")
    print(A)
    print("Type of A: ", type(A))
    print("Data type of A: ", A.dtype)


if __name__ == "__main__":
    main()
