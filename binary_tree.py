
class Node(object):
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None

def create_node(value):
    node = Node()
    node.data = value
    node.left = None
    node.right = None
    print(" Node has been created!")
    return node

def insert_node(node, value):
    if not node.data:
        node = create_node(value)
        print(" Node has been created before insertion!")
    else:
        root_value = node.data
        if value > root_value:
            insert_node(node.right, value)
        else:
            insert_node(node.left, value)
    return node

num = 8
num2 = 17
num3 = 5

my_node = Node()
my_node = create_node(num)

new_node = insert_node(my_node, num2)
next_node = insert_node(new_node, num3)

print(next_node.data)
print(next_node.right.data)
print(next_node.left.data)