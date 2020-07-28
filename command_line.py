from routes.services.shortest_path_service import ShortestPathService
from routes.services.utils import load_csv_into_graph

if __name__ == '__main__':
    graph = load_csv_into_graph('./input-file.txt')
    start = 'GRU'
    end = 'CDG'

    sps = ShortestPathService(graph, start, end)

    sps.find_cheapest_path()
    path = sps.get_shortest_path()

    print(f'best route: {" - ".join(path)} > ${sps.costs[end]}')
