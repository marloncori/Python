from __future__ import print_function

class Node:
    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        # added to delete a node easier
        self.parent = parent

    def get_label(self):
        return self.label

    def set_label(self, value):
        self.label = value

    def get_left(self):
        return self.left

    def set_left(self, value):
        self.left = value

    def get_right(self):
        return self.right

    def set_right(self, value):
        self.right = value

    def get_parent(self):
        return self.parent

    def set_parent(self, value):
        self.parent = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, label):
        new_node = Node(label, None)
        if self.empty():
            self.root = new_node
        else:
            current_node = self.root
            # while we don`t get to a leaf
            while current_node is not None:
                # keep a reference to parent node
                parent_node = current_node
                if new_node.get_label() < current_node.get_label():
                    # move left
                    current_node = current_node.get_left()
                else:
                    current_node = current_node.get_right()

            # insert new node in a leaf
            if new_node.get_label() < parent_node.get_label():
                parent_node.set_left(new_node)
            else:
                parent_node.set_right(new_node)
            #Set parent to the new node
            new_node.set_parent(parent_node)
            
    def delete(self, label):
        if not self.empty():
            node = self.get_node(label)
            if node is not None:
                # node has no children
                if not node.get_left() and not node.get_right():
                    self.__reassign_nodes(node, None)
                    node = None
                elif not node.get_left() and node.get_right():
                    self.__reassign_nodes(node, node.get_right())
                elif node.get_left() and not node.get_right():
                    self.__reassign_nodes(node, node.get_left())
                # if node has two children
                else:
                    tmp_node = self.get_max(node.get_left())
                    self.delete(tmp_node.get_label())
                    node.set_label(tmp_node.get_label())
                    
    def get_node(self, label):
        curr_node = None
        if not self.empty():
            curr_node = self.get_root()
            # while node is not found
            # use lazy evaluation to avoid NoneType Attribute Error
            while curr_node and curr_node.get_label() is not label:
                if label < curr_node.get_label():
                    curr_node = curr_node.get_left()
                else:
                    curr_node = curr_node.get_right()
        return curr_node

    def get_max(self, root=None):
        if root:
            curr_node = root
        else:
            #We go deep on the right branch
            curr_node = self.get_root()
        if not self.empty():
            while curr_node.get_right():
                curr_node = curr_node.get_right()
        return curr_node

    def get_min(self, root=None):
        if root:
            curr_node = root
        else:

            curr_node = self.get_root()
        if not self.empty():
            curr_node = self.get_root()
            while curr_node.get_left():
                curr_node = curr_node.get_left()
        return curr_node

    def empty(self):
        return not self.root
       
    def __in_order_traversal(self, curr_node):
        node_list = []
        if curr_node:
            node_list.insert(0, curr_node)
            node_list = node_list + self.__in_order_traversal(curr_node.get_left())
            node_list = node_list + self.__in_order_traversal(curr_node.get_right())
        return node_list

    def get_root(self):
        return self.root

    def __is_right_children(self, node):
        return node == node.get_parent().get_right()

    def __reassign_nodes(self, node, new_children):
        if new_children:
            new_children.set_parent(node.get_parent())
        if node.get_parent():
            #If it is the Right Children
            if self.__is_right_children(node):
                node.get_parent().set_right(new_children)
            else:
                #Else it is the left children
                node.get_parent().set_left(new_children)

    #This function traverse the tree. By default it returns an
    #In order traversal list. You can pass a function to traverse
    #The tree as needed by client code
    def traversal_tree(self, traversal_function = None, root = None):
        if not traversal_function:
            #Returns a list of nodes in preOrder by default
            return self.__in_order_traversal(self.root)
        else:
            #Returns a list of nodes in the order that the users wants to
            return traversal_function(self.root)

    def __str__(self):
        """ returns an string of all the node labels
        present in the list in ordre traversal """
        all_nodes = self.__in_order_traversal(self.root)
        node_str = ""
        for one_node in all_nodes:
            node_str = node_str + " " + one_node.get_label().__str__()
        return node_str





























    

