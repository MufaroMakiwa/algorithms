def combinations(arr, n):
    """
    :param arr: A list of distinct integers
    :param n: Size of each combination
    :return: A list of all combinations of size n
    """

    if n == 0:
        yield []

    else:
        for i in range(len(arr) - n + 1):
            for next_ in combinations(arr[i + 1:], n - 1):
                yield [arr[i]] + next_


if __name__ == '__main__':
    for combination in combinations([1, 2, 3, 4, 5], 4):
        print(combination)