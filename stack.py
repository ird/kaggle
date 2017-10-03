import numpy as np


def main():
    a = np.array([2, 2, 2, 2])
    b = np.array([4, 4, 4, 4])
    c = np.stack((a, b))  # has to be a sequence of arrays!
    d = np.stack((b, a), axis=-1)
    print(c)
    print(d)
    return


if __name__ == '__main__':
    main()
