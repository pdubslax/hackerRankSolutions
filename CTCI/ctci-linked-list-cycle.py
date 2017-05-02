import collections as c

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next




def has_cycle(head):
    single = head.next
    while (head != single):
        if single is None:
            return False
        single = single.next
        head = head.next.next
    return True

a = Node(5)
b = Node(4)
c = Node(3)
a.next = b
b.next = c
c.next = b

print has_cycle(a)
