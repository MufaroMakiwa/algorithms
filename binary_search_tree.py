import random

class Tree:

    def __init__(self, parent=None):
        self.key = None
        self.count = 0
        self.parent = parent
        self.left: Tree = None
        self.right: Tree = None

    def __str__(self):
        nodes = []
        for node in self:
            nodes.append(node)

        return str(nodes)

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

    def get_height(self, so_far=0):
        """
        :return: Height of the binary search tree
        """

        if self.left and self.right:
            return max(self.left.get_height(so_far + 1), self.right.get_height(so_far + 1))

        if self.left:
            return self.left.get_height(so_far + 1)

        if self.right:
            return self.right.get_height(so_far + 1)

        return so_far

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

    def is_balanced(self, left_h=0, right_h=0):
        """
        :return: True is the heights of the two subtrees of any node never differ by more than one
        """
        if abs(left_h - right_h) > 1:
            return False

        if self.left and self.right:
            if not self.left.is_balanced(left_h + 1, right_h + 1):
                return False

            if not self.right.is_balanced(left_h + 1, right_h + 1):
                return False

            return True

        if self.left:
            return self.left.is_balanced(left_h + 1, right_h)

        if self.right:
            return self.right.is_balanced(left_h, right_h + 1)

        return True

    def find_median(self):
        """
        :return: The median of the numbers in the BST
        """


if __name__ == '__main__':

    pass


