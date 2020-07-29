import os
import sys

from domain.shortest_path_service import ShortestPathService
from domain.utils import load_csv_into_graph

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print(f'You need to provide a input file. \n\nEx.: python {sys.argv[0]} my-file.csv')
        exit(-1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f'Couldn\'t find {filename}')
        exit(-1)
    graph = load_csv_into_graph(filename)

    try:
        entered_input = input('please enter the route: ')
        splitted = entered_input.split('-')
        start = splitted[0].upper()
        end = splitted[1].upper()
    except IndexError:
        print('You need to enter the route in the following format: START-END')
        exit(-1)

    sps = ShortestPathService(graph, start, end)

    sps.find_cheapest_path()
    path = sps.get_shortest_path()

    print(f'best route: {" - ".join(path)} > ${sps.costs[end]}')
