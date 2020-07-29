from http import HTTPStatus

from flask import Blueprint, request, json

from api.rest.serializer import ApiSerializer, ApiSerializerException
from api.service import get_cheapest_route_api, RouteServiceException, add_line
from domain.cheapest_route_service import CheapestRouteServiceException

bp = Blueprint('routes', __name__, url_prefix='/')


@bp.route('/routes/cheapest', methods=['POST'])
def cheapest_route():
    try:
        serializer = ApiSerializer(request.data)
        serializer.is_valid()

        return get_cheapest_route_api(serializer.get('start'), serializer.get('end'))
    except RouteServiceException as ex:
        return {'msg': str(ex)}

    except (CheapestRouteServiceException, ApiSerializerException) as ex:
        return {'msg': str(ex)}, HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route('/routes', methods=['POST'])
def add_routes():
    try:
        serializer = ApiSerializer(request.data, cost=True)
        serializer.is_valid()

        add_line(serializer.get('start'), serializer.get('end'), serializer.get('cost'))
    except RouteServiceException as ex:
        return {'msg': str(ex)}

    except ApiSerializerException as ex:
        return {'msg': str(ex)}, HTTPStatus.UNPROCESSABLE_ENTITY

    return {'msg': 'New route added successfully.'}
