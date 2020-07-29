from flask import Blueprint, request, json

from domain.shortest_path_service import ShortestPathService

bp = Blueprint('routes', __name__, url_prefix='/')


@bp.route('/routes/cheapest', methods=['POST'])
def cheapest_route():
    data = json.loads(request.data)
    start = data.get('start')
    end = data.get('end')
    graph = {}
    sps = ShortestPathService(graph, start, end)

    return f'{start}'


@bp.route('/routes', methods=['POST'])
def add_routes():
    return 'ok'
