# https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2279s
# FreeCodeCamp - 10 Common Coding Interview Problems
# 4 - simetric tree problem (30-05-2022) 
# T(n) = O(n), S(n) = O(logn)
# it is solved with Depth First Search for tree_sum
###########################################################
from binary_tree2 import BinaryTree
###########################################################
def tree_sum(root):
    if not root:
        return 0
    else:
        left = tree_sum(root.left)
        right = tree_sum(root.right)
        return root.key + left + right
    
###########################################################
def are_symmetric(root1, root2):
    if not root1 and not root2:
        return True
    elif ((root1 is None) is not (root2 is None)) or root1.key is not root2.key:
        return False
    else:
        return are_symmetric(root1.left, root2.left)\
               and are_symmetric(root1.right, root2.right)
    
###########################################################
def is_symmetric(root):
    if not root:
        return True
    return are_symmetric(root.left, root.right)

###########################################################
def show_result(output, identity=False):
    if not output and not identity:
        print(f'\n\t The output parameter is empty!')
        return
    
    if identity:
        if output:
            print(f"\n\t >> Both trees are symmetric!")
        else:
            print(f"\n\t [WARNING] Binary trees are not symmetric...")
    else:        
        if output != -1:
            print(f"\n\t The tree sum value is '{output}'.")
        else:
            print(f'\n\t There is no positive result to be showed.')
        
###########################################################
def run_test():
    nums = [5, 8, 3, 4, 6, 7, 2]
    tree_A = BinaryTree()
    for num in nums:
        tree_A.insert(num)
    sum_A = tree_sum(tree_A.root)
    
    tree_B = BinaryTree()
    for num in nums:
        tree_B.insert(num)
    sum_B = tree_sum(tree_B.root)
    
    vals = [8, 3, 1, 6, 7, 10, 9]
    identity = are_symmetric(tree_A.root, tree_B.root)
    show_result(identity, True)
    
    tree_C = BinaryTree()
    for val in vals:
        tree_C.insert(val)
    sum_C = tree_sum(tree_C.root)
    
    identity = are_symmetric(tree_A.root, tree_C.root)
    show_result(identity, True)
    
    tree_D = BinaryTree()
    sum_D = tree_sum(tree_D.root)
    
    identity = are_symmetric(tree_D.root, tree_C.root)
    show_result(identity, True)
    
    tree_E = BinaryTree()
    for val in vals:
        tree_E.insert(val)
    sum_E = tree_sum(tree_E.root)

    identity = are_symmetric(tree_C.root, tree_E.root)
    show_result(identity, True)
    
    sums = [sum_A, sum_B, sum_C, sum_E, sum_D]
    for s in sums:
        show_result(s)
        
    trees = [tree_A, tree_B, tree_C, tree_D, tree_E]
    for tree in trees:
        del tree
        print(" [INFO] Tree deleted!")
###########################################################
def cleanup():
    print(' User has stopped program execution. Goodbye!')

###########################################################
if __name__ == '__main__':
    try:
        run_test()    
        
    except (KeyboardInterrupt, SystemExit):
        cleanup()
###########################################################