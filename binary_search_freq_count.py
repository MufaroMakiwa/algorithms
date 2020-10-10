import random


def binary_search_freq_count(arr, n, start=0, end=None):
    """
    :param end:
    :param start:
    :param arr: sorted array of integers
    :param n: integer to look for in the array
    :return: the index of the n
    """

    if end is None:
        end = len(arr)

    if start >= end:
        return 0

    mid = (start + end) // 2

    if arr[mid] == n:
        left_count = binary_search_freq_count(arr, n, start, mid)
        right_count = binary_search_freq_count(arr, n, mid + 1, end)
        return 1 + left_count + right_count

    elif arr[mid] > n:
        return binary_search_freq_count(arr, n, start, mid)

    else:
        return binary_search_freq_count(arr, n, mid + 1, end)


if __name__ == '__main__':
    arr = [random.randint(0, 10) for i in range(20)]
    arr.sort()
    n = random.randint(0, 10)
    print(arr)
    print("n =", n)
    print()
    print("count =", binary_search_freq_count(arr, n))


