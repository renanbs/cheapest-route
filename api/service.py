import os

from domain.cheapest_route_service import CheapestRouteService
from repository.csv_repo import CsvRepo


class RouteServiceException(Exception):
    pass


def _get_cheapest_route(graph, start, end) -> (str, str):
    sps = CheapestRouteService(graph, start, end)
    sps.find_cheapest_path()
    path = sps.get_shortest_path()
    if not path:
        raise RouteServiceException('Could not find route a suitable route.')
    return f'{" - ".join(path)}', sps.costs[end]


def get_cheapest_route_api(start, end) -> dict:
    repo = CsvRepo('input-file.csv')
    graph = repo.load_csv_into_graph()

    route, cost = _get_cheapest_route(graph, start, end)
    return {'best_route': route, 'cost': f'${cost}'}


def get_cheapest_route_cmd_line(filename, start, end) -> (str, str):
    if not os.path.exists(filename):
        raise RouteServiceException(f'Couldn\'t find {filename}')

    repo = CsvRepo(filename)
    graph = repo.load_csv_into_graph()
    return _get_cheapest_route(graph, start, end)


def add_line(start, end, cost):
    filename = 'input-file.csv'

    if not os.path.exists(filename):
        raise RouteServiceException(f'Couldn\'t find {filename}')

    repo = CsvRepo(filename)
    repo.add_line([start, end, cost])
