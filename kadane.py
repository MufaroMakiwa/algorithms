import random


def maximum_sum(arr):
    """
    :param arr: A list of negative and non-negative integers
    :return: The maximum sum of any contiguous subarray
    """

    max_so_far = -float("inf")
    max_ending_here = 0

    for number in arr:
        max_ending_here += number
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


def maximum_sum_subarray(arr, n):
    """
    :param arr: A sequence of negative and positive numbers
    :param n: A sum for which we want to find a contiguous array of that sum
    :return: The subarray with that sum
    """

    prefix_totals = {}
    curr_sum = 0

    for i in range(n):
        curr_sum = curr_sum + arr[i]

        if curr_sum == n:
            return arr[: i + 1]

        v = curr_sum - n
        if (curr_sum - n) in prefix_totals:
            return arr[prefix_totals[curr_sum - n] + 1: i + 1]

        prefix_totals[curr_sum] = i

    return None


if __name__ == '__main__':

    arr = [-1, -2, 5, 6, 8, -12]
    n = maximum_sum(arr)
    print(maximum_sum_subarray(arr, n))