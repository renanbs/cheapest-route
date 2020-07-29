import os

from domain.cheapest_route_service import CheapestRouteService
from domain.utils import load_csv_into_graph


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

    graph = load_csv_into_graph('input-file.txt')

    route, cost = _get_cheapest_route(graph, start, end)
    return {'best_route': route, 'cost': f'${cost}'}


def get_cheapest_route_cmd_line(filename, start, end) -> (str, str):
    if not os.path.exists(filename):
        raise RouteServiceException(f'Couldn\'t find {filename}')

    graph = load_csv_into_graph('input-file.txt')
    return _get_cheapest_route(graph, start, end)
