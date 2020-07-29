from http import HTTPStatus


def test_should_not_find_route_without_end(api_client, start_1):
    response = api_client.post('/routes/cheapest', json=dict(start=start_1))
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json == {'msg': 'end is required'}


def test_should_find_cheapest_route(api_client, start_1, end_1, mocker):
    mocker.patch('repository.csv_repo.CsvRepo.load_csv_into_graph')
    mocker.patch('api.service._get_cheapest_route', return_value=('XYZ', 40))
    response = api_client.post('/routes/cheapest', json=dict(start=start_1, end=end_1))

    assert response.status_code == HTTPStatus.OK
    assert response.json == {'best_route': 'XYZ', 'cost': '$40'}


def test_should_add_new_route(api_client, start_1, end_1, mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('repository.csv_repo.CsvRepo.add_line')
    response = api_client.post('/routes', json=dict(start=start_1, end=end_1, cost='45'))

    assert response.status_code == HTTPStatus.OK
    assert response.json == {'msg': 'New route added successfully.'}


def test_should_not_add_route_without_end(api_client, start_1):
    response = api_client.post('/routes', json=dict(start=start_1))
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json == {'msg': 'end is required'}
