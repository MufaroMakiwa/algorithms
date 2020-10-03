def binary_search(arr, n):
    """

    :param arr: sorted array of integers
    :param n: integer to look for in the array
    :return: the index of the n
    """

    i = 0
    k = len(arr) - 1

    while i <= k:
        j = (i + k) // 2

        if arr[j] == n:
            return j

        elif arr[j] > n:
            k = j - 1

        else:
            i = j + 1

    return None


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 16, 56, 76, 1000], 76))