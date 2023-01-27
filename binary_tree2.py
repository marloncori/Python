# Binary Tree implementation
class Node:
    def __init__(self, key, parent_node = None):
        self.left = None
        self.right = None
        self.key = key
        if not parent_node:
            self.parent = self
        else:
            self.parent = parent_node

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if not self.root:
            self.root = Node(x)
        else:
            self._insert(x, self.root)

    def is_less(self, x, y):
        return x < y
    
    def _insert(self, x, node):
        if self.is_less(x, node.key):
            if not node.left:
                node.left = Node(x, node)
            else:
                self._insert(x, node.left)
        else:
            if not node.right:
                node.right = Node(x, node)
            else:
                self._insert(x, node.right)

    def find(self, x):
        if not self.root:
            return None
        else:
            return self._find(x, self.root)
        
    def _find(self, x, node):
        if x == node.key:
            return node
        elif x < node.key:
            if not node.left:
                return None
            else:
                return self._find(x, node.left)
        else:
            if not node.right:
                return None
            else:
                return self._find(x, node.right)

    def next(self, node):
        if node.right:
            return self._left_descendant(node.right)
        else:
            return self._right_ancestor(node)

    def _left_descendant(self, node):
        if not node.left:
            return node
        else:
            return self._left_descendant(node.left)
    def _right_ancestor(self, node):
        if node.key <= node.parent.key:
            return node.parent
        else:
            return self._right_ancestor(node.parent)

    def delete(self, x):
        node = self.find(x)
        if not node:
            print(f"\n\t The value {x} is not present in the Binary Tree!")
        else:
            if not node.right:
                if not node.left:
                    if self.is_less(node.key, node.parent.key):
                        node.parent.left = None
                        del node # Clean garbage
                    else:
                        node.parent.right = None
                        del node
                else:
                    node.key = node.left.key
                    node.left = None
            else:
                x = self.next(node)
                node.key = x.key
                x = None
