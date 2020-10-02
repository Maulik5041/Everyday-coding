class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, val):
        if val < self.val:
            if self.leftChild:
                self.leftChild.insert(val)
            else:
                self.leftChild = Node(val)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(val)
            else:
                self.rightChild = Node(val)
                return

    def search(self, val):
        if val < self.val:
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return False
        elif val > self.val:
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return False
        else:
            return True
        return False

    def delete(self, val):
        '''
        if current node's val is less than that of root node, then
        only search in left subtree otherwise right subtree
        '''
        if val < self.val:
            if(self.leftChild):
                self.leftChild = self.leftChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        elif val > self.val:
            if(self.rightChild):
                self.rightChild = self.rightChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        else:
            # deleting node with no children
            if self.leftChild is None and self.rightChild is None:
                self = None
                return None
            # deleting node with right child
            elif self.leftChild is None:
                tmp = self.rightChild
                self = None
                return tmp
            # deleting node with left child
            elif self.rightChild is None:
                tmp = self.leftChild
                self = None
                return tmp
            # deleting node with two children
            else:
                # first get the inorder successor
                current = self.rightChild
                # loop down to find the leftmost leaf
                while(current.leftChild is not None):
                    current = current.leftChild
                self.val = current.val
                self.rightChild = self.rightChild.delete(current.val)

        return self


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
        else:
            return False

    def delete(self, val):
        if self.root is not None:
            self.root = self.root.delete(val)


def find_min(root):
    if root is None:
        return None

    while root.leftChild:
        root = root.leftChild

    return root.val


def find_kth_max(root, k):
    tree = []
    in_order_traverse(root, tree)
    if len(tree) >= 0:
        return tree[-k]

    return None


def in_order_traverse(node, tree):
    if node:
        in_order_traverse(node.leftChild, tree)
        if len(tree) is 0:
            tree.append(node.val)

        elif tree[-1] is not node.val:
            tree.append(node.val)

        in_order_traverse(node.rightChild, tree)


BST = BinarySearchTree(6)
BST.insert(20)
BST.insert(-1)

print(find_min(BST.root))
