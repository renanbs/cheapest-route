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