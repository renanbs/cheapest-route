from api.service import get_cheapest_route_cmd_line, RouteServiceException
from domain.cheapest_route_service import CheapestRouteServiceException


def process(arguments):
    if len(arguments) != 2:
        print(f'\nYou need to provide a input file. \n\nEx.: python {arguments[0]} my-file.csv')
        exit(-1)

    filename = arguments[1]

    try:
        entered_input = input('please enter the route: ')
        splitted = entered_input.split('-')
        start = splitted[0].upper()
        end = splitted[1].upper()
    except IndexError:
        print('\nYou need to enter the route in the following format: START-END')
        exit(-1)

    try:
        route, cost = get_cheapest_route_cmd_line(filename, start, end)
    except (RouteServiceException, CheapestRouteServiceException) as ex:
        print(f'\n{str(ex)}')
        exit(-1)

    print(f'best route: {route} > ${cost}')
