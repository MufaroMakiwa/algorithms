import random

class Tree:

    def __init__(self, parent=None):
        self.key = None
        self.count = 0
        self.parent = parent
        self.left = None
        self.right = None
        self.median = None

    def __contains__(self, item):
        if self.key < item:
            if self.right:
                return self.right.__contains__(item)
            else:
                return False

        elif self.key > item:
            if self.left:
                return self.left.__contains__(item)
            else:
                raise False

        else:
            return True

    def __iter__(self):
        if self.left:
            yield from self.left.__iter__()

        for _ in range(self.count):
            yield self.key

        if self.right:
            yield from self.right.__iter__()

    def insert(self, node):
        """
        :param node: Node to insert into the BST
        """
        if self.key is None:
            self.key = node
            self.count += 1
            return

        if self.key == node:
            self.count += 1

        if self.key > node:
            if not self.left:
                self.left = Tree(self)
            self.left.insert(node)

        if self.key < node:
            if not self.right:
                self.right = Tree(self)
            self.right.insert(node)

    def find_min(self):
        """
        :return: The minimum number in the BST
        """
        if self.left:
            return self.left.find_min()
        return self.key

    def find_max(self):
        """
        :return: The maximum number in the BST
        """
        if self.right:
            return self.right.find_max()
        return self.key

    def find_median(self):
        """
        :return: The median of the numbers in the BST
        """


if __name__ == '__main__':

    tree = Tree()

    for i in range(10):
        tree.insert(random.randint(1, 10))

    print(list(tree))
