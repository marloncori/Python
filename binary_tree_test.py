from binary_tree2 import BinaryTree

def test_binary_tree():
    t = BinaryTree()
    t.insert(5)
    t.insert(8)
    t.insert(3)
    t.insert(4)
    t.insert(6)
    t.insert(2)
        
    t.delete(8) 
    t.delete(5)

    t.insert(9)
    t.insert(1)

    t.delete(2)
    t.delete(100)

    # Remember: Find method return the node object. 
    # To return a number use t.find(nº).key
    # But it will cause an error if the number is not in the tree.
    node = t.find(5)
    if node:
        print(node.key)
    else:
        print(" 5 is not in tree. Node has been deleted!")

    node2 = t.find(8)
    if node2:
        print(node2.key)
    else:
        print(" 8 is not in tree. Node has been deleted!")
        
    node3 = t.find(4)
    if node3:
        print(node3.key)
    else:
        print(" 4 is not in tree. Node has been deleted!")

    node4 = t.find(9)
    if node4:
        print(node4.key)
    else:
        print(" 9 is not in tree. Node has been deleted!")
    del t

if __name__ == '__main__':
    test_binary_tree()
