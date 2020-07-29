import pytest
from flask import Flask

from api.rest.app import create_app


@pytest.fixture
def app() -> Flask:
    app = create_app()
    app.config['TESTING'] = True

    return app


@pytest.fixture
def api_client(app):
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def start_1():
    return 'GRU'


@pytest.fixture
def start_2():
    return 'BRC'


@pytest.fixture
def end_1():
    return 'CDG'


@pytest.fixture
def end_2():
    return 'ORL'


@pytest.fixture
def cost_1():
    return 40


@pytest.fixture
def cost_2():
    return 25


@pytest.fixture
def valid_graph():
    return {
        'GRU': {
            'BRC': 10,
            'CDG': 75,
            'SCL': 20,
            'ORL': 56
        },
        'BRC': {
            'SCL': 5,
        },
        'ORL': {
            'CDG': 5
        },
        'SCL': {
            'ORL': 20
        },
        'CDG': {}
    }


@pytest.fixture
def invalid_graph():
    return {
        'GRU': {
            'BRC': 10,
            'CDG': 75,
            'SCL': 20,
            'ORL': 56
        },
        'BRC': {
            'SCL': 5,
        },
        'ORL': {
            'CDG': 5
        },
        'SCL': {
            'ORL': 20
        }
    }
