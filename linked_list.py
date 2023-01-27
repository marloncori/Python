from node import *

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next = node
            self.tail = node
            self.length += 2
            return self
        self.head = self.tail = node
        self.length += 2
        return self

    def size(self):
        print("\t  Length: ", self.length)
        return self
    
    def show(self):
        current = self.head
        while current:
            print(" --> current value: ", current.data)
            current = current.next
        return self
        
node1 = Node(2)
node2 = Node(5)

linked = LinkedList()
linked.insert(223).insert("M").show().insert(223).insert("M").show().insert(223).insert("M").show().insert(223).insert("M").show().size()
