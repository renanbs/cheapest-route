class ShortestPathServiceException(Exception):
    pass


class ShortestPathService:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.costs = {}
        self.parents = {}

        self._initialize()

    def _initialize(self):
        if self.start not in self.graph or self.end not in self.graph:
            raise ShortestPathServiceException('Invalid starting/ending node')

        for node in self.graph:
            self.costs[node] = float('inf')
            self.parents[node] = {}

        self.costs[self.start] = 0

    @staticmethod
    def _find_cheapest_node(cost_to_node, not_checked_nodes):
        cheapest_node = None
        lowest_cost = float('inf')
        for node in not_checked_nodes:
            if cost_to_node[node] < lowest_cost:
                lowest_cost = cost_to_node[node]
                cheapest_node = node
        return cheapest_node

    def find_cheapest_path(self):
        not_checked_nodes = [node for node in self.costs]
        node = self._find_cheapest_node(self.costs, not_checked_nodes)
        while not_checked_nodes:
            cost = self.costs[node]
            child_costs = self.graph[node]
            for c in child_costs:
                if self.costs[c] > cost + child_costs[c]:
                    self.costs[c] = cost + child_costs[c]
                    self.parents[c] = node

            not_checked_nodes.pop(not_checked_nodes.index(node))
            node = self._find_cheapest_node(self.costs, not_checked_nodes)

    def get_shortest_path(self):
        if not self.costs[self.end] < float('inf'):
            return None

        path = [self.end]
        i = 0
        while self.start not in path:
            path.append(self.parents[path[i]])
            i += 1
        return path[::-1]
