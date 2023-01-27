# https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2279s
# FreeCodeCamp - 10 Common Coding Interview Problems
# 5 - matching parenthesis problem (30-05-2022) 
# T(n) = O(n), S(n) = O(logn)
# 
###########################################################
def is_valid(combination):
    stack = []
    for par in combination:
        if par == '(':
            stack.append(par)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

def is_valid2(combination):
    diff = 0
    for par in combination:
        if par == '(':
            diff += 1
        else:
            if diff == 0:
                return False
            else:
                diff -= 1
    return diff == 0
###########################################################

def show_result(output):
    if not output:
        print(f'\n\t The output parameter is empty!')
        return

    if output is not -1:
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