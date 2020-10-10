# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[ListNode], start=None, end=None) -> ListNode:

        if len(lists) == 0:
            return None

        if end is None:
            end = len(lists)

        if end - start == 1:
            return lists[start]

        mid = (start + end) // 2

        left = self.mergeKLists(lists, start, mid)
        right = self.mergeKLists(lists, mid, end)

        merged_lr = current_node = ListNode()

        while left and right:

            if left.val < right.val:
                new_node = ListNode(left.val)
                left = left.next

            else:
                new_node = ListNode(right.val)
                right = right.next

            current_node.next = new_node
            current_node = new_node

        if left is None:
            current_node.next = right
        else:
            current_node.next = left

        return merged_lr.next


if __name__ == '__main__':
    pass