class Node:
    def __init__(self, value):
    	self.id = value
    	self.connections = []

class Graph:
	def __init__(self):
		self.nodes = []

	def addNodes(self,n):
		for i in range(n):
			self.nodes.append(Node(i))

	def connect(self, a, b):
		self.nodes[a].connections.append(self.nodes[b])
		self.nodes[b].connections.append(self.nodes[a])

	def find_all_distances(self, n):
		distances = [-1 for x in range(len(self.nodes))]


		queue = [(self.nodes[n],0)]
		visited = [False for x in range(len(self.nodes))]
		
		while len(queue) > 0:
			currentPoint, level = queue.pop(0)
			if visited[currentPoint.id] == False:
				visited[currentPoint.id] = True
				distances[currentPoint.id] = level * 6
				for node in currentPoint.connections:
					if not visited[node.id]:
						queue.append((node,level + 1))


		return distances



t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph()
    graph.addNodes(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1) 
    s = input()
    results = graph.find_all_distances(s-1)
    for index, val in enumerate(results):
    	if index != s - 1:
    		print val,
    print 
