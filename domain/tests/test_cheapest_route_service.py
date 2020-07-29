import pytest

from domain.cheapest_route_service import CheapestRouteService, CheapestRouteServiceException


@pytest.fixture
def cheapest_route_1():
    return ['GRU', 'BRC', 'SCL', 'ORL', 'CDG']


@pytest.fixture
def cheapest_route_2():
    return ['BRC', 'SCL', 'ORL']


@pytest.fixture
def costs_1():
    return {'GRU': 0, 'BRC': float('inf'), 'ORL': float('inf'), 'SCL': float('inf'), 'CDG': float('inf')}


@pytest.fixture
def parents_1():
    return {'GRU': {}, 'BRC': {}, 'ORL': {}, 'SCL': {}, 'CDG': {}}


def test_should_initialize_a_valid_graph(valid_graph, start_1, end_1, costs_1, parents_1):
    crs = CheapestRouteService(valid_graph, start_1, end_1)
    assert crs.costs == costs_1
    assert crs.parents == parents_1


def test_should_not_initialize_a_valid_graph(invalid_graph, start_1, end_1, parents_1):
    with pytest.raises(CheapestRouteServiceException) as e:
        CheapestRouteService(invalid_graph, start_1, end_1)
    assert str(e.value) == 'Invalid starting/ending node'


@pytest.mark.parametrize('start, end, cheapest_route, cost', [
    (pytest.lazy_fixture('start_1'), pytest.lazy_fixture('end_1'),
     pytest.lazy_fixture('cheapest_route_1'), pytest.lazy_fixture('cost_1')),
    (pytest.lazy_fixture('start_2'), pytest.lazy_fixture('end_2'),
     pytest.lazy_fixture('cheapest_route_2'), pytest.lazy_fixture('cost_2'))
])
def test_should_find_cheapest_route(valid_graph, start, end, cheapest_route, cost):
    crs = CheapestRouteService(valid_graph, start, end)
    crs.find_cheapest_path()
    route_found = crs.get_shortest_path()
    assert route_found == cheapest_route
    assert crs.costs[end] == cost
