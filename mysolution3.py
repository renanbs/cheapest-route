import csv

inf = float('inf')

start = 'GRU'
stop = 'CDG'

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


def read_csv():
    with open('input-file.txt', newline='') as csvfile:
        data = list(csv.reader(csvfile))

    return data


def _load_all_nodes(data):
    graph = {}
    for node in data:
        if node[0] not in graph:
            graph[node[0]] = dict()
        if node[1] not in graph:
            graph[node[1]] = dict()
    return graph


def process_csv_file(data):
    graph = _load_all_nodes(data)

    for edge in data:
        cost = {edge[1]: int(edge[2])}
        graph[edge[0]].update(cost)
    return graph


if __name__ == '__main__':
    data = read_csv()
    graph = process_csv_file(data)

    initialize_algorithm(costs, parents, graph)

    not_checked = [node for node in costs]
    node = find_cheapest_node(costs, not_checked)
    while not_checked:
        print(f'Not checked: {not_checked}')
        cost = costs[node]
        child_costs = graph[node]
        for c in child_costs:
            if costs[c] > cost + child_costs[c]:
                costs[c] = cost + child_costs[c]
                parents[c] = node

        not_checked.pop(not_checked.index(node))
        node = find_cheapest_node(costs, not_checked)
    print(f'Costs: {costs}')
    print(f'The cost to go from {start} to {stop} is {costs[stop]}!')

    print(get_the_path())



