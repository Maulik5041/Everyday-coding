class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)

        else:
            self.root = Node(val)
            return True

    def search(self, val):
        if self.root:
            return self.root.search(val)
        return False

    def delete(self, val):
        if self.root:
            self.root = self.root.delete(val)
        else:
            return False


BST = BinarySearchTree(6)
print(BST.root.val)
