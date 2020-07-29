from api.cmd.serializer import CmdSerializerException, CmdSerializer
from api.service import get_cheapest_route_cmd_line, RouteServiceException
from domain.cheapest_route_service import CheapestRouteServiceException


def process(arguments):
    if len(arguments) != 2:
        print(f'\nYou need to provide a input file. \n\nEx.: python {arguments[0]} my-file.csv')
        return -1

    filename = arguments[1]

    try:
        entered_input = input('please enter the route: ')
        serializer = CmdSerializer(entered_input)
        serializer.is_valid()

        route, cost = get_cheapest_route_cmd_line(filename, serializer.get('start'), serializer.get('end'))
    except (RouteServiceException, CheapestRouteServiceException, CmdSerializerException) as ex:
        print(f'\n{str(ex)}')
        return -1

    print(f'best route: {route} > ${cost}')
