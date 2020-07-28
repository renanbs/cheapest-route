inf = float('inf')

start = 'GRU'
stop = 'CDG'

graph = {
    'GRU': {
        'BRC': 10,
        'CDG': 75,
        'SCL': 20,
        'ORL': 56
    },
    'BRC': {
        'SCL': 5,
    },
    'ORL': {
        'CDG': 5
    },
    'SCL': {
        'ORL': 20
    },
    'CDG': {}
}

costs = {}
parents = {}


def initialize_algorithm(costs, parents, graph):
    for node in graph:
        costs[node] = inf
        parents[node] = {}

    costs[start] = 0


def find_cheapest_node(cost_to_node, not_checked_nodes):
    cheapest_node = None
    lowest_cost = inf
    for node in not_checked_nodes:
        if cost_to_node[node] < lowest_cost:
            lowest_cost = cost_to_node[node]
            cheapest_node = node
    return cheapest_node


def get_the_path():
    if not costs[stop] < inf:
        return 'A path could not be found'


    path = [stop]
    i = 0
    while start not in path:
        path.append(parents[path[i]])
        i += 1
    return f'The shortest path is {path[::-1]}'


if __name__ == '__main__':
    import csv

    with open('testfile.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))

    print(data)


    initialize_algorithm(costs, parents, graph)

    not_checked = [node for node in costs]
    node = find_cheapest_node(costs, not_checked)
    while not_checked:
        print(f'Not checked: {not_checked}')
        cost = costs[node]
        child_cost = graph[node]
        for c in child_cost:
            if costs[c] > cost + child_cost[c]:
                costs[c] = cost + child_cost[c]
                parents[c] = node

        not_checked.pop(not_checked.index(node))
        node = find_cheapest_node(costs, not_checked)
    print(f'Costs: {costs}')
    print(f'The cost to go from {start} to {stop} is {costs[stop]}!')

    print(get_the_path())



