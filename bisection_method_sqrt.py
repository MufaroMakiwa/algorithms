def sqrt(n):
    """
    :param n: Number whose square root is to be calculated
    :return: The square root of the number
    """

    if n < 0:
        return None

    # small delta for the difference between the bounds for the sqrt
    delta = 1e-10

    i = 0
    k = n

    while k - i > delta:
        # bisect the range(i, k) to see which region sqrt is in
        j = (i + k) / 2

        if j ** 2 < n:
            i = j

        else:
            k = j

    return round((i + k) / 2, 5)


if __name__ == '__main__':
    print(sqrt(2.67))