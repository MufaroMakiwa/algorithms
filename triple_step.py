def tripple_step(n):
    """
    :param n: The number of steps on a staircase
    You can only do 1, 2 or 3 steps at a time
    :return: The number of ways to climb a staircase of n steps
    """

    memo = {0: 1}

    if n < 0:
        return 0

    if n not in memo:
        memo[n] = tripple_step(n - 1) + tripple_step(n - 2) + tripple_step(n - 3)

    return memo[n]


if __name__ == '__main__':
    print(tripple_step(5))