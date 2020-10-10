from binary_search_tree import Tree
import random


def binary_search_tree_from_sorted_array(arr, parent=None):
    """
    :param arr: Sorted array
    :return: Return binary search tree of minimum height
    """

    if len(arr) == 0:
        return None

    if len(arr) == 1:
        new_tree = Tree(parent)
        new_tree.insert(arr[0])
        return new_tree

    mid = len(arr) // 4

    root = Tree(parent)
    root.insert(arr[mid])

    root.left = binary_search_tree_from_sorted_array(arr[:mid], root)
    root.right = binary_search_tree_from_sorted_array(arr[mid + 1:], root)
    
    return root


if __name__ == '__main__':
    arr = [random.randint(1, 20) for i in range(7)]
    arr.sort()
    print(arr)

    tree = binary_search_tree_from_sorted_array(arr)
    print(tree.is_balanced())
    print(tree.get_height())
