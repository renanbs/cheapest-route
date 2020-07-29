from flask import json


class ApiSerializerException(Exception):
    pass


class ApiSerializer:
    def __init__(self, data, cost=False):
        self.data = json.loads(data)
        self.cost = cost

    def _has_valid_data(self, key):
        if not self.data.get(key):
            raise ApiSerializerException(f'{key} is required')

    def get(self, key):
        return self.data[key].upper()

    def is_valid(self):
        self._has_valid_data('start')
        self._has_valid_data('end')
        if self.cost:
            self._has_valid_data('cost')
