class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head: Node = Node()

    def __iter__(self):
        current_node = self.head

        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

    def __str__(self):
        values = [value for value in self]
        return str(values)

    def insert_start(self, value):
        """
        :param value: Integer to insert at the start
        :return: None
        """
        if self.is_empty():
            self.head = Node(value)

        else:
            new_head = Node(value)
            new_head.next = self.head
            self.head = new_head

    def insert_end(self, value):
        """
        :param value: Number to be inserted
        :return: None
        """
        if self.is_empty():
            self.head = Node(value)

        current_node = self.head
        while True:
            if current_node.next is None:
                new_node = Node(value)
                current_node.next = new_node
                break

            current_node = current_node.next

    def is_empty(self):
        return self.head.value is None


def return_kth_to_last(linked_list: LinkedList, k):
    """
    :param linked_list: Linked list
    :param k: The value from last to return
    :return: The kth value from last
    """

    def find_kth(node):
        """
        :param node: Current node
        :return: The position from last or the kth value
        """

        if node is None:
            return 1

        current_position = find_kth(node.next)
        if isinstance(current_position, Node):
            return current_position

        elif current_position == k:
            return node

        else:
            return current_position + 1

    kth_value = find_kth(linked_list.head)
    if isinstance(kth_value, int):
        return None
    else:
        return kth_value.value


if __name__ == '__main__':
    list_ = LinkedList()
    list_.insert_start(4)
    list_.insert_start(1)
    list_.insert_end(2)
    list_.insert_start(34)
    list_.insert_start(1)
    print(list_)

    print(return_kth_to_last(list_, 20))
