from unittest.mock import patch

from api.cmd.routes import process


def test_should_not_process_arguments(start_1):
    with patch('builtins.print') as p:
        response = process([''])
    assert response == -1
    p.assert_called_with('\nYou need to provide a input file. \n\nEx.: python  my-file.csv')


def test_should_find_cheapest_route(api_client, start_1, end_1, mocker):
    mocker.patch('builtins.input', return_value=f'{start_1}-{end_1}')
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('repository.csv_repo.CsvRepo.load_csv_into_graph')
    mocker.patch('api.service._get_cheapest_route', return_value=('XYZ', 40))
    with patch('builtins.print') as p:
        response = process(['', 'my_filename.csv'])
    assert response != -1
    p.assert_called_with('best route: XYZ > $40')
