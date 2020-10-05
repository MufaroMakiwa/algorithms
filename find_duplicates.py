def find_duplicates(arr1, arr2):
    """
    Given two sorted arrays, return a list of all the numbers that appear in both lists
    """

    arr1_index = 0
    arr2_index = 0
    n = len(arr1)
    duplicates = set()

    while arr1_index < n and arr2_index < n:
        if arr1[arr1_index] < arr2[arr2_index]:
            arr1_index += 1

        elif arr2[arr2_index] < arr1[arr1_index]:
            arr2_index += 1

        else:
            duplicates.add(arr1[arr1_index])
            arr1_index += 1
            arr2_index += 1

    return duplicates


if __name__ == '__main__':
    arr_1 = [1, 2, 3, 4, 5]
    arr_2 = [1, 1, 6, 7, 8]

    print(find_duplicates(arr_1, arr_2))