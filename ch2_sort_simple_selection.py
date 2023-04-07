import numpy as np


""" selection sort with O(N^2) """

def selection_sort(x):

    for i in range(len(x)):

        swap = i + np.argmin(x[i:])

        (x[i], x[swap]) = (x[swap], x[i])

    return x

if __name__ == "__main__":
    x = np.array(np.random.randint(0, 45, size=6))
    print(f"{x}")
    sort_arr = selection_sort(x)
    print(f"{sort_arr}")