from typing import List


def subset_sum_k(arr, k):
    """
    :param arr: An array of non-negative integer
    :param k: The sum to look for
    :return: True if there is a subset in arr of sum k
    """

    class Matrix:

        matrix: List[List[int]]

        def __init__(self, r, c):
            self.matrix = [[-1 for _ in range(c + 1)] for _ in range(r)]

            for i in range(r):
                self.matrix[i][0] = 1

        def set(self, r, c, value):
            """
            :param r: Row number based on the index 0 system
            :param c: Column number based on the index 0 system
            :param value: Value to set at stated point
            :return: None
            """
            self.matrix[r][c] = value

        def get(self, r, c):
            """
            :param r: Row number based on the index 0 system
            :param c: Column number based on the index 0 system
            :return: Value at position described by r and c
            """

            if r < 0 or c < 0:
                return False

            return self.matrix[r][c]

        def __str__(self):
            return "\n".join(list(map(str, self.matrix)))

    # map indices i -> len(arr) - 1 to each of the elements in k
    index_val_map = {index: value for index, value in zip(range(len(arr)), arr)}

    # initialize a new matrix
    matrix = Matrix(len(arr), k)

    for r in range(len(arr)):
        for c in range(1, k + 1):

            if c == index_val_map[r]:
                value = 1
            else:
                value = int(matrix.get(r - 1, c) | matrix.get(r - 1, c - index_val_map[r]))
            matrix.set(r, c, value)

    return bool(matrix.get(len(arr) - 1, k))


if __name__ == '__main__':
    print(subset_sum_k([9, 5, 4, 2, 1], 15))