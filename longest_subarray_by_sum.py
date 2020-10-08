import random


def longest_subarray_array_by_sum(arr, n):
    """
    :param arr: Array of integer
    :param n: Sum to look for
    :return: The longest array of given sum
    """

    # each total maps to an index up to which the sum is total
    prefix_totals = {}

    # the highest length of subarray of sum n so far
    max_subarray_len = -float("inf")

    # the sum so far up to the given index
    current_sum = 0

    # starting index for the maximum sum subarray
    start_index = None

    # ending index for the maximum sum subarray
    end_index = None

    for i in range(len(arr)):
        # add to current sum
        current_sum += arr[i]

        # add the sum to the
        if current_sum not in prefix_totals:
            prefix_totals[current_sum] = i

        if current_sum == n:
            if i + 1 > max_subarray_len:
                start_index = 0
                end_index = i + 1
                max_subarray_len = i + 1

        else:
            diff = current_sum - n
            if diff in prefix_totals:
                start = prefix_totals[diff]
                if i - start > max_subarray_len:
                    start_index = start + 1
                    end_index = i + 1
                    max_subarray_len = i + 1

    if start_index is None:
        return [-1]

    return arr[start_index: end_index]


if __name__ == '__main__':
    arr = [random.randint(- 10 ** 5, 10 ** 5) for _ in range(10 ** 4)]
    r = random.randint(0, 20)
    print(r)
    print(longest_subarray_array_by_sum(arr, r))