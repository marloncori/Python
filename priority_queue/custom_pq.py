import heapq

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class PriorityQueue:
    def __init__(self):
        print(" Priority Queue has been created.")
        
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)

        priority_queue = []
        for lis in lists:
            if lis:
                heapq.heappush(priority_queue, lis)

        out = ListNode(None)
        head = out
        while priority_queue:
            lis = heapq.heappop(priority_queue)
            head.next = lis
            if lis and lis.next:
                heapq.heappush(priority_queue, lis.next)

        return out.next

node1 = ListNode(5)
node2 = ListNode(7)
node3 = ListNode(12)
node4 = ListNode(15)
node5 = ListNode(27)

nodes = [
    node1,
    node2,
    node3,
    node4,
    node5
]

pq = PriorityQueue()
new_node = pq.mergeKLists(nodes)
print(" Result = ", new_node.next)
