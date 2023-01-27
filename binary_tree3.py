class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None    
    @property
    def get_value(self):
        return self.value

    @property
    def get_left(self):
        return self.left

    @property
    def get_right(self):
        return self.right

    @get_left.setter
    def set_left(self, left_node):
        self.left = left_node
    
    @get_value.setter
    def set_value(self, value):
        self.value = value
    
    @get_right.setter
    def set_right(self, right_node):
        self.right = right_node


class BinaryTree:
    def __init__(self):
        self._node = None
        self._x = 0
        
    def create(self):
        self._node = Node() #creating new node.
        self._x = int(input("Enter the node data \n (-1 for null): "))
        if self._x == -1: #for defining no child.
            return self.get_node()

        self._node.set_value = self._x #setting the value of the node.
        print("Enter the left child of '{}'".format(self._x))
        self._node.set_left = self.create() #setting the left subtree
        print("Enter the right child of '{}'".format(self._x))
        self._node.set_right = self.create() #setting the right subtree.

    def get_node(self):
        return self._node
    
    def pre_order(self, root):
        if root:
            print(root.get_value)
            self.pre_order(root.get_left)
            self.pre_order(root.get_right)

if __name__ == '__main__':
    try:
        tree = BinaryTree()
        root_node = tree.create()
        tree.pre_order(root_node)
        
    except KeyboardInterrupt:
        print(" Program has ended")