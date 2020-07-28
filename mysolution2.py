class Node:
    def __init__(self, label: str):
        self.label = label

    def __eq__(self, other):
        return self.label == other.label

    def __str__(self):
        return self.label

    def __hash__(self):
        return hash(self.label)


class Edge:
    def __init__(self, to_node: Node, length: int):
        self.to_node = to_node
        self.length = length

    def __eq__(self, other):
        return self.to_node == other.to_node and \
               self.length == other.to_node

    def __str__(self):
        return f'{self.to_node}: {self.length}'


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node: Node):
        self.nodes.add(node)

    def add_edge(self, from_node: Node, to_node: Node, length: int):
        edge = Edge(to_node, length)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge


graph = Graph()

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
graph.add_node(a)
graph.add_node(b)
graph.add_node(c)
graph.add_node(d)

graph.add_edge(a, b, 1)
graph.add_edge(a, c, 3)
graph.add_edge(b, c, 1)
graph.add_edge(b, d, 5)
graph.add_edge(c, d, 3)


costs = {}
parents = {}

inf = float('inf')

start = a
stop = d


def initialize(graph):
    for node in graph:
        costs[node] = inf
        parents[node] = {}

    costs[start] = 0


initialize(graph)

