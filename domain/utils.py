from repository.file import read_csv


def _load_all_nodes(data):
    graph = {}
    for node in data:
        if node[0] not in graph:
            graph[node[0]] = dict()
        if node[1] not in graph:
            graph[node[1]] = dict()
    return graph


def _process_csv_file(data):
    graph = _load_all_nodes(data)

    for edge in data:
        cost = {edge[1]: int(edge[2])}
        graph[edge[0]].update(cost)
    return graph


def load_csv_into_graph(filename) -> dict:
    data = read_csv(filename)
    return _process_csv_file(data)
