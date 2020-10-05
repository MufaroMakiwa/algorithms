def permutations(arr):
    """
    :param arr: A sequence of characters
    :return: A list of all the possible permutations
    """
    n = len(arr)

    if n == 1:
        return [arr]

    sub_permutations = []
    next_char = arr[n - 1]

    for permutation in permutations(arr[:n - 1]):
        for i in range(n):
            new_perm = permutation[:i] + [next_char] + permutation[i:]
            sub_permutations.append(new_perm)

    return sub_permutations


if __name__ == '__main__':
    print(len(permutations([1, 2, 3, 4, 5, 6])))
