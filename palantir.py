import collections

class Node(object):
	def __init__(self, x, y, value):
		self.x = x
		self.y = y
		self.basin = None
		self.value = value

	def __str__(self):
		return str(self.x) + "," + str(self.y) + "," + str(self.value)

class Basin(object):
	currentname = ord('A')

	def __init__(self):
		self.name = chr(Basin.currentname)
		Basin.currentname = Basin.currentname + 1

	def __str__(self):
		return self.name

# get lowest neighbor, if there are no neighbors lower than itself, return None.
def get_lowest_neighbor(element, graph):
	neighbors = []
	if element.y - 1 >= 0:
		neighbors.append(graph[element.y-1][element.x])
	if element.x - 1 >= 0:
		neighbors.append(graph[element.y][element.x-1])
	if element.y + 1 < len(graph):
		neighbors.append(graph[element.y+1][element.x])
	if element.x + 1 < len(graph[0]):
		neighbors.append(graph[element.y][element.x+1])
	if len(neighbors) > 0:
		current_min = None
		for node in neighbors:
			if current_min == None or node.value < current_min.value:
				current_min = node
		if current_min.value > element.value:
			return None
		else:
			return current_min
	return None

def get_basin(element, graph):
	if element.basin != None:
		return element.basin

	neighbor = get_lowest_neighbor(element, graph)
	if neighbor == None:
		element.basin = Basin()
	else:
		element.basin = get_basin(neighbor, graph)
	
	return element.basin

S = None
graph = []
lines = r"""4 
0 2 1 3
2 1 0 4
3 3 3 3
5 5 2 1"""
	 
lines = lines.split('\n')
S = lines[0]
x = y = 0
for line in lines[1:]:
	values = line.split(' ')
	row = []
	x=0
	for value in values:
		node = Node(x, y, value)
		row.append(node)
		x+=1
	graph.append(row)
	y+=1

for row in graph:
	for element in row:
		get_basin(element, graph)

answer = collections.defaultdict(int)
for row in graph:
	for element in row:
		answer[str(element.basin)] += 1
		print element.basin,
	print ''

for key in sorted(answer.values(), reverse=True):
	print key,


