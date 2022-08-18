"""ExampleInfrastrucure class - subclass of Infrastructure

"""

from assets.infrastructure import Infrastructure


class ExampleInfrastructure(Infrastructure):

    def __init__(self, location: object):
        super().__init__("Example infrastructure", "wealth", "Blah blah blah", 5, location)