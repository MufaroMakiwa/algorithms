def binary_search(arr, n, start=None, end=None):
    """
    Recursively search in sorted array arr for n
    :param arr: sorted array
    :param n: element to search for
    :param start: Starting index for the search
    :param end: Ending index for the search
    :return: Index of i in arr else None
    """

    if start is None:
        start = 0

    if end is None:
        end = len(arr) - 1

    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == n:
        return mid

    if arr[mid] > n:
        return binary_search(arr, n, start, mid - 1)

    return binary_search(arr, n, mid + 1, end)


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 16, 56, 76, 1000], 23))