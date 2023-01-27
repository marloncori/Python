# binary search tree test
from binary_search_tree import BinarySearchTree

def in_pre_order(curr_node):
    node_list = []
    if curr_node:
        node_list += in_pre_order(curr_node.get_left())
        node_list.insert(0, curr_node.get_label())
        node_list += in_pre_order(curr_node.get_right())
    return node_list

def test_bst():
    r'''
    Example
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13 
    '''

    r'''
    Example After Deletion
                  7
                 / \
                1   4

    '''
    t = BinarySearchTree()
    t.insert(8)
    t.insert(3)
    t.insert(6)
    t.insert(1)
    t.insert(10)
    t.insert(14)
    t.insert(13)
    t.insert(4)
    t.insert(7)

    #Prints all the elements of the list in order traversal
    print(t.__str__())

    if t.get_node(6):
        print("The label 6 exists")
    else:
        print("The label 6 doesn't exist")

    if t.get_node(-1):
        print("The label -1 exists")
    else:
        print("The label -1 doesn't exist")

    if not t.empty():
        print("Max Value: ", t.get_max().get_label())
        print("Min Value: ", t.get_min().get_label())

    t.delete(13)
    t.delete(10)
    t.delete(8)
    t.delete(3)
    t.delete(6)
    t.delete(14)

    #Gets all the elements of the tree In pre order
    #And it prints them
    nodelist = t.traversal_tree(in_pre_order, t.root)
    for node in nodelist:
        print(node)

if __name__ == "__main__":
    try:
        test_bst()
        
    except (KeyboardInterrupt, SystemExit):
        print(" User has stopped program")
