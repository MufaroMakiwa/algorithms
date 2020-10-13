import random

def maximum_length_sorted_array(arr):
    """
    :param arr: Array or integers
    :return: Longest sorted subarray in ascending order
    """

    # initialize a left pointer to the beginning of subarray being checked
    left_pointer = 0

    # initialize a right pointer to the end of subarray being checked (runner)
    right_pointer = 0

    # keep track of the subarray being formed
    length_so_far = 0

    # keep track of the maximum length of sorted subarray
    max_len = -float("inf")

    # start index of max_length sorted subarray
    max_len_start = None

    # end index of max_length sorted subarray
    max_len_end = None

    while right_pointer < len(arr):

        # increase the count of the max_length
        if right_pointer == left_pointer or arr[right_pointer] >= arr[right_pointer-1]:
            length_so_far += 1
            right_pointer += 1

        else:
            # if subarray so far is longer than max_length subarray
            if length_so_far > max_len:

                # update max_length
                max_len = length_so_far

                # update max length start and end indices
                max_len_start, max_len_end = left_pointer, right_pointer

            # update left pointer
            left_pointer = right_pointer

            # reset length so far
            length_so_far = 0

    # if maximum length is at the end of the array, this check will not be done in the loop
    if length_so_far > max_len:
        max_len_start, max_len_end = left_pointer, right_pointer

    return arr[max_len_start: max_len_end]


if __name__ == '__main__':
    arr = [random.randint(10, 99) for i in range(20)]
    print(arr)
    print(maximum_length_sorted_array(arr))