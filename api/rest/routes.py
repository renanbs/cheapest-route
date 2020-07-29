from flask import Blueprint, request, json

from api.service import get_cheapest_route_api, RouteServiceException

bp = Blueprint('routes', __name__, url_prefix='/')


@bp.route('/routes/cheapest', methods=['POST'])
def cheapest_route():
    data = json.loads(request.data)
    start = data.get('start')
    end = data.get('end')

    try:
        return get_cheapest_route_api(start, end)
    except RouteServiceException as ex:
        return {'msg': str(ex)}


@bp.route('/routes', methods=['POST'])
def add_routes():
    return 'ok'
