class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if not self.second:
            return self.first[0]
        return self.second[-1]

    def pop(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())
        self.second.pop()

    def put(self, value):
        self.first.append(value)

queue = MyQueue()
queue.put(5)
queue.put(6)
queue.pop()
print queue.peek()
queue.put(6)
queue.put(7)
queue.put(2)
queue.pop()
print queue.peek()
queue.pop()
queue.pop()
print queue.peek()


# t = int(raw_input())
# for line in xrange(t):
#     values = map(int, raw_input().split())

#     if values[0] == 1:
#         queue.put(values[1])
#     elif values[0] == 2:
#         queue.pop()
#     else:
#         print queue.peek()
