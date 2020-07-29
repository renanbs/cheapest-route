
class CmdSerializerException(Exception):
    pass


class CmdSerializer:
    def __init__(self, the_input):
        self.the_input = the_input
        self.data = {}

    def get(self, key):
        return self.data[key]

    def is_valid(self):
        try:
            splitted = self.the_input.split('-')
            self.data['start'] = splitted[0].upper()
            self.data['end'] = splitted[1].upper()
        except IndexError:
            raise CmdSerializerException('\nYou need to enter the route in the following format: START-END')
