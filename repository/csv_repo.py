import csv


class CsvRepo:
    def __init__(self, filename):
        self.filename = filename

    def _read_csv(self) -> list:
        with open(self.filename, newline='') as csvfile:
            data = list(csv.reader(csvfile))

        return data

    @staticmethod
    def _load_all_nodes(data):
        graph = {}
        for node in data:
            if node[0] not in graph:
                graph[node[0]] = dict()
            if node[1] not in graph:
                graph[node[1]] = dict()
        return graph

    def _process_csv_file(self, data):
        graph = self._load_all_nodes(data)

        for edge in data:
            cost = {edge[1]: int(edge[2])}
            graph[edge[0]].update(cost)
        return graph

    def load_csv_into_graph(self):
        data = self._read_csv()
        return self._process_csv_file(data)

    def add_line(self, line: list):
        with open(self.filename, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(line)
